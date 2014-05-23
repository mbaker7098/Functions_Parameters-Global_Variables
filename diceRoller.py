import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll():
    print("rolling.....")
    roll = random.randint(1,6) #generates a random number between 1 -6
    time.sleep(1)
    print(roll)
    return roll#returns the roll variable to the main function
   
def until_six(roll):#functions 
    roll = 0
    while roll != 6:
        roll = random.randint(1,6)
        print(roll)
        time.sleep(1)
        if roll == 6:
            print("it reached a 6!!")
            break #stops the loops

def show_dice(roll):#carries the roll variable to this function
    print(roll)
    if roll == 1:#prints the side of the dice corrosponding number (1 would be s1)
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)


roll=roll()
print(roll)
show_dice(roll)

