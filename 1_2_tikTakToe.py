def ticTacToe():
    a = [' ',' ',' ']
    b = [' ',' ',' ']
    c = [' ',' ',' ']
    counter = 0
    xCounter = 0
    oCounter = 0
    counterForTies = 0
    tieCounter = 0
    print("\n")
    print("\n")
    print("\n")
    while counter < 2:
        if counter == 0:
            player = "X"
            incMe = 1
            decMe = 0
        else:
            player = "O"
            incMe = 0
            decMe = 1
        print("\n")
        print("  ~~~ " + player + "'s turn! ~~~")
        print("    1    2    3")
        print("a", a)
        print("b", b)
        print("c", c)
        r = eval(input("What row do you choose? (Single letter response): "))
        n = int(input("What number do you choose? (Single digit response): "))
        if r[n-1] != "X" and r[n-1] != "O":
            r[n-1] = player
            counterForTies = counterForTies + 1
            if a[0] + b[0] + c[0] == player*3 or a[1] + b[1] + c[1] == player*3 or a[2] + b[2] + c[2] == player*3 or a[0] + a[1] + a[2] == player*3 or b[0] + b[1] + b[2] == player*3 or c[0] + c[1] + c[2] == player*3 or a[0] + b[1] + c[2] == player*3 or a[2] + b[1] + c[0] == player*3:
                if player == "X":
                    xCounter = xCounter + 1
                elif player == "O":
                    oCounter = oCounter + 1
                print("\n")
                print("    1    2    3")
                print("a", a)
                print("b", b)
                print("c", c)                    
                print(player + "'s has won the game! Congrats!")
                x = input("Would you like to play again? (Yes = y/No = n): ")
                if x == "y":
                    for i in range(0,len(a)):
                        a[i] = ' '
                    for i in range(0,len(b)):
                        b[i] = ' '
                    for i in range(0,len(c)):
                        c[i] = ' '                        
                    counter = incMe
                    counterForTies = 0
                else:
                    print("X's have won " + str(xCounter) + " time(s).")
                    print("O's have won " + str(oCounter) + " time(s).")
                    print("There has been " + str(tieCounter) + " tie(s).")
                    return "Good job everyone! Hope you had fun!"
            elif counterForTies == 9:
                tieCounter = tieCounter + 1
                print("\n")
                print("    1    2    3")
                print("a", a)
                print("b", b)
                print("c", c)                    
                print("You have tied!")
                x = input("Would you like to play again? (Yes = y/No = n): ")
                if x == "y":
                    for i in range(0,len(a)):
                        a[i] = ' '
                    for i in range(0,len(b)):
                        b[i] = ' '
                    for i in range(0,len(c)):
                        c[i] = ' '
                    counter = decMe
                    counterForTies = 0
                else:
                    print("X's have won " + str(xCounter) + " time(s).")
                    print("O's have won " + str(oCounter) + " time(s).")
                    print("There has been " + str(tieCounter) + " tie(s).")
                    return "Good job everyone! Hope you had fun!"                    
            else:
                counter = incMe
        else:
            print("\n")
            print("##Try a different spot, that one is already taken!##")
