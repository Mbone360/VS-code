import role1
import role2
import game

def main():
    game = game()
    print("WELCOME TO WARHAMMER")
    while True:
        print("Will you fight for the Imperium or the Tau Empire")
        print("1. Space Marines\n2. Tau Empire\n3. Quit")
        choice = eval(input("Please choose an option"))

        if choice == 1:
            player = role1.name()
        elif choice == 2:
            player = role2.name()
        elif choice == 3:
            print("Exiting the game")
            break
        else:
            print("Invalid choice. Please try again")

        print("You are playing as the ", player, " with the following attributes:")
        if player == "Space Marine's":
            print(role1.name,
                  "\n",role1.strg,
                  "\n",role1.dex,
                  "\n",role1.int,
                  "\n",role1.hh,
                  "\n",role1.lv)
        elif player == "Tau Empire":
            print(role2.name,
                  "\n",role2.strg,
                  "\n",role2.dex,
                  "\n",role2.int,
                  "\n",role2.hh,
                  "\n",role2.lv)
            
           
    print("The 3 objectives are 1. Escaping the Necrons (Dexterity)\n2. Defeating the Necrons (Strength)\n3. Capturing the control point")

    print(game.c1, " the Necron force!")
    roll1 = game.dice
    print("You rolled a ", roll1)
    if player == role1.name:
        result1 = role1.dex + roll1
    elif player == role2.name:
        result1 = role2.dex + roll1
    game.resolve1

    print(game.c2, "!")
    roll2 = game.dice
    print("You rolled a ", roll2)
    if player == role1.name:
        result1 = role1.strg + roll2
    elif player == role2.name:
        result1 = role2.strg + roll2
    game.resolve2

    print(game.c3, "!")
    roll3 = game.dice
    print("You rolled a ", roll3)
    if player == role1.name:
        result1 = role1.int + roll3
    elif player == role2.name:
        result1 = role2.int + roll3
    game.resolve3

    game.check