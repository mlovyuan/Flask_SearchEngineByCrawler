import requests

def get_google_info(word):
    url = "https://www.google.com/search?q={}".format(word)
    res = requests.get(url).text
    return res