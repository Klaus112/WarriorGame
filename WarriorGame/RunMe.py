'''
Created on 27.11.2018

@author: Klaus
'''
from Aufgabe import Aufgabe
'''
The main function of this game
'''

def inputName():
    '''
    The function that will create the hero and ask the user for a name
    '''
    name = input("Input the name of the warrior")
    print("The warriors name is " +name)
    #placeholder Hero(name,....) erstellen
    return name;
def getNumber():
    '''
    A function that checks if the user has entered a number
    '''
    while (True):
        x = input("Please enter a number")
        try:
            int(x)
            break;
        except ValueError:
            print ("This is not a number")
    return x;
def mainMenu():
    '''
    The main menu function of the game
    '''
    print("Welcome to the main Menu")
    print("1) Show your stats")
    print("2) Enter the marketplace (to upgrade your weapon)")
    print("3) Continue with your adventure (Get a quest)")
    print("4) Exit the game")

def marketplace():
    pass;

if __name__ == '__main__':
    inputName();
    while(True):
        mainMenu()
        getNumber()
        
        break;
