'''
Created on 27.11.2018

@author: Marcel2000
'''
from Monster import Monster
from Aufgabe import Aufgabe
from Hero import Hero

class Mage(Monster):
    '''
    classdocs
    '''


    def __init__(self,name,quest,hero):
        '''
        Constructor
        '''
        super().__init__(name)
        self.damage = 20*(hero.HeroLevel + quest.questLevel)
        self.health = 10*(hero.HeroLevel + quest.questLevel)