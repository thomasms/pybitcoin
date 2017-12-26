import requests


def getresponse(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def getdata(url):
    data = getresponse(url)
    return data
