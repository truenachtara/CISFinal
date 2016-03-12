#tilt-tac-toe
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
player = False

def moveLeft(): #Shift board to the left
    global row1
    global row2
    global row3
    row1 = [row1[1],row1[2]," "]
    row2 = [row2[1],row2[2]," "]
    row3 = [row3[1],row3[2]," "]
#end moveLeft

def moveRight(): #Shift board to the right
    global row1
    global row2
    global row3
    row1 = [" ",row1[0],row1[1]]
    row2 = [" ",row2[0],row2[1]]
    row3 = [" ",row3[0],row3[1]]
#end moveRight

def refreshBoard():
    print("   |   |   ")
    print("",row1[0],"|",row1[1],"|",row1[2],"")
    print("---+---+---")
    print("",row2[0],"|",row2[1],"|",row2[2],"")
    print("---+---+---")
    print("",row3[0],"|",row3[1],"|",row3[2],"")
    print("   |   |   ")

def main():
    print("████████╗██╗██╗  ████████╗              ████████╗ █████╗  ██████╗              ████████╗ ██████╗ ███████╗\n╚══██╔══╝██║██║  ╚══██╔══╝              ╚══██╔══╝██╔══██╗██╔════╝              ╚══██╔══╝██╔═══██╗██╔════╝\n   ██║   ██║██║     ██║       █████╗       ██║   ███████║██║         █████╗       ██║   ██║   ██║█████╗  \n   ██║   ██║██║     ██║       ╚════╝       ██║   ██╔══██║██║         ╚════╝       ██║   ██║   ██║██╔══╝  \n   ██║   ██║███████╗██║                    ██║   ██║  ██║╚██████╗                 ██║   ╚██████╔╝███████╗\n   ╚═╝   ╚═╝╚══════╝╚═╝                    ╚═╝   ╚═╝  ╚═╝ ╚═════╝                 ╚═╝    ╚═════╝ ╚══════╝")
    print("ASCII art created by: http://patorjk.com/software/taag/")

    print("Tilt-Tac-Toe is like regular tic-tac-toe, except before your turn you may also type < or > to shift the board left or right. Type Q to quit.")
    print("All X's or O's that would be shifted off the board fall into the deep blackness of the void below.")
    print("These are the values that each square corresponds to:")

    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("   |   |   \n\n")

    keepPlay = "go"

    while keepPlay == "go":
        keepPlay = makeTurn()

    print("Thanks for playing!")

def canBeInt(s): #Checks if a string can be an integer. 
    try: 
        int(s)
        return True
    except ValueError:
        return False

def makeTurn():
    refreshBoard()
    global player
    global row1
    global row2
    global row3
    player = not player
    validInput = False
    print("Type < or > to tilt the board, and anything else to choose not to move the board.")
    
    if player:
        userInput = input("You're X.\n")
    else:
        userInput = input("You're O.\n")

    if userInput == "q":
        return "stop"
    
    if userInput == ">":
        moveRight()
        refreshBoard()
    elif userInput == "<":
        moveLeft()
        refreshBoard()
    #end if

    canPlay = False
    
    while canPlay == False:
        userInput = " "
        validInput = False
        while validInput == False:
            userInput = input("Which square would you like?\n")

            if userInput.lower == "q":
                return "stop"
            
            if canBeInt(userInput) == False:
                print("Invalid input!")
            else:
                userInput = int(userInput)

                if userInput in range(1,10):
                    validInput = True
                else:
                    print("Invalid input!")
                #end if
            #end if
        #end while

        if userInput == 1:
            if row1[0] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row1[0] = "X"
                else:
                    row1[0] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 2:
            if row1[1] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row1[1] = "X"
                else:
                    row1[1] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 3:
            if row1[2] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row1[2] = "X"
                else:
                    row1[2] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 4:
            if row2[0] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row2[0] = "X"
                else:
                    row2[0] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 5:
            if row2[1] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row2[1] = "X"
                else:
                    row2[1] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 6:
            if row2[2] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row2[2] = "X"
                else:
                    row2[2] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 7:
            if row3[0] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row3[0] = "X"
                else:
                    row3[0] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 8:
            if row3[1] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row3[1] = "X"
                else:
                    row3[1] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput == 9:
            if row3[2] != " ":
                print("That square has something in it already.")
            else:
                if player:
                    row3[2] = "X"
                else:
                    row3[2] = "O"
                #end if
                canPlay = True
            #end if
        elif userInput.lower == "q":
            return "stop"
        #end if


    if row1[0] == row1[1] == row1[2] == "X" or row2[0] == row2[1] == row2[2] == "X" or row3[0] == row3[1] == row3[2] == "X" or  row1[0] == row2[0] == row3[0] == "X" or row1[1] == row2[1] == row3[1] == "X" or row1[2] == row2[2] == row3[2] == "X" or row1[0] == row2[1] == row3[2] == "X" or row1[2] == row2[1] == row3[0] == "X":
        refreshBoard()
        print("X wins!!!")
        return "stop"
    elif row1[0] == row1[1] == row1[2] == "O" or row2[0] == row2[1] == row2[2] == "O" or row3[0] == row3[1] == row3[2] == "O" or  row1[0] == row2[0] == row3[0] == "O" or row1[1] == row2[1] == row3[1] == "O" or row1[2] == row2[2] == row3[2] == "O" or row1[0] == row2[1] == row3[2] == "O" or row1[2] == row2[1] == row3[0] == "O":
        refreshBoard()
        print("O wins!!!")
        return "stop"

    return "go"


main()
