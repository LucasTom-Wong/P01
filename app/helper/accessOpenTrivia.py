# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl

def newQuestion(): #returns the new question from the api
    url = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple"

    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) #opens with firefox
        quest = urllib.request.urlopen(req)
        question = json.loads(quest.read())
        question = question['results']
        return question[0]
    except urllib.error.URLError as e:
        print(e.reason)
        return "ahhhhhhhhhhh" #need to fix later with a better error

def fQuestion(quest): #returns the question
    return "" + quest['question']

def fCorrect(quest): #returns correct answer
    return "" + quest['correct_answer']

def fIncorrect(quest): #returns a list of incorrect answers
    listIncorrect = []
    incorrect = quest['incorrect_answers']
    for str in incorrect:
        listIncorrect.append(str)
    # print (listIncorrect)
    return listIncorrect

def fListPossible(quest): #returns a list of the incorrect answre
    # print(fIncorrect(quest).append(fCorrect(quest)))
    super_List = fIncorrect(quest)
    super_List.append(fCorrect(quest))
    return super_List

def fAnswers_to_String(answers):
    str = ""
    for x in answers:
        str += x + "&*&^!#"
    return str

def fString_to_Answers(str):
    quest = str.split("&*&^!#")
    return quest

def main():
    # ssl._create_default_https_context = ssl._create_unverified_context
    newres = newQuestion()

    print(fQuestion(newres))
    print(fCorrect(newres))
    print(fIncorrect(newres))
    answerList = fListPossible(newres)
    print(answerList)
    answerString = fAnswers_to_String(answerList)
    print(answerString)
    print(fString_to_Answers(answerString))

if __name__ == "__main__":
    main()
