class Anime:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __str__(self):
        return "Tohle je to string metoda: jméno je  is % s, " \
               "b is % s" % (self.name, self.url)

