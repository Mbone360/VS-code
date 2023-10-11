# game.py
import random
# the 3 game challenges
c1 = "Escape"
c2 = "Defeat the Necrons"
c3 = "Capture the control point"

def dice():
    return random.randint(2, 12)

def resolve1(result1, player):
    if result1 < 4:
        print("You did not escape the invading force of Necrons and had no surviors!")
        player -1
    elif 4 < result1 < 8:
        print("You escaped the Necrons with no casualties!")
        player + 1
    elif result1 > 8:
        print("You escaped the Necron force while also dealing devastating damage!")
        player + 2

def resolve2(result2, player):
    if result2 < 4:
        print("Your attack on the Necrons failed misserably!")
        player - 1
    elif 4 < result2 < 8:
        print("You succened in attacking the Necron strong hold!")
        player + 1
    elif result2 > 8:
        print("You succened in attacking the Necron strong hold, and also pushed intho their territory!")
        player + 2

def resolve3(result3, player):
    if result3 < 4:
        print("You did not capture the control point!")
        player - 1
    elif 4 < result3 < 8:
        print("You captured the control point!")
        player + 1
    elif result3 > 8:
        print("You captured the control point and also retrieved valuable data from the Necrons!")
        player + 2

def check(player):
    if player < 2:
        print("You lost too many objectives")
    elif 2 < player < 5:
        print("You won all of the objects")
    elif player == 6:
        print("You exceding in completeing all of the objectives")