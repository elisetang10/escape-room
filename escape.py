def start_game():
    print("welcome to the hardest escape room ever!")
    print("you need to choose between the metal door or the wooden door.")
    choice = input("press 1 for metal, 2 for wooden.")
    if choice == "1":
        metal()
    elif choice == "2":
        wooden()
    else: 
        print("choose number 1 or 2")
        start_game()
def win():
    print("great job! you did it!")
    print("here's your medal!")
    winner = open("w.txt","r")
    print(winner.read())
    winner.close()
    play_again()
def metal():
    print("answer this riddle:")
    print("I have branches but no trunk, leaves, roots or fruit. What am I?")
    enter = input(">")
    if enter.lower() == "bank":
        print("you got it right!")
        print("choose 1 to enter the water room or 2 to enter the fire room.")
        choice = input("type 1 or 2")
        if choice == "1":
            print("you drowned! you failed the mission!")
            play_again()
        elif choice == "2":
            print("you got burnt but you managed to escape. well done :)")
            win()
    else:
        print("wrong answer. try again!")
        start_game()
    
def wooden():
    print("What can't talk but will reply when spoken to?")
    choice = input("enter you answer: ")
    if choice.lower() == "echo":
        print("correct! answer the next riddle to leave.")
        print("What has many keys but cannot open a single lock?")
        choice2 = input(">")
        if choice2.lower() == "piano":
            print("you did it!")
            win()
        else:
            print("wrong answer, try again")
    else:
        print("please try again.")
start_game()
def play_again():
    print("do you want to play again? y/n?")
    answer = input(">").lower()
    if answer == "y":
        start_game()
    elif answer == "n":
        print("thanks for playing :)")
        exit()
    else:
        print("incorrect input: type y/n")