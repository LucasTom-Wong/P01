# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newMeme():
    url = "https://meme-api.herokuapp.com/gimme"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #opens with firefox
        meme = urllib.request.urlopen(req)
        meme = json.loads(meme.read())
        return meme
    except urllib.error.URLError as e:
        print(e.reason)
        return 0

def grabImage0(meme): #smol
    meme = meme['preview']
    meme = meme[0]
    return meme

def grabImage3(meme): #chunky
    meme = meme['preview']
    meme = meme[3]
    return meme

def main():
    # ssl._create_default_https_context = ssl._create_unverified_context
    x = newMeme()
    print(x)
    y = grabImage3(x)
    print(y)
    z = grabImage0(x)
    print(z)

if __name__ == "__main__":
    main()
