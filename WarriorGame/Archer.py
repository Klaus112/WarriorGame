'''
Created on 27.11.2018

@author: Marcel2000
'''
from Monster import Monster

class Archer(Monster):



    def __init__(self,name,quest,hero):
      
        super().__init__(name)
        self.damage = 10*(hero.level + quest.questlevel)
        self.health = 20*(hero.level + quest.questlevel)