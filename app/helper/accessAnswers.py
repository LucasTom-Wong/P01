    # Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newAnswer(question):
    url = "https://api.m3o.com/v1/answer/Question"

    header = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ZGRlNjhhYWQtN2UyOS00ZTY5LWI2OTctZGU0ZmIwNWY2NThh',
    }

    data = {"query" : question}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii') # data should be bytes

    req = urllib.request.Request(url, headers=header, data = data)
    # req.add_header('Content-Type', 'application/json')
    # req.add_header('Authorization', 'Bearer ZGRlNjhhYWQtN2UyOS00ZTY5LWI2OTctZGU0ZmIwNWY2NThh')
    # print(req)

    try: urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
        return 0

    answerUrl = urllib.request.urlopen(req)
    answer = json.loads(answerUrl.read())
    return answer

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    x = newAnswer("What is the meaning of life?")
    print(x)

if __name__ == "__main__":
    main()
