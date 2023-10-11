'''
    This module handles dice roles and callenge outcoms
'''
import random

# the 3 game challenges
c1 = "Escape"
c2 = "Defeat the Necrons"
c3 = "Capture the control point"

# rolls the 2 dice
def dice():
    return random.randint(2, 12)

# figures out the outcome of the first chellenge
def resolve1(result1):
    if result1 < 10:
        print("You did not escape the invading force of Necrons and had no surviors!")
    elif 10 <= result1 <= 15:
        print("You escaped the Necrons with no casualties!")
    elif result1 > 15:
        print("You escaped the Necron force while also dealing devastating damage!")
    return(result1)

# figures out the outcome of the second challenge
def resolve2(result2):
    if result2 < 10:
        print("Your attack on the Necrons failed misserably!")
    elif 10 <= result2 <= 12:
        print("You succeded in attacking the Necron strong hold!")
    elif result2 > 12:
        print("You succeded in attacking the Necron strong hold, and also pushed into their territory!")
    return(result2)

# figures out the third chellenge
def resolve3(result3):
    if result3 < 11:
        print("You did not capture the control point!")
    elif 11 <= result3 <= 13:
        print("You captured the control point!")
    elif result3 > 13:
        print("You captured the control point and also retrieved valuable data from the Necrons!")
    return(result3)