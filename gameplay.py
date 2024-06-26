# Play command line rock-Paper-Scissors / By me, Cassidy

win1 = int(0)
win2 = int(0)

print('Options(case sensitive): rock, paper, scissors')
P1choice = input('Player 1: ')
P2choice = input('Player 2: ')

if P1choice == "scissors":
    if P2choice == "paper":
        print('--Player 1 wins round 1--')
        win1 += 1
    elif P2choice == "rock":
        print("--Player 2 wins round 1.--")
        win2 += 1
    else:
        print("--Tie.--")
if P1choice == "rock":
    if P2choice == "scissors":
        print('--Player 1 wins round 1.--')
        win1 += 1
    elif P2choice == "paper":
        print("--Player 2 wins round 1.--")
        win2 += 1
    else:
        print("--Tie.--")
if P1choice == "paper":
    if P2choice == "rock":
        print('--Player 1 wins round 1.--')
        win1 += 1
    elif P2choice == "scissors":
        print("--Player 2 wins round 1.--")
        win2 += 1
    else:
        print("--Tie.--")
# ROUND 2 vvv
print('Options(case sensitive): rock, paper, scissors')
P1choice = input('Player 1: ')
P2choice = input('Player 2: ')

if P1choice == "scissors":
    if P2choice == "paper":
        print('--Player 1 wins round 2--')
        win1 += 1
        if win1 == 2:
            print('--Player 1 wins best of 3.--')
    elif P2choice == "rock":
        print("--Player 2 wins round 2.--")
        win2 += 1
        if win2 == 2:
            print('--Player 2 wins best of 3.--')
    else:
        print("--Tie.--")
if P1choice == "rock":
    if P2choice == "scissors":
        print('--Player 1 wins round 2.--')
        win1 += 1
        if win1 == 2:
            print('--Player 1 wins best of 3.--')
    elif P2choice == "paper":
        print("--Player 2 wins round 2.--")
        win2 += 1
        if win2 == 2:
            print('--Player 2 wins best of 3.--')
    else:
        print("--Tie.--")
if P1choice == "paper":
    if P2choice == "rock":
        print('--Player 1 wins round 2.--')
        win1 += 1
        if win1 == 2:
            print('--Player 1 wins best of 3.--')
    elif P2choice == "scissors":
        print("--Player 2 wins round 2.--")
        win2 += 1
        if win2 == 2:
            print('--Player 2 wins best of 3.--')
    else:
        print("--Tie.--")
# ROUND 3 vvv
print('Options(case sensitive): rock, paper, scissors')
P1choice = input('Player 1: ')
P2choice = input('Player 2: ')

if P1choice == "scissors":
    if P2choice == "paper":
        print('--Player 1 wins round 2--')
        win1 += 1
        if win1 == 2:
            print('--Player 1 wins best of 3.--')
    elif P2choice == "rock":
        print("--Player 2 wins round 2.--")
        win2 += 1
        if win2 == 2:
            print('--Player 2 wins best of 3.--')
    else:
        print("--Tie.--")
if P1choice == "rock":
    if P2choice == "scissors":
        print('--Player 1 wins round 2.--')
        win1 += 1
        if win1 == 2:
            print('--Player 1 wins best of 3.--')
    elif P2choice == "paper":
        print("--Player 2 wins round 2.--")
        win2 += 1
        if win2 == 2:
            print('--Player 2 wins best of 3.--')
    else:
        print("--Tie.--")
if P1choice == "paper":
    if P2choice == "rock":
        print('--Player 1 wins round 2.--')
        win1 += 1
        if win1 == 2:
            print('--Player 1 wins best of 3.--')
    elif P2choice == "scissors":
        print("--Player 2 wins round 2.--")
        win2 += 1
        if win2 == 2:
            print('--Player 2 wins best of 3.--')
    else:
        print("--Tie.--")
        if win1 > win2:
            print('--Player 1 wins best of 3.--')
        if win2 > win1:
            print('--Player 2 wins best of 3.--')