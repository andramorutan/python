import warUtils as wu
import generalUtils as gu
import random
from collections import Counter
#TODO create a class for the game
noOfPlayers = None
numberOfDecks = None
matchStrategy = None
playersTotalCards = None
usedCards = [[0 for x in range(13)] for x in range(4)]

#def initGame(noOfPlayers, numberOfDecks, matchStrategy, playersTotalCards):
noOfPlayers = gu.readPositiveInt("Players")
numberOfDecks = gu.readPositiveInt("Decks")
matchStrategy = gu.readPositiveInteger("Strategy", 0 , 2)
playersTotalCards = [0 for x in range(noOfPlayers)]

#TODO: move this to warUtils.
def playGame():
	generatedCard0 = wu.generateCard(numberOfDecks, usedCards)
	cardIndex = 1
	currentCards = 1
	while  cardIndex < 52 * numberOfDecks:
		generatedCard1 = wu.generateCard(numberOfDecks, usedCards)
		cardIndex += 1
		currentCards += 1
		war = wu.isMatch(generatedCard0, generatedCard1, matchStrategy)
		if war:
			print ("We have a war")
			winner = random.randint(0, noOfPlayers - 1)
			playersTotalCards[winner] += currentCards
			print("Player {player} got extra {cards} cards. The player {player} now has {total}"
				.format(player = winner, cards = currentCards, total =playersTotalCards[winner] + 1))
			currentCards = 0
	maximCardsNumber = max(playersTotalCards)
	numberOfWinners = Counter(playersTotalCards)[maximCardsNumber]
	if numberOfWinners > 1:
		print "Draw. There are {} players with {} cards".format(numberOfWinners, maximCardsNumber)
	else: 
		print "The winner is player {} with {} cards".format(playersTotalCards.index(maximCardsNumber) + 1, maximCardsNumber)


#initGame(noOfPlayers, numberOfDecks, matchStrategy, playersTotalCards)
playGame()