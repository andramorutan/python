import random
import operator
import os

def getUserScore(userName):
	result = None
	try:
		u = open('userScores.txt', 'r')
		for line in u:
			lineStrings = line.split()
			if 	lineStrings[0] == userName:
				result = int(lineStrings[1])
				break
	except IOError:
		u = open('userScores.txt', 'w')
	
			
	u.close();
	return result

def updateUserScore(userName, newScore):
	previousScore = getUserScore(userName)
	if  previousScore is not None and newScore > previousScore:
		updateFileScore(userName, newScore)
	elif previousScore is None:
		u = open('userScores.txt', 'a')
		size = os.stat('userScores.txt').st_size
		newScoreLine = "\n{} {}\n".format(userName, newScore) if size > 0 else "{} {}\n".format( userName, newScore) 
		print(newScoreLine+"a")
		u.write(newScoreLine)
		u.close()			
	elif previousScore == newScore:
		print("{}, Congrats you've achieved your best score".format({}))
	else:
		print("{userName}, You've done better before...You have {score} points to achieve your best score".format(userName = userName, score = previousScore - newScore))
	return

def updateFileScore(userName, newScore):
	print("{}, Congrats you've achieved your best score".format(userName))
	u = open('userScores.txt', 'r');
	newFile = ""
	lineNr = 0
	userLineNr = -1
	for line in u:
		lineNr += 1
		lineStrings = line.split()
		if lineStrings[0] == userName:
			userLineNr = lineNr
			newFile += "{} {}".format(lineStrings[0], newScore)
		else:
			newFile += line
	if userLineNr == -1:
		newFile += "{} {}".format(userName, newScore)
	if userLineNr != lineNr:
		newFile += "\n"
	u.close()
	u = open('userScores.txt', 'w')
	u.write(newFile)
	u.close()

def getHighScores():
	try:
		u = open('userScores.txt', 'r')
		scores = {}
		for line in u:
			splits = line.split(" ")
			scores[splits[0]] = splits[1]
		
		sortedScores = sorted(scores.items(), key=operator.itemgetter(1))
		print("_____________________")
		print("No.  UserName Score     ")
		print("_____________________")
		for index, i in enumerate(sortedScores):
			print("%3d%9s%8d" %(index + 1, i[0], int(i[1])))
	except IOError:
		print("No scores yet...")
		u = open('userScores.txt', 'w')
	u.close()
		
	

def generateExpression():
	expression = ''
	operatorsTuple = ("+", "-", "*", "**")
	operandsNumber = random.randint(2,5)
	for i in range(operandsNumber - 1 ):
		operand = random.randint(1,10)
		operator = operatorsTuple[random.randint(0,3)]
		expression += str(operand) + " " + operator + " "
	operator = random.randint(1, 10)
	expression += str(operand)
	return expression

def correctAnswer(expression, answer):
	correctAnswer = eval(expression) 
	return correctAnswer == answer

def question(score):
	expression = generateExpression()
	print("Question: {}".format(expression.replace("**", "^")))
	if score is None:
		score = int(0)
	while True:
		try:
			answer = int(input("Answer:"))
			if correctAnswer(expression, answer):
				score += 10
				print("You got 10 points for the Question.\nYou now have {} points\n\n".format(score))
			else:
				score = score - 5 if score > 5 else 0
				print("Your score has been decreased by 5 points.\nYou now have {} points\n\n".format(score))
			break
		except TypeError:
			print("Please enter a number")
	return score