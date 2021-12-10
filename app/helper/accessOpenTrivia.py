# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib

def newQuestion():
    url = "https://opentdb.com/api.php?amount=1"
    openTrivia = urllib.request.urlopen(url)
    question = json.loads(openTrivia.read())
    return question

def translateQuestion():


def main():
    print(newQuestion())

if __name__ == "__main__":
    main()
