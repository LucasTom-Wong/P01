# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newQuestion():
    url = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple"
    openTrivia = urllib.request.urlopen(url)
    question = json.loads(openTrivia.read())
    question = question['results']
    return question[0]

def fQuestion(quest):
    return "" + quest['question']

def fCorrect(quest):
    return "" + quest['correct_answer']

def fIncorrect(quest):
    listIncorrect = []
    incorrect = quest['incorrect_answers']
    for str in incorrect:
        listIncorrect.append(str)
    # print (listIncorrect)
    return listIncorrect

def fListPossible(quest):
    # print(fIncorrect(quest).append(fCorrect(quest)))
    super_List = fIncorrect(quest)
    super_List.append(fCorrect(quest))
    return super_List

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    newres = newQuestion()
    print(fQuestion(newres))
    print(fCorrect(newres))
    print(fIncorrect(newres))
    print(fListPossible(newres))

if __name__ == "__main__":
    main()
