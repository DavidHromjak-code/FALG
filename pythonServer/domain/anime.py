import json
class Anime:

    def __init__(self, engName, japName, bCastType, eps, airStatus, ageGroup, url, image):
        self.engName = engName
        self.japName = japName
        self.bCastType = bCastType
        self.eps = eps
        self.airStatus = airStatus
        self.ageGroup = ageGroup
        self.url = url
        self.image = image


    def get_eng_name(self):
        return self.engName

    def set_eng_name(self, engName):
        self.engName = engName

    def get_jap_name(self):
        return self.japName

    def set_jap_name(self, japName):
        self.japName = japName

    def get_b_cast_type(self):
        return self.bCastType

    def set_b_cast_type(self, bCastType):
        self.bCastType = bCastType

    def get_eps(self):
        return self.eps

    def set_eps(self, eps):
        self.eps = eps

    def get_air_status(self):
        return self.airStatus

    def set_air_status(self, airStatus):
        self.airStatus = airStatus

    def get_age_group(self):
        return self.ageGroup

    def set_age_group(self, ageGroup):
        self.ageGroup = ageGroup

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def __str__(self):
        return "anglický název: % s, " \
               "japonský název: % s, typ vysílání: % s, status vysílání: % s, počet epizod: % s, věková skupina: % s, odkaz na mal: % s" % (
            self.engName, self.japName, self.bCastType, self.eps, self.airStatus, self.ageGroup, self.url)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Param:
    def __init__(self, sfw,order_by, minScore, sort):
        self.sfw = sfw
        self.order_by = order_by
        self.minScore = minScore
        self.sort = sort
    def __str__(self):
        return "Tohle je to string metoda: sfw je % s, " \
               "min score je  % s" % (self.sfw, self.minScore)

