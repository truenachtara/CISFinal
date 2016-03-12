#mancala
import time

side1 = [0,4,4,4,4,4,4] #Side 1's stones. side1[0] is P2's mancala
side2 = [0,4,4,4,4,4,4] #Side 2's stones. side2[0] is P1's mancala
player = False #player is a boolean variable, "true" being player 1 and "false" being player 2

def refreshBoard(): #Updates the board on-screen with a running total of stones in all pots
    print(" _________________________________________________________")
    print("|  ____   ____   ____   ____   ____   ____   ____   ____  |")
    print("| |    | |    | |    | |    | |    | |    | |    | |    | |")
    print("| |    | |",str(side2[1]).zfill(2),"| |",str(side2[2]).zfill(2),"| |",str(side2[3]).zfill(2),"| |",str(side2[4]).zfill(2),"| |",str(side2[5]).zfill(2),"| |",str(side2[6]).zfill(2),"| |    | |")
    print("| |    | |____| |____| |____| |____| |____| |____| |    | |")
    print("| |    |   1      2      3      4      5      6    |    | |")
    print("| |",str(side2[0]).zfill(2),"|                                           |",str(side1[0]).zfill(2),"| |")
    print("| |    |  _6__   _5__   _4__   _3__   _2__   _1__  |    | |")
    print("| |    | |    | |    | |    | |    | |    | |    | |    | |")
    print("| |    | |",str(side1[6]).zfill(2),"| |",str(side1[5]).zfill(2),"| |",str(side1[4]).zfill(2),"| |",str(side1[3]).zfill(2),"| |",str(side1[2]).zfill(2),"| |",str(side1[1]).zfill(2),"| |    | |")
    print("| |____| |____| |____| |____| |____| |____| |____| |____| |")
    print("|_________________________________________________________|")
    print()
#end refreshBoard

def canBeInt(s): #Checks if a string can be an integer. 
    try: 
        int(s)
        return True
    except ValueError:
        return False

def checkSave(): #Checks if there is a save file
    try: 
        open("save.txt", "r")
        return True
    except FileNotFoundError:
        return False

def makeTurn(): #This will prompt a player to choose a pot.
    global player
    global side1
    global side2
    player = not player
    validPot = False
    print("Which pot do you choose? Enter the number of your pot.")
    if player == True: #Checks who is playing, and tells them which pot to choose from.
        chosenPot = input("You're player 1, so choose from the bottom six.\n")
    else:
        chosenPot = input("You're player 2, so choose from the top six.\n")
    #end if

    if chosenPot.lower() == "q":
        return "stop"
    elif chosenPot.lower() == "s":
        
        with open("save.txt", "w") as f: #Open new file called "save.txt" and erase any previous saves
            for i in range(0,7):
                f.write(str(side1[i]))
                f.write(" ")
            #end for

            f.write("\n")
            
            for i in range(0,7):
                f.write(str(side2[i]))
                f.write(" ")
            #end for

            f.write("\n")
            
            print("Game has been saved.")
        #end with. Close file!

    elif chosenPot.lower() == "l":
        if checkSave():
            with open("save.txt", "r") as f:
                data = f.readlines() #Loads the data

                side = 1
                for line in data: #Splits data into lines
                    numbers = line.split() #Splits the lines into arrays
                    
                    if side == 2:
                        for i in range(0,7):                            
                            side2[i] = int(numbers[i])
                        #end for
                    elif side == 1:
                        for i in range(0,7):
                            side1[i] = int(numbers[i])
                        #end for
                    #end if
                        
                    side = 2
                #end for
            print("Data successfully loaded.")
            refreshBoard()
            #end with. Close file!
        else:
            print("There is no save file yet! Type S to save!")
            
                
    while validPot == False:
        if canBeInt(chosenPot) == False and chosenPot != "s" and chosenPot != "l": #Input validation on chosen pot
            print("That's not a valid pot number. Please try again.")
        elif chosenPot == "s" or chosenPot == "l":
            print("Please pick a number.")
        else:
            chosenPot = int(chosenPot)
            if chosenPot < 1 or chosenPot > 6:
                print("That's not a valid pot number. Please try again.")
            else:
                if player:
                    if side1[chosenPot] == 0:
                        print("That pot's empty!")
                    else:
                        validPot = True
                        choosePot(chosenPot)
                else:
                    if side2[chosenPot] == 0:
                        print("That pot's empty!")
                    else:
                        validPot = True
                        choosePot(chosenPot)

        if validPot == False:
            chosenPot = input("Which pot do you choose?\n")

    return "go"

def choosePot(pot): #Choose which pot to pick
    if player:
        if pot == 1:
            stones = side1[1]
            side1[1] = 0
            inS1P5(stones)
        elif pot == 2:
            stones = side1[2]
            side1[2] = 0
            inS1P4(stones)
        elif pot == 3:
            stones = side1[3]
            side1[3] = 0
            inS1P3(stones)
        elif pot == 4:
            stones = side1[4]
            side1[4] = 0
            inS1P2(stones)
        elif pot == 5:
            stones = side1[5]
            side1[5] = 0
            inS1P1(stones)
        elif pot == 6:
            stones = side1[6]
            side1[6] = 0
            inMan1(stones)
    else:
        if pot == 1:
            stones = side2[1]
            side2[1] = 0
            inS2P2(stones)
        elif pot == 2:
            stones = side2[2]
            side2[2] = 0
            inS2P3(stones)
        elif pot == 3:
            stones = side2[3]
            side2[3] = 0
            inS2P4(stones)
        elif pot == 4:
            stones = side2[4]
            side2[4] = 0
            inS2P5(stones)
        elif pot == 5:
            stones = side2[5]
            side2[5] = 0
            inS2P6(stones)
        elif pot == 6:
            stones = side2[6]
            side2[6] = 0
            inMan2(stones)


#WARNING: THE FOLLOWING IS ONE GIANT LOOP COMPOSED OF LIKE 14 FUNCTIONS
#==================================================SIDE 1 STUFF================================================
def inS1P1(stones): #Side 1, Pot 1
    turnOver = False
    side1[6] += 1
    stones -= 1

    if stones == 0 and side1[6] > 1:
        stones = side1[6]
        side1[6] = 0
    elif stones == 0 and side1[6] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False and player == True:
        inMan1(stones)
    elif turnOver == False and player == False:
        inS2P1(stones)
#end inS1P1

def inS1P2(stones): #Side 1, Pot 2
    turnOver = False
    side1[5] += 1
    stones -= 1

    if stones == 0 and side1[5] > 1:
        stones = side1[5]
        side1[5] = 0
    elif stones == 0 and side1[5] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS1P1(stones)
#end inS1P2

def inS1P3(stones): #Side 1, Pot 3
    turnOver = False
    side1[4] += 1
    stones -= 1

    if stones == 0 and side1[4] > 1:
        stones = side1[4]
        side1[4] = 0
    elif stones == 0 and side1[4] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS1P2(stones)
#end inS1P3

def inS1P4(stones): #Side 1, Pot 4
    turnOver = False
    side1[3] += 1
    stones -= 1

    if stones == 0 and side1[3] > 1:
        stones = side1[3]
        side1[3] = 0
    elif stones == 0 and side1[3] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS1P3(stones)
#end inS1P4

def inS1P5(stones): #Side 1, Pot 5
    turnOver = False
    side1[2] += 1
    stones -= 1

    if stones == 0 and side1[2] > 1:
        stones = side1[2]
        side1[2] = 0
    elif stones == 0 and side1[2] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS1P4(stones)
#end inS1P5

def inS1P6(stones): #Side 1, Pot 6
    turnOver = False
    side1[1] += 1
    stones -= 1

    if stones == 0 and side1[1] > 1:
        stones = side1[1]
        side1[1] = 0
    elif stones == 0 and side1[1] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS1P5(stones)
#end inS1P6

def inMan1(stones): #In Player 1's mancala
    turnOver = False
    side2[0] += 1
    stones -= 1

    if stones == 0:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS2P1(stones)
#end inMan1

#=========================================================SIDE 2 STUFF===============================================================

def inS2P1(stones): #Side 2, Pot 1
    turnOver = False
    side2[1] += 1
    stones -= 1

    if stones == 0 and side2[1] > 1:
        stones = side2[1]
        side2[1] = 0
    elif stones == 0 and side2[1] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS2P2(stones)
#end inS2P1

def inS2P2(stones): #Side 2, Pot 2
    turnOver = False
    side2[2] += 1
    stones -= 1

    if stones == 0 and side2[2] > 1:
        stones = side2[2]
        side2[2] = 0
    elif stones == 0 and side2[2] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS2P3(stones)
#end inS2P2

def inS2P3(stones): #Side 2, Pot 3
    turnOver = False
    side2[3] += 1
    stones -= 1

    if stones == 0 and side2[3] > 1:
        stones = side2[3]
        side2[3] = 0
    elif stones == 0 and side2[3] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS2P4(stones)
#end inS2P3

def inS2P4(stones): #Side 2, Pot 4
    turnOver = False
    side2[4] += 1
    stones -= 1

    if stones == 0 and side2[4] > 1:
        stones = side2[4]
        side2[4] = 0
    elif stones == 0 and side2[4] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS2P5(stones)
#end inS2P4

def inS2P5(stones): #Side 2, Pot 5
    turnOver = False
    side2[5] += 1
    stones -= 1

    if stones == 0 and side2[5] > 1:
        stones = side2[5]
        side2[5] = 0
    elif stones == 0 and side2[5] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS2P6(stones)
#end inS2P5

def inS2P6(stones): #Side 2, Pot 6
    turnOver = False
    side2[6] += 1
    stones -= 1

    if stones == 0 and side2[6] > 1:
        stones = side2[6]
        side2[6] = 0
    elif stones == 0 and side2[6] == 1:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False and player == False:
        inMan2(stones)
    elif turnOver == False and player == True:
        inS1P6(stones)
#end inS1P6

def inMan2(stones): #In Player 2's mancala
    turnOver = False
    side1[0] += 1
    stones -= 1

    if stones == 0:
        turnOver = True
    else:
        print("Made a move.")
    #end if
    refreshBoard()

    if turnOver == False:
        inS1P6(stones)
#end inMan1

#==========================================END OF THE MAIN LOOP======================================

def main():
    print("███╗   ███╗ █████╗ ███╗   ██╗ ██████╗ █████╗ ██╗      █████╗\n████╗ ████║██╔══██╗████╗  ██║██╔════╝██╔══██╗██║     ██╔══██╗\n██╔████╔██║███████║██╔██╗ ██║██║     ███████║██║     ███████║\n██║╚██╔╝██║██╔══██║██║╚██╗██║██║     ██╔══██║██║     ██╔══██║\n██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║\n╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
    print("ASCII art created by: http://patorjk.com/software/taag/")
    print("You can enter the following when asked to make a move: Q to quit, S to save, and L to load.")

    refreshBoard()
    keepPlay = "go"

    while keepPlay == "go":
        keepPlay = makeTurn()
        if side1[0] == sum(side1) or side2[0] == sum(side2):
            keepPlay = "end"
            if side1[0] > side2[0]:
                print("Player 2 wins with", side1[0],"stones!")
            elif side1[0] < side2[0]:
                print("Player 1 wins with", side2[0],"stones!")
            else:
                print("The game ends in a tie!~")
            

    print("Thanks for playing! Play again some time!")
#end main


main()
