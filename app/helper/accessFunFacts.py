# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newFact():
    url = "https://asli-fun-fact-api.herokuapp.com/"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #opens with firefox
        funFact = urllib.request.urlopen(req)
        fact = json.loads(funFact.read())
        return fact
    except:
        return "no fun fact :("

def fFact(fffact):
    return fffact['fact']

def main():
    # ssl._create_default_https_context = ssl._create_unverified_context
    newis = newFact()
    # print(newis)
    newres = newis['data']
    print(fFact(newres))


if __name__ == "__main__":
    main()
