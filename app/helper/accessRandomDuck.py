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
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #opens with firefox
        rDuck = urllib.request.urlopen(req)
        duck = json.loads(rDuck.read())
        return duck
    except urllib.error.URLError as e:
        print(e.reason)
        return {"url" : "error"}

def fDuck(quack):
    return quack['url']

def fullDuck():
    newis = newDuck()
    aa = fDuck(newis)
    return aa

def main():
    # ssl._create_default_https_context = ssl._create_unverified_context
    newis = newDuck()
    aa = fDuck(newis)
    print(aa)


if __name__ == "__main__":
    main()
