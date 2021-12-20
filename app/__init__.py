# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl
import helper.accessOpenTrivia
import random
import os
from flask import Flask, render_template, request, session

app = Flask(__name__)    #create Flask object
newis = helper.accessOpenTrivia.newQuestion()

def randomizedQuestions(quest):
    list = helper.accessOpenTrivia.fListPossible(quest)
    blue = []
    for str in list:
        blue.append(str)
    print (blue)
    blue = random.sample(blue, len(blue))
    return blue

@app.route("/trivia")
def disp_triviaPage():
    ssl._create_default_https_context = ssl._create_unverified_context
    global newis
    newis = helper.accessOpenTrivia.newQuestion()
    # print(randomizedQuestions(newis))
    # print(randomizedQuestions(newis)[0])
    return render_template('trivia.html', question = helper.accessOpenTrivia.fQuestion(newis), listAnswers = randomizedQuestions(newis))
@app.route("/")
def disp_homePage():
    return render_template("home.html")
@app.route("/submitAnswer", methods = ['GET', 'POST'])
def disp_submitAnswer():
    answer = request.args['ans']
    print(answer)
    print(helper.accessOpenTrivia.fCorrect(newis))
    if (answer == helper.accessOpenTrivia.fCorrect(newis)):
        return render_template("submitAnswer.html", answer = "CORRECT")
    return render_template("submitAnswer.html", answer = "WRONG")

if __name__ == "__main__":
    app.debug = True
    app.run()
