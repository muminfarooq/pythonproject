# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:10:19 2020

@author: Mumin
"""


OPTIONS=['Rock','Paper','Scissors']
import random
class RockPaperScissors:
    def __init(self):
        self.human_choice=None
        self.computer_choice=None
        
    def get_human_choice(self):
        choice=int(input('Enter your choice'))
        self.human_choice=OPTIONS[choice-1]
    def get_computer_choice(self):
        self.computer_choice=random.choice(OPTIONS)
            
    def print_options(self):
        print('\n'.join(f'({index}) {option.title()}'for index ,option in enumerate( OPTIONS) ))
    def print_choices(self):
        print(f'You chose {self.human_choice}')
        print(f'computer choose {self.computer_choice}')
        
    def print_win_loose(self,human_beats,human_loses_to):
        if self.computer_choice==human_beats:
            print(f'YES {self.human_choice} beats {self.computer_choice}')
        elif self.computer_choice==human_loses_to:
            print(f'Sorry {self.computer_choice} beats {self.human_choice}')
    def print_results(self):
        if self.human_choice==self.computer_choice:
            print('Draw')
        elif self.human_choice=='Rock':
            self.print_win_loose('Scissors', 'Paper')
        elif self.human_choice=='Scissors':
            self.print_win_loose('Paper','rock')
        elif self.human_choice=='Paper':
            self.print_win_loose('Rock','Scissors')
        
    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_results()
        
        
        
c=RockPaperScissors()
c.simulate()        
        
        
