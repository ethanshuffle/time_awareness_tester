from reaction_test import game_mode_sequence
from scoreboard import scoreboard_menu_sequence
import time

def clear_console():
  print("\033c", end='')

def shuff_print():
  print(" __ _            __  __ ")
  print("/ _\ |__  _   _ / _|/ _|")
  print("\ \| '_ \| | | | |_| |_ ")
  print("_\ \ | | | |_| |  _|  _|")
  print("\__/_| |_|\__,_|_| |_|  ")

def main_menu_print():
  print("d888888P  88888888b .d88888b  d888888P ")
  print("   88     88        88.          88    ")
  print("   88    a88aaaa    `Y88888b.    88  ")
  print("   88     88              `8b    88   ")
  print("   88     88        d8'   .8P    88")
  print("   dP     88888888P  Y88888P     dP")
  time.sleep(1)
  print("dP    dP  .88888.  dP     dP  888888ba ")
  print("Y8.  .8P d8'   `8b 88     88  88    `8b")
  print(" Y8aa8P  88     88 88     88 a88aaaa8P'")
  print("   88    88     88 88     88  88   `8b. ")
  print("   88    Y8.   .8P Y8.   .8P  88     88 ")
  print("   dP     `8888P'  `Y88888P'  dP     dP")
  time.sleep(1)
  print("8888ba.88ba  dP  .88888.  dP     dP  d888888P")
  print("88  `8b  `8b 88 d8'   `88 88     88     88 ")
  print("88   88   88 88 88        88aaaaa88a    88")
  print("88   88   88 88 88   YP88 88     88     88 ")
  print("88   88   88 88 Y8.   .88 88     88     88 ")
  print("dP   dP   dP dP  `88888'  dP     dP     dP")
  print("")
  print("")
  time.sleep(1)
  print("1. Start")
  print("2. Tutorial")
  print("3. Scoreboards")
  print("4. Exit")
  
def main_menu_input():
  choice = input("Select a menu option: ")
  if (choice == "1"):
    clear_console()
    game_mode_sequence()
  elif (choice == "2"):
    clear_console()
    tutorial()
    tutorial_exit()
  elif (choice == "3"):
    clear_console()
    scoreboard_menu_sequence()
  elif (choice == "4"):
    clear_console()
    print("Goodbye!")
  else:
    print("Invalid choice; try again")
    main_menu_input()
    
def menu_sequence():
  clear_console()
  main_menu_print()
  main_menu_input()
  
def tutorial():
  print("This game has 3 game modes: classic, random, and blind.")
  print("")
  print("Classic mode:")
  print("A timer is displayed after a short countdown Your goal is to press the enter ")
  print("key once the timer hits 10 seconds")
  print("")
  print("Random mode:")
  print("A timer is displayed after a short countdown, alongside a random time to hit.")
  print("Your goal is to press the enter key once the timer hits the number provided.")
  print("")
  print("Blind mode:")
  print("After a short countdown, an invisible timer begins. Your goal is to press the")
  print("enter key once the timer hits 10 seconds.")
  print("")

def tutorial_exit():
  choice = input("Press enter to return to menu")
  if (choice == ""):
    clear_console()
    menu_sequence()
  else:
    clear_console()
    menu_sequence()



