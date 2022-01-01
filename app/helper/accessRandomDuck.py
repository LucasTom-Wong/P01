# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newDuck():
    url = "https://random-d.uk/api/v1/random"
    try:
        rDuck = urllib.request.urlopen(url)
        duck = json.loads(rDuck.read())
        return duck
    except:
        return {"url" : "https://random-d.uk/api/115.jpg"}

def fDuck(quack):
    return quack['url']

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    newis = newDuck()
    aa = fDuck(newis)
    print(aa)


if __name__ == "__main__":
    main()
