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
	if  previousScore != None and newScore > previousScore:
		updateFileScore(userName, newScore)
	elif previousScore == None:
		u = open('userScores.txt', 'a')
		size = os.stat('userScores.txt').st_size
		newScoreLine = "\n%s %d\n" %(userName, newScore) if size > 0  else "%s %d\n" %(userName, newScore) 
		print(newScoreLine+"a")
		u.write(newScoreLine)
		u.close()			
	elif previousScore == newScore:
		print("%s, Congrats you've achieved your best score" %(userName))
	else:
		print("%s, You've done better before...You have %d points to achieve your best score" %(userName, previousScore - newScore))
	return

def updateFileScore(userName, newScore):
	print("%s, Congrats you've achieved your best score" %(userName))
	u = open('userScores.txt', 'r');
	newFile = ""
	lineNr = 0
	userLineNr = -1
	for line in u:
		lineNr += 1
		lineStrings = line.split()
		if lineStrings[0] == userName:
			userLineNr = lineNr
			newFile += "%s %d" %(lineStrings[0], newScore)
		else:
			newFile += line
	if userLineNr == -1:
		newFile += "%s %d" %(userName, newScore)
	if userLineNr != lineNr:
		newFile += "\n"
	u.close()
	u = open('userScores.txt', 'w')
	u.write(newFile)
	u.close()

def getHighScores():
	try:
		u = open('userScores.txt', 'r')
	except IOError:
		print("No scores yet...")
		u = open('userScores.txt', 'w')
	scores = {}
	for line in u:
		splits = line.split(" ")
		scores[splits[0]] = splits[1]
	u.close()	
	sortedScores = sorted(scores.items(), key=operator.itemgetter(1))
	print("_____________________")
	print("No.  UserName Score     ")
	print("_____________________")
	for index, i in enumerate(sortedScores):
		print("%3d%9s%8d" %(index + 1, i[0], int(i[1])))
		
	

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
	print("Question: %s" %(expression.replace("**", "^")))
	if score == None:
		score = int(0)
	while True:
		try:
			answer = int(input("Answer:"))
			if correctAnswer(expression, answer):
				score += 10
				print("You got 10 points for the Question.\nYou now have %d points\n\n" %(score))
			else:
				score = score - 5 if score > 5 else 0
				print("Your score has been decreased by 5 points.\nYou now have %d points\n\n" %(score))
			break
		except TypeError:
			print("Please enter a number")
	return score