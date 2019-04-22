import random
playagain = "y"
comCount = 0
playerCount = 0
while playagain == "y":
	#for computer choice, 1 is rock. 2 is paper, 3 is scissors
	comChoice = random.randint(1,3)
	print("make a move! (r/s/p)")

	playerChoice = input()

	if playerChoice == "sc":
		print("human: {}, computer: {}".format(playerCount,comCount))
	elif playerChoice == "r" and comChoice == 1:
		print("You chose rock and the computer chose rock, tie!")
	elif playerChoice == "r" and comChoice == 3:
		print("You chose rock and the computer chose scissors, you win!")
		playerCount = playerCount + 1
	elif playerChoice == "r" and comChoice == 2:
		print("You chose rock and the computer chose paper, you lose!")
		comCount = comCount + 1
	elif playerChoice == "s" and comChoice == 1:
		print("You chose scissors and the computer chose rock, you lose!")
		comCount = comCount + 1
	elif playerChoice == "s" and comChoice == 3:
		print("You chose scissors and the computer chose scissors, tie!")
	elif playerChoice == "s" and comChoice == 2:
		print("You chose scissors and the computer chose paper, you win!")
		playerCount = playerCount + 1
	elif playerChoice == "p" and comChoice == 1:
		print("You chose paper and the computer chose rock, you win!")
		playerCount = playerCount + 1
	elif playerChoice == "p" and comChoice == 3:
		print("You chose paper and the computer chose scissors, you lose!")
		comCount = comCount + 1
	elif playerChoice == "p" and comChoice == 2:
		print("You chose paper and the computer chose paper, tie!")


	print("Do you want to play again? (Y/N)?")
	playagain= input()