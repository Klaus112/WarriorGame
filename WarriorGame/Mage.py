'''
Created on 27.11.2018

@author: Marcel2000
'''
from Monster import Monster

class Mage(Monster):
    '''
    classdocs
    '''


    def __init__(self,name,quest,hero):
        '''
        Constructor
        '''
        super().__init__(name)
        self.damage = 20*(hero.level + quest.questlevel)
        self.health = 10*(hero.level + quest.questlevel)