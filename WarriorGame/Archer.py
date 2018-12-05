'''
Created on 27.11.2018

@author: Marcel2000
'''
from Monster import Monster
from Aufgabe import Aufgabe
from Hero import Hero

class Archer(Monster):



    def __init__(self,name,quest,hero):
      
        super().__init__(name)
        self.damage = 10*(hero.HeroLevel + quest.questLevel)
        self.health = 20*(hero.HeroLevel + quest.questLevel)