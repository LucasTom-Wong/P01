# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import json
import urllib.request
import urllib
import ssl
import helper.accessOpenTrivia
from flask import Flask, render_template, request, session
app = Flask(__name__)    #create Flask object
def temp():
    question1 = newQuestion()
    question1 = question1['results']
    question1 = question1[0]

@app.route("/")
def disp_triviaPage():
    ssl._create_default_https_context = ssl._create_unverified_context
    newis = helper.accessOpenTrivia.newQuestion()
    newiss = newis['results']
    newiss = newiss[0]
    return render_template('trivia.html', question = helper.accessOpenTrivia.fQuestion(newiss))

if __name__ == "__main__":
    app.debug = True
    app.run()
