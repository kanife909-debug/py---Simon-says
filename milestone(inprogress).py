import random
import os
import time
from highscore import *

red = 1
blue = 2
green = 3
colors = [1, 2, 3] #button 1 would red, button 2 would be blue, button 3 would be green.
sequence = []
round = 0


def showHighScore():
    print(f"High Score: {highscore} by {highname}")

print("\nThis is simmons says. Colors: 1 is red, 2 is blue, 3 is green.")

def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')


while True:
    round += 1
    print("Round:",round)
    new_color = random.choice(colors)
    sequence.append(random.choice(colors))

# how does one make the leds light up with sequence

    user_sequence = []



    print("Sequence:",sequence) #printing sequence

    time.sleep(3)    # Waits something amount of seconds.
    
    clear_terminal() # Clears the terminal

    for i in range(len(sequence)):
        user_input = int(input(f"Enter color #{i+1}: "))
        user_sequence.append(user_input)


    if user_sequence == sequence:
        print("Correct, next round.")

    elif user_sequence != sequence:
        print("Game over, Round:",round)
        again = input("Would you like to try again. Y/N? ")
        if again == "Y":
            sequence = []
            round = 0
            continue
        else:
            print("Game over")

            if round > highscore:
                clear()
                print(f"Game over\nNew High Score: {round}!")

                name = input("Enter your name: ")

                setHighScore(name, round)
                break
            else:
                clear()
                print("Game over")

                showHighScore()
                
                break

# 




