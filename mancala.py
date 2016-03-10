#mancala

side1 = [0,4,4,4,4,4,4] #Side 1's stones. side1[0] is P2's mancala
side2 = [0,4,4,4,4,4,4] #Side 2's stones. side2[0] is P1's mancala
player = True #player is a boolean variable, "true" being player 1 and "false" being player 2

def refreshBoard(): #Updates the board on-screen with a running total of stones in all pots
    print(" _________________________________________________")
    print("|  ___   ___   ___   ___   ___   ___   ___   ___  |")
    print("| |   | |   | |   | |   | |   | |   | |   | |   | |")
    print("| |   | |",side2[1],"| |",side2[2],"| |",side2[3],"| |",side2[4],"| |",side2[5],"| |",side2[6],"| |   | |")
    print("| |   | |___| |___| |___| |___| |___| |___| |   | |")
    print("| |   |   1     2     3     4     5     6   |   | |")
    print("| |",side2[0],"|                                     |",side1[0],"| |")
    print("| |   |  _6_   _5_   _4_   _3_   _2_   _1_  |   | |")
    print("| |   | |   | |   | |   | |   | |   | |   | |   | |")
    print("| |   | |",side2[6],"| |",side2[5],"| |",side1[4],"| |",side1[3],"| |",side1[2],"| |",side1[1],"| |   | |")
    print("| |___| |___| |___| |___| |___| |___| |___| |___| |")
    print("|_________________________________________________|")
#end refreshBoard

def canBeInt(s): #Checks if a string can be an integer. 
    try: 
        int(s)
        return True
    except ValueError:
        return False

def makeTurn(): #This will prompt a player to choose a pot. 
    print("Which pot do you choose? Enter the number of your pot.")
    if player = True: #Checks who is playing, and tells them which pot to choose from.
        chosenPot = input("You're player 1, so choose from the bottom six.\n")
    else:
        chosenPot = input("You're player 2, so choose from the top six.\n")


    if canBeInt(chosenPot) == False: #Input validation on chosen pot
        print("That's not a valid pot number.")
    else:
        chosenPot = int(chosenPot)
        if chosenPot < 1 or chosenPot > 6:
            print("That's not a valid pot number.")
        else:
            validPot = True

