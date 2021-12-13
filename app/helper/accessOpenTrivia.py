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


def fQuestion(quest):
    return quest['question']

def fCorrect(quest):
    return quest['correct_answer']

def fIncorrect(quest):
    listIncorrect = ""
    incorrect = quest['incorrect_answers']

    return listIncorrect

# def toDict(string):
#     return json.loads("'" + string + "'")

def main():
    newis = newQuestion()
    newiss = newis['results']
    # print(newiss)
    newres = newiss[0]
    print(newres)
    # print("\n")
    print(fQuestion(newres))
    print(fCorrect(newres))
    print(fIncorrect(newres))

if __name__ == "__main__":
    main()
