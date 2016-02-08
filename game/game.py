import mathGameFunctions as m

def game(userName):
	userNameScore = m.getUserScore(userName)
	while True:
		userNameScore = m.question(userNameScore)
		cont = raw_input("Press 0 to exit, any key to continue: ")
		if "0" == cont:
			m.updateFileScore(userName, userNameScore)
			break
	return



userName = raw_input("Please provide your userName ")
while True:
	command = input('''
	1 To start game
	2 See your best score
	3 See high scores
	4 Quit\n''')

	if command == 1:
		game(userName)
	elif command == 2:
		score = m.getUserScore(userName)
		if score == None:
			print("You have not played yet")
		else:
			print("Your best score :%d" %(score))
	elif command == 3:
		m.getHighScores()
	elif command == 4:
		print("See you soon")
		exit()
	else:
		print("Please provide a correct menu key")