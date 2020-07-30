# An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference between dict() and OrderedDict() is that:

'''OrderedDict preserves the order in which the keys are inserted. 
A regular dict doesn’t track the insertion order, and iterating it gives the values in 
an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.'''
import os
from collections import OrderedDict

import commands

def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print('\t'.join(
            str(field) if field else''
            for field in bookmark
        ))      
class Option:
    def __init__(self,name,command,prep_call=None):
        self.name=name
        self.command=command
        self.prep_call=prep_call
    def _handle_message(self,message):
        if isinstance(message,list):
            print_bookmarks(message)
        else:
            print(message)             
    def choose(self):
        data=self.prep_call() if self.prep_call else None
        message=self.command.execute(data) if data else self.command.execute()
        self._handle_message(message)

    def str(self):
        return self.name
def clear_screen():
    clear='cls' if os.name=='nt' else 'clear'
    os.system(clear)
def print_options(options):
    for shortcut,option in options.items():
        print(f'({shortcut})--{option}')       
    print()
def option_choice_is_valid(choice,options):
    return choice in options or choice.upper() in options              
def get_option_choice(options):
    choice=input('Choose an option')
    while not option_choice_is_valid(choice,options):
        print('invalid choice')
        choice=input('choose an option')
    return options[choice.upper()]    
def get_user_input(label,required=True):
    value=input(f'{label}:') or None
    while required and not value:
        value=input(f'{label}: ') or None
    return value    
def get_new_bookmark_data():
    return{
        'title':get_user_input('Title'),
        'url':get_user_input('URL'),
        'notes':get_user_input('Notes',required=False),
    }    
def get_bookmark_id_for_deletion():
    return get_user_input('Enter a bookmark Id for deletion')

def loop():
    clear_screen()
    options=OrderedDict({
        'A':Option('Add a Bookmark',commands.AddBookmarkCommand(),prep_call=get_new_bookmark_data),
        'B':Option('List Bookmarks by Date',commands.ListBookmarksCommand()),
        'T':Option('List BookMark by Title',commands.ListBookmarksCommand(order_by='title')),
        'D':Option('Delete a BookMark',commands.DeleteBookmarkCommand(),prep_call=get_bookmark_id_for_deletion),
        'Q':Option('Quit',commands.QuitCommand()), 
    })
    print_options(options)
    chosen_option=get_option_choice(options)
    clear_screen()
    chosen_option.choose()
    _=input('Press Enter to return to Menu') 
if __name__=='__main__':
    commands.CreateBookmarksTableCommand().execute()
    while True:
        loop()











