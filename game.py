from random import randint

choices=["rock", "paper", "scissors"]

computer=choices[randint(0,2)]

player = False

while player is False:

	player = input("Choose rock, paper, scissors!\n")

	print("Computer: ", computer, "player: ", player)

	if player == "exit":
		print("You Choose to quit....")
		exit()
	else:

		
		#
		#start doing some logic and condition checking
		#always check breaking condition first


		if player == computer:
			#we have a tie, no point in going any further
			print(computer, player, "\nIt's a Tie...can you tie a tie?....Sorry\n")
		else:

			if player == "rock" and computer == "paper":
				print(player, computer, "\nPaper beats Rock!!\n AI wins!\n")

			if player == "paper" and computer == "rock":
				print(player, computer, "\nPaper beats Rock!! Player Wins!\n")

			if player == "scissors" and computer == "paper":
				print(player, computer, "\nScissors beats Paper!! Player Wins!\n")

			if player == "scissors" and computer == "paper":
				print(player, computer, "\nScissors beats Paper!! Player Wins!\n")