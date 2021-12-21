    # Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newAnswer(question):
    url = "https://api.m3o.com/v1/answer/Question"
    values = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer OTEzNzY2ZDYtMmI2OC00MDE5LWIwMTktNzVhMjg2OGUyOTNk',
    }
    data = {"query" : "microsoft"}

    header = urllib.parse.urlencode(values)
    header = header.encode('ascii') # data should be bytes

    req = urllib.request.Request(url, header, data)
    try: urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)

    # answerUrl = urllib.request.urlopen(req)
    # answer = json.loads(answerUrl.read())

    return 0

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    x = newAnswer("What is the meaning of life?")

if __name__ == "__main__":
    main()
