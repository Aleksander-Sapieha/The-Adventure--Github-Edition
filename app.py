import time
import sys
import subprocess
import os


while True:
    subprocess.run("cls" if os.name == "nt" else "clear")
    answer = input("do you want to play (yes/no)? ")

    if answer.lower().strip() == "yes":

        answer = input("you reach a crossroads, do you want to go left (1) or right (2)? ").lower().strip()
        if answer == "left" or answer == 1:
            answer = input("you encounter a monster, do you want to fight or run? ").lower().strip()

            if answer == "fight":
                print("the monster fights back and kills you (bad ending 1) ")
                time.sleep(1)

            elif answer == "run":
                answer = input("do you want to go into the forest?(yes/no) ")

                if answer == "yes":
                    print("you got lost and drowned in the river (bad ending 2) ")
                    time.sleep(1)
                elif answer == "no":
                    answer = input("you see a town nearby, do you want to go there (yes/no) ")

                    if answer == "yes":
                        print("you decided to live here(good ending 1) ")
                        time.sleep(1)
                    elif answer == "no":
                        answer = input("you decided to go on the opposite path, but suddenly you see a bear, do you want do fight or run" )
                        
                        if answer == "fight":
                            print("you killed the bear, but got a heart attack (bad ending 4)")
                            time.sleep(1)
                        elif answer == "run":
                            print("you got home (good ending 2)")
                            time.sleep(1)

        elif answer == "right" or answer == 2:
            print("you fall off a cliff and die (bad ending 3) ")
            time.sleep(1)
        else:
            print("you lost")
            time.sleep(1)

    else:
        print("bye!" )
        time.sleep(1)
        break

sys.exit(0)