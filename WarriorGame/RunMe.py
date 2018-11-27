'''
Created on 27.11.2018

@author: Klaus
'''
from Aufgabe import Aufgabe

if __name__ == '__main__':
    name = input("Input the name of the warrior")
    print("The warriors name is " +name)
    
    "Aufgabe wird getestet"
    
    x = Aufgabe("Test", 1)
    print(x.experience)
    print(x.goldReward)
    print(x.name)
    print(x.questLevel)
    
    
    