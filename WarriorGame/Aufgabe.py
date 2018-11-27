'''
Created on 27.11.2018

@author: Martin
'''
from random import randint


class Aufgabe():
    '''
    classdocs
    '''
   
    

    def __init__(self, name, questLevel, goldReward, experience):
        '''
        Constructor
        '''
        self.name = name
        self.questLevel = questLevel
        self.goldReward = self.questLevel + randint(0,2)
        self.experience = experience     