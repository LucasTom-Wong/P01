# Tests the databases
import sys
from os import remove, path
from databases import Databases
import random

def start():
	global d
	d = Databases()

start()

def show_result(success:bool):
	if success:
  		print("Success")
	else:
  		print("Failed")

def test_question_creation(num:int = 100):
	success = False
	print("Testing question creation...")
	try:
		for i in range(num):
			d.add_question(str(i), str(i), str(i))
			success = True
	except Exception as e:
		print(e)
	return show_result(success)

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

def test_return_questions(num:int=100):
	success = False
	print("Testing question return...")
	try:
		for i in range(num):
			print("Question returned: " + str(d.return_question()))
			success = True
	except Exception as e:
		print(e)
	return show_result(success)

print(d.return_leaderboard())

d.print_databases()

test_question_creation(5)
d.add_question("1", "2", "3")

test_leaderboard_update(5)
d.update_leaderboard("EXTRA", 10)
d.update_leaderboard("EXTRA", 10)

test_return_questions(6)

d.print_databases()

print("Leaderboard data in order: " + str(d.return_leaderboard()))

print("All questions used?: " +  str(d.all_questions_used()))
