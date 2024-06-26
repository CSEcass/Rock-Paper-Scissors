# Play command line rock-Paper-Scissors / By me, Cassidy

print('Options(case sensitive): rock, paper, scissors')
P1choice = input('Player 1: ')
P2choice = input('Player 2: ')



if P1choice == "scissors":
    if P2choice == "paper":
        print('--Player 1 wins--')
    elif P2choice == "rock":
        print("--Player 2 wins.--")
    else:
        print("--Tie.--")
if P1choice == "rock":
    if P2choice == "scissors":
        print('--Player 1 wins.--')
    elif P2choice == "paper":
        print("--Player 2 wins.--")
    else:
        print("--Tie.--")
if P1choice == "paper":
    if P2choice == "rock":
        print('--Player 1 wins.--')
    elif P2choice == "scissors":
        print("--Player 2 wins.--")
    else:
        print("--Tie.--")