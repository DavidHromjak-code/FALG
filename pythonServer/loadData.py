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

paramObject = Param(sfw, order_by, minScore, sort)

print("This is param object: " + paramObject.__str__())

response = requests.get(url, params={"sfw": paramObject.sfw, "sort": paramObject.sort, "order_by": paramObject.order_by, "min_score": paramObject.minScore})

# json method of response object
# convert json format data into
# python format data
dataAsJson = response.json()


# Check the value of "data" key is set
if dataAsJson["data"]:

  # store the value of "data"
  loaded_anime = dataAsJson["data"]
  animeList = []
  for anime in loaded_anime:
    # one way to set data on object
    animeObject = Anime(anime["title"], anime["title_japanese"], anime["type"],
                        anime["status"], anime["episodes"], anime["rating"], anime["url"])

    # second way to set data on object
    animeObject.set_eng_name(anime["title"])
    print("Anglický název: " + animeObject.get_eng_name())

    animeObject.set_jap_name(anime["title_japanese"])
    print("Japonský název: " + animeObject.get_jap_name())

    animeObject.set_b_cast_type(anime["type"])
    print("Typ vysílání: " + animeObject.get_b_cast_type())

    animeObject.set_air_status(anime["status"])
    print("Status vysílání: " + animeObject.get_air_status())

    animeObject.set_eps(anime["episodes"])
    print("Počet epizod: " + str(animeObject.get_eps()))

    animeObject.set_age_group(anime["rating"])
    print("Věková skupina: " + animeObject.get_age_group())

    animeObject.set_url(anime["url"])
    print("url: " + animeObject.get_url())

    # print("This is anime: " + animeObject.__str__())
    animeList.append(animeObject)


else:
  print(" Api not working ")
