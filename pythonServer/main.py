import eel
from loadData import load_data

eel.init("web")


@eel.expose
def get_data():
    return load_data()


eel.start("index.html")
