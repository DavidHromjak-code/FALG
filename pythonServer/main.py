import eel

eel.init("web")

@eel.expose
def helloWorld():

  return ["Hello world", "Hello", "BABA", "YAGA"]

eel.start("index.html")
