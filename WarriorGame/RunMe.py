'''
Created on 27.11.2018

@author: Klaus
'''
from Aufgabe import Aufgabe
from Hero import Hero
from random import randint
from Archer import Archer
from Mage import Mage
import sys
'''
The main function of this game
'''


def inputHeroName():
    '''
    The function that will create the hero and ask the user for a name
    '''
    name = input("Input the name of the warrior")
    player = Hero(name)
    return player;

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
    print("Welcome to the main Menu, " +player.Name)
    print("1) Show your stats")
    print("2) Enter the marketplace (to upgrade your weapon)")
    print("3) Continue with your adventure (Get a quest)")
    print("4) Exit the game")

def showStats():
    '''
    A function that shows the players stats
    '''
    print("Your level is "+str(player.HeroLevel))
    print("Your weapon level is " +str(player.WeaponLevel))
    print("Your current gold is "+str(player.GoldValue))
    print("Your damage is " +str(player.Damage))
    print("Your health is " +str(player.Health))
    input("press enter to continue")
    
def marketplace():
    '''
    The upgrade handling for the weaponlevel
    '''
    cost = player.WeaponLevel * 2
    print("Do you wanna upgrade your weapon by 1 (costs " +str(cost)+"), you have "+str(player.GoldValue)+" money")
    if(input(" enter y or anything else") == 'y'):
        if(player.GoldValue >= cost):
            player.setWeaponLevel(1)
            player.GoldValue = player.GoldValue-cost
            print("Your weapon was upgraded")
        else:
            print("You don't have enough money")

def adventure():
    print("What difficulty do you want the quest to be(1-3)")
    choice = int(getNumber())
    if(1 <= choice and choice <= 3):
        a = Aufgabe("Adventure",choice);
        if(randint(0,1) == 0):
            m = Archer("Robin_Hood",a,player)
        else:
            m = Mage("Gandalf",a,player)
    counterm = 0;
    counterh = 0;
    j = 1
    while(m.damage * j < player.Health):
        counterm += 1
        j += 1
    j= 1;
    while(player.Damage * j< m.health):
        counterh += 1
        j += 1
        
    if(counterh >= counterm):
        print("You won against the mob")
        print("You got "+str(a.goldReward)+" gold")
        player.GoldValue = player.GoldValue + a.goldReward
        print("You gained " +str(a.experience)+" levels")
        player.setHeroLevel(a.experience)
        input("Press a button to continue")
        
    else:
        print("You loose and the game is over")
        sys.exit()
            
if __name__ == '__main__':
    '''
    The main game loop
    '''
    player = inputHeroName();
    while(True):
        mainMenu()
        choice = getNumber()
        if(choice == '1'):
            showStats()
        elif(choice == '2'):
            marketplace()
        elif(choice == '3'):
            adventure()
            
        else:
            print("See you soon!")
            break;