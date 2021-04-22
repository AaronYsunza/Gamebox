# guessing game
# rock paper scissors
# dice roll
# fortune teller

import random

def guessingGame():
	print("Try to guess my number correctl")

def RPS():
	print("""
Rock = 1
Paper = 2
Scissors = 3""")
	
	cpuChoice = random.randint(1,3)
	playerChoice = int(input("What's your move: "))

	if(playerChoice == 1):
		if(cpuChoice == 1):
			print("Tie! I chose rock")
		elif(cpuChoice == 2):
			print("You lose! I chose paper")
		elif(cpuChoice == 3):
			print("You win! I chose scissors")
	
	if(playerChoice == 2):
		if(cpuChoice == 1):
			print("You win! I chose rock")
		elif(cpuChoice == 2):
			print("Tie! I chose paper")
		elif(cpuChoice == 3):
			print("You lose! I chose scissors")
	
	if(playerChoice == 3):
		if(cpuChoice == 1):
			print("You lose! I chose rock")
		elif(cpuChoice == 2):
			print("You win! I chose paper")
		elif(cpuChoice == 3):
			print("You Tie! I chose scissors")

def diceRoll():
	dice = random.randint(1, 6)
	print("The dice rolled on... " + str(dice))
def fortuneTeller():
	fortuneList = ["A jolly man will visit you on the 25th of December", "Your next meal is something edible.", "You will hear a big bang outside during the midnight of December 31st...", "You will look oustide your window... and see another house.", "The next time you use the microwave, it will star beeping!", "You will get so used to sleeping, that you can start doing it with your eyes closed."]

	print(fortuneList[random.randint(0,len(fortuneList)-1)])

# 'main' funtion
# this is where we define how we want our program to run

def main():

# Tell the user their game options
# Ask the user to choose one
# Call the correct funtion based on user input

	print("""
This is my Game Box.
There are four games you can choose.
	1. A Guessing Game
	2. Rock Paper Scissors
	3. Dice Roll
	4. Fortune Teller""")

	gameChoice = input("Type the number of the game you want to play: ")

	if(gameChoice == '1'):
		guessingGame()
	elif(gameChoice == '2'):
		RPS()
	elif(gameChoice == '3'):
		diceRoll()
	elif(gameChoice == '4'):
		fortuneTeller()
	else: # catch exceptions
		print("Sorry that was an invalid input")
		main()

# This controls the execution of our code
if __name__ == "__main__":
	main()
