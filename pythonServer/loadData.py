# import required modules

import json
import requests
from domain.anime import Anime
from domain.anime import Param

# base_url variable to store url
url = "https://api.jikan.moe/v4/anime/"


# complete_url variable to store
# complete url address


# get method of requests module
# return response object

def load_data():
    sfw = "true"

    order_by = "title"

    minScore = None
    if order_by == "score":
        minScore = input("Select minimal score for anime form 1 - 9:")

    sort = "asc"

    paramObject = Param(sfw, order_by, minScore, sort)

    print("This is param object: " + paramObject.__str__())

    response = requests.get(url, params={"sfw": paramObject.sfw, "sort": paramObject.sort,
                                         "order_by": paramObject.order_by, "min_score": paramObject.minScore})

    # json method of response object
    # convert json format data into
    # python format data
    dataAsJson = response.json()
    animeList = []
    # Check the value of "data" key is set
    if dataAsJson["data"]:

        # store the value of "data"
        loaded_anime = dataAsJson["data"]

        for anime in loaded_anime:
            # one way to set data on object
            print(anime)
            animeObject = Anime(anime["title"], anime["title_japanese"], anime["type"],
                                anime["status"], anime["episodes"], anime["rating"], anime["url"], anime["images"]["jpg"]["image_url"])

            # print("This is anime: " + animeObject.__str__())
            animeList.append(animeObject)


    else:
        print(" Api not working ")

    output = []
    for anime in animeList:
        output.append(anime.to_json())
        print(anime.to_json())
    return output
