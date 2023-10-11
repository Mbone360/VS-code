'''
    This module runs the entire game pulling functions and variables from role1.py, role2.py, and game.py
'''
import role1
import role2
import game
# variables that are global
player = ""
con1 = True
con2 = True
# welcome message
print("WELCOME TO WARHAMMER")

# loops game
while con2:

    # loops menu
    while con1:

        # prints menu
        print("Will you fight for the Imperium or the Tau Empire")
        print("1. Space Marines\n2. Tau Empire\n3. Quit")
        choice = eval(input("Please choose an option:"))

        # sets player role
        if choice == 1:
            player = role1.name
            con1 = False
        elif choice == 2:
            player = role2.name
            con1 = False
        elif choice == 3:
            print("Exiting the game")
            exit()
        else:
            print("Invalid choice. Please try again")

        # will print out coresponding attributes
        print("You are playing as the ", player, " with the following attributes:")
        if player == "Space Marine's":
            print(role1.name,
                    "\nStrength: ",role1.strg,
                    "\nDexterity: ",role1.dex,
                    "\nIntelligence: ",role1.int,
                    "\nHealth: ",role1.hh,
                    "\nLives: ",role1.lv)
        elif player == "Tau Empire":
            print(role2.name,
                    "\nStrength: ",role2.strg,
                    "\nDexterity: ",role2.dex,
                    "\nIntelligence: ",role2.int,
                    "\nHealth: ",role2.hh,
                    "\nLives: ",role2.lv)
            
    # shows user what the challenges are
    print("\nThe 3 objectives are \n1. Escaping the Necrons (Dexterity)\n2. Defeating the Necrons (Strength)\n3. Capturing the control point")

    # runs challenge 1
    print("\n Now!", game.c1, "the Necron force!")      
    roll1 = game.dice()
    print("You rolled a ", roll1)
    if player == role1.name:
        result1 = role1.dex + roll1
        print("You scored ", result1)
    elif player == role2.name:
        result1 = role2.dex + roll1
        print("You scored ", result1)
    # prints out challenge 1
    game.resolve1(result1)

    # runs challenge 2
    print("\n", game.c2, "!")
    roll2 = game.dice()
    print("You rolled a ", roll2)
    if player == role1.name:
        result2 = role1.strg + roll2
        print("You scored ", result2)
    elif player == role2.name:
        result2 = role2.strg + roll2
        print("You scored ", result2)
    # prints out challenge outcome
    game.resolve2(result2)

    # runs challenge 3
    print("\n", game.c3, "!")
    roll3 = game.dice()
    print("You rolled a ", roll3)
    if player == role1.name:
        result3 = role1.int + roll3
        print("You scored ", result3)

    elif player == role2.name:
        result3 = role2.int + roll3
        print("You scored ", result3)
    # prints out challenge outcom
    game.resolve3(result3)
    
    # calculates if the user won enough objectives
    total = result1 + result2 + result3
    if total > 20:
        print("\nYou won enough objectives")

    # asks the user if they want to play again
    inp = input("Would you like to play again? y/n")
    if inp == 'n':
        con2 = False
    else:
        con1 = True
        choice = 0