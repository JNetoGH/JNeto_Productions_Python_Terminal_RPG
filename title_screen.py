# IMPORTS

import time
from time import sleep

# Initialize rich (UI, GUI builder) modules
import rich

from rich.progress import Progress, track
from rich.console import Console
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

from pyfiglet import Figlet  # This is what draws the title screen name
from char_and_squad.battle_entities import Character

# Turn off later
from classes_example import Class

# VARS to define
console = Console()  # easier to work with rich's console commands
f = Figlet(font='standard', justify='center')
listofclasses = Class.__subclasses__  # wanted to make a list here but got a bunch of errors
columns = Columns(listofclasses, equal=True, expand=True)  # will only work if listofclasses is an array or list!


# Functions

# the intention here was to get all classes and then get each individual one in a table/cell
# isn't working
def show_class(ind):
    for ind in listofclasses:
        indexes = list(listofclasses.index(ind))  # doesn't let me iterate...
        return indexes

    return f"[b]{listofclasses}[/b]\n[yellow]{indexes}"


def newChar() -> object:
    charcreation: bool = True  # make it loopable
    while charcreation:
        print("—" * 100)
        print("\n" + '{:^75}'.format("Hi! Welcome to the character creator.\n") + "Here's a quick list of the available classes:\n")
        print("...\n")  # should be here where we print the columns
        print("What's the name of your character?")
        n_name = input()
        print(f"And which class is {n_name}'s?")
        n_speclass = input()
        print(f"So you are creating a {n_speclass} named {n_name}. Is that right?")
        confirm = input()
        if confirm == "Yes" or confirm == "yes" or confirm == "Y" or confirm == "y":
            mychar = Character(str(n_name), 10, 5, 5, 5, 10)  # era pra ser n_speclass(n_name, .....) mas n funfou
            print("Character creation successful!")
            charcreation = False
            return mychar, charcreation
        elif confirm == "No" or confirm == "no" or confirm == "N" or confirm == "n":
            print(
                "Let's start from the beggining again, then.")  # and here it should return to the beginning of the loop
        else:
            print("That command doesn't exist.")


# actual interface
"""THIS IS THE MAIN LOOP/BRANCH"""

while True:
    # them = [Panel(show_class(ind), expand=True) for ind in listofclasses]  # trying an alternative way to get the tables
    # testing    print(Columns(them))
    # testing    print(columns)

    print("\n\n")
    print(f.renderText("Game Name"))  # GAME LOGO
    print('{:^75}'.format('Press <m> to start.'))  # trying to center this, trying to get a game boy vibe
    print("\n")
    UserInput = input()

    if UserInput == "m":
        print("\n")
        print(f.renderText("Game Name"))  # showing logo again
        with console.status("[bold green]Initializing...".center(40)) as status:  # this doesn't actually initialize
            # anything, it just looks nice
            sleep(5)
            console.status(f'[bold][red]Done!\n')

    print('{:^85}'.format('Would you like to create a new character or play with the default ones?'))
    print("\n")
    sleep(1)
    print('{:^80}'.format('[1] New Character | [2] Default Character'))

    getInput = int(input())

    if getInput == 1:
        newChar()
    elif getInput == 2:
        pass
    else:
        print("Not a valid option.")