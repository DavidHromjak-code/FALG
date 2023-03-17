# import required modules
import requests
from domain.anime import Anime

# base_url variable to store url
url = "https://api.jikan.moe/v4/anime/"

# complete_url variable to store
# complete url address


# get method of requests module
# return response object
response = requests.get(url, params= {"sfw" : "true","sort":"desc", "order_by": "score", "min_score" : "5"})

# json method of response object
# convert json format data into
# python format data
dataAsJson = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if dataAsJson["data"]:

    # store the value of "main"
    # key in variable y
    loadedAnime = dataAsJson["data"]
    animeList = []
    for anime in loadedAnime:

        animeObject = Anime(anime["title"], anime["url"])
        print("This is anime: " + animeObject.__str__())
        animeList.append(animeObject)
    # store the value corresponding
    # to the "temp" key of y


else:
    print(" Api not working ")

    print(" Jinej kok branch ")

