# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newAnswer(question):
    url = "https://api.m3o.com/v1/answer/Question"

    key = str(open("../keys/key_Answers.txt", "r").read())
    key = key.split("\n")
    key = key[0]
    print(key)
    # print("awaw")

    header = {
        # 'User-Agent': 'Mozilla/5.0',
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' +  key
    }

    data = {"query" : question}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii') # data should be bytes

    try:
        req = urllib.request.Request(url, headers=header, data = data)
        answerUrl = urllib.request.urlopen(req)
        answer = json.loads(answerUrl.read())
        return answer

    except urllib.error.URLError as e:
        print(e.reason)
        return 0

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    x = newAnswer("What is the meaning of life?")
    print(x)

if __name__ == "__main__":
    main()
