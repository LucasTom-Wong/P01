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
import random
from os import path, remove
from data.databases import Databases
from flask import Flask, render_template, request, session
# import data.test

app = Flask(__name__)    #create Flask object
newis = helper.accessOpenTrivia.newQuestion()
# ssl._create_default_https_context = ssl._create_unverified_context

def randomizedQuestions(quest):
    list = helper.accessOpenTrivia.fListPossible(quest)
    blue = []
    for str in list:
        blue.append(str)
    print (blue)
    blue = random.sample(blue, len(blue))
    return blue

def purge():
	global d
	global db_file
	db_file = "perm.db"
	if path.exists(db_file):
		remove(db_file) #makes sure none of previous test is there
		d = Databases()
	else:
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

@app.route("/")
def disp_homePage():
    duckimage = helper.accessRandomDuck.fullDuck()
    return render_template("home.html", url = duckimage)

@app.route("/leaderboard")
def display_Leaderboard():

    print("start test!!")
    purge()
    print("purged")

    # test_question_creation(5)
    # d.add_question("1", "2", "3")

    test_leaderboard_update(5)
    d.update_leaderboard("EXTRA", 3)

    # test_return_questions(6)

    d.print_databases()

    debug = str(d.return_leaderboard())

    # print("Leaderboard data in order: " + str(d.return_leaderboard()))
    leaders = {
        'Bob': 1,
        'Jason': 2,
        'Derrick': 3
    }

    return render_template("leaderboard.html", leaders = leaders, debug = debug)

@app.route("/trivia")
def disp_triviaPage():
    # ssl._create_default_https_context = ssl._create_unverified_context
    global newis
    newis = helper.accessOpenTrivia.newQuestion()
    # print(randomizedQuestions(newis))
    # print(randomizedQuestions(newis)[0])
    return render_template('trivia.html', question = helper.accessOpenTrivia.fQuestion(newis), listAnswers = randomizedQuestions(newis))

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
