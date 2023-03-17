# import required modules
import requests
from domain.anime import Anime
from domain.anime import Param

# base_url variable to store url
url = "https://api.jikan.moe/v4/anime/"

# complete_url variable to store
# complete url address


# get method of requests module
# return response object

sfw = input("Want only sfw results true/false?")

order_by = input('Order by "mal_id" "title" "type" "rating" "start_date" "end_date" "episodes" "score" "scored_by" "rank" "popularity" "members" "favorites" ?')

minScore = None
if order_by == "score":
    minScore = input("Select minimal score for anime form 1 - 9:")

sort = input("sort asc or desc?")

paramObject = Param(sfw,order_by,minScore,sort)

print("This is param object: " + paramObject.__str__())

response = requests.get(url, params= {"sfw" : paramObject.sfw,"sort": paramObject.sort, "order_by": paramObject.order_by, "min_score" : paramObject.minScore})

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

