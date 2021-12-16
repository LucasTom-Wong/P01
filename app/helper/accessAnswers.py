# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newAnswer(question):
    url = "https://api.m3o.com/v1/answer/Question"
    answerUrl = urllib.request.urlopen(url)
    answer = json.loads(answerUrl.read())
    return answer

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    x = newAnswer("What is the meaning of life?")
    return x

if __name__ == "__main__":
    main()
