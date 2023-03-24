class Anime:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return "Tohle je to string metoda: jméno je  is % s, " \
               "b is % s" % (self.name, self.url)
         
class Param:
    def __init__(self, sfw,order_by, minScore, sort):
        self.sfw = sfw 
        self.order_by = order_by
        self.minScore = minScore
        self.sort = sort
    def __str__(self):
        return "Tohle je to string metoda: sfw je % s, " \
               "min score je  % s" % (self.sfw, self.minScore)
    
