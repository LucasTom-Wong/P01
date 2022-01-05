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
        return {"postLink":"https://redd.it/rw34t0","subreddit":"me_irl","title":"me_irl","url":"https://i.redd.it/hn9007gt7q981.jpg","nsfw":false,"spoiler":false,"author":"Ledorak","ups":45,"preview":["https://preview.redd.it/hn9007gt7q981.jpg?width=108\u0026crop=smart\u0026auto=webp\u0026s=d7ce4d0c7ecdcee5693172a4a86b36b510d7a173","https://preview.redd.it/hn9007gt7q981.jpg?width=216\u0026crop=smart\u0026auto=webp\u0026s=67648323239efadf3adcaaa51b8e5cb6b20c3c22","https://preview.redd.it/hn9007gt7q981.jpg?width=320\u0026crop=smart\u0026auto=webp\u0026s=f25c5a253fc4979fb8ad6c599d29aef12d74a7e4","https://preview.redd.it/hn9007gt7q981.jpg?width=640\u0026crop=smart\u0026auto=webp\u0026s=1e4504797dc34a971ce00f635248b845a2cc11b9"]}

def grabImage0(meme): #smol
    meme = meme['preview']
    meme = meme[0]
    return meme

def grabImage3(meme): #chunky
    meme = meme['preview']
    meme = meme[2]
    return meme

def fullMeme():
    x = newMeme()
    return grabImage3(x)

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
