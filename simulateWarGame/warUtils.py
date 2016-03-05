import random

def generateCard(numberOfDecks, usedCards):
	while True:
		numberCard = random.randint(0,12)
		color = random.randint(0,3)
		if usedCards[color][numberCard] < numberOfDecks:
			usedCards[color][numberCard] += 1
			#print("Generated Card: {} , {}, {}".format(color, numberCard, usedCards[color][numberCard]))
			break
	return (color, numberCard)

def isMatch(card0, card1, matchStrategy):
	result = False
	if matchStrategy == 0:
		if card0[0] == card1[0]:
			result = True 
	elif matchStrategy == 1:
		if card0[1] == card1[1]:
			result = True
	elif matchStrategy == 2:
		if card0[1] == card1[1] and card0[0] == card1[0]:
			result = True
	return result 