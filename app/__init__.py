# Shoebuckle: Lucas (LTW) Tom-Wong, Julia (Lia) Nelson, Shriya Anand
# SoftDev
# P01 ArRESTed Development: Trivia

import sqlite3
import json
import urllib.request
import urllib
import ssl
import helper.accessOpenTrivia
import helper.accessRandomDuck
import helper.accessFunFacts
import random
from os import path, remove
from data.databases import Databases
from flask import Flask, render_template, request, session
import helper.accessMeme

app = Flask(__name__)    #create Flask object
newis = helper.accessOpenTrivia.newQuestion()
# ssl._create_default_https_context = ssl._create_unverified_context

db_file = "databases.db"
d = Databases()
score = 0

def randomizedQuestions(quest):
    list = helper.accessOpenTrivia.fListPossible(quest)
    blue = []
    for str in list:
        blue.append(str)
    print (blue)
    blue = random.sample(blue, len(blue))
    return blue

def purge():
    if path.exists(db_file):
        remove(db_file) #makes sure none of previous test is there
        d = Databases()
    d = Databases()

def test_leaderboard_update(num:int=100):
	success = False
	print("Testing leaderboard update...")
	try:
		for i in range(num):
			d.update_leaderboard(str(i), i % 10)
			success = True
	except Exception as e:
		print(e)
	return show_result(success)

def show_result(success:bool):
	if success:
  		print("Success")
	else:
  		print("Failed")

def convertToFormLeaderboard(database_leaderboard):
    tempString = ""

    for names in database_leaderboard:
        tempString += names
        # converting to string because...

    tempString = tempString.strip()

    new_string = tempString.replace('[', ',').replace(']', ',').replace('(', ',').replace(')', ',')
    new_string = new_string.replace(',,', ',')
    new_string = new_string.replace(" ", "")
    new_string = new_string[1:-1]
    new_string = new_string.replace(',,', ',')
    print(new_string)
    values = new_string.split(',')
    print(values)

    formAA = {}

    try:
        formAA.update({values[1]: values[2]})
    except:
        formAA.update({"empty": 0})
    try:
        formAA.update({values[4]: values[5]})
    except:
        formAA.update({"empty": 0})
    try:
        formAA.update({values[7]: values[8]})
    except:
        formAA.update({"empty": 0})
    try:
        formAA.update({values[10]: values[11]})
    except:
        formAA.update({"empty": 0})
    try:
        formAA.update({values[13]: values[14]})
    except:
        formAA.update({"empty": 0})
    print(formAA)
    # print(tempString)
    return formAA

@app.route("/")
def disp_homePage():
    duckimage = helper.accessRandomDuck.fullDuck()
    return render_template("home.html", url = duckimage)

@app.route("/leaderboard")
def display_Leaderboard():
    global d
    d = Databases()
    global db_file
    db_file = "databases.db"
    # print("start test!!")
    # purge()
    # print("purged")

    # test_leaderboard_update(5)
    # d.update_leaderboard("EXTRA", 3)

    d.print_databases()

    debug = str(d.return_leaderboard())
    # print("wy")
    # print(debug)
    # print("hi")

    x = convertToFormLeaderboard(debug)
    print(x)

    # print("Leaderboard data in order: " + str(d.return_leaderboard()))
    # leaders = {
    #     'Bob': 1,
    #     'Jason': 2,
    #     'Derrick': 3
    # }

    return render_template("leaderboard.html", leaders = x)

@app.route("/between")
def disp_Between():
    global score
    score = 0
    fact = helper.accessFunFacts.fullFact()
    # print(fact)
    return render_template('inBetween.html', fact = fact)

@app.route("/trivia")
def disp_triviaPage():
    # ssl._create_default_https_context = ssl._create_unverified_context
    global newis
    newis = helper.accessOpenTrivia.newQuestion()
    # print(randomizedQuestions(newis))
    # print(randomizedQuestions(newis)[0])

    newmeme = helper.accessMeme.fullMeme()

    return render_template('trivia.html', question = helper.accessOpenTrivia.fQuestion(newis), listAnswers = randomizedQuestions(newis), url = newmeme)

@app.route("/submitAnswer", methods = ['GET', 'POST'])
def disp_submitAnswer():
    global score
    answer = request.args['ans']
    print(answer)
    print(helper.accessOpenTrivia.fCorrect(newis))
    if (answer == helper.accessOpenTrivia.fCorrect(newis)):
        score += 1
        return render_template("rightAnswer.html", score = score)
    return render_template("wrongAnswer.html", score = score)

@app.route("/end", methods = ['GET', 'POST'])
def disp_endPage():
    return render_template("end.html")


if __name__ == "__main__":
    app.debug = True

    # global d
    # d = Databases()
    # global db_file
    # db_file = "perm.db"

    app.run()
