#!/usr/bin/env python3

##This will be a python script that creates a command line journal

from datetime import datetime

the_date = []
the_entry = []
create_option = ["C", "c"]
open_option = ["O", "o"]
exit_option = ["X", "x"]

get_date = datetime.now()

def create_entry():
    '''Gets inputs from user, appends it to a text file and reloads the menu'''
    global get_date
    get_entry = input("What's on your mind?: ")
    the_entry.append(get_entry)
    entry = ''.join(the_entry)

    with open('Journal.txt', 'a') as journal:
        print(get_date.strftime("%x"), entry, file=journal)
    menu()

def open_journal():
    with open('Journal.txt') as open_journal:
        for j_entry in open_journal:
            print(j_entry)
    menu()

def menu():
    global get_date
    print("Hello, Today is ", get_date.strftime("%x"), ".")
    menu = input("To create a new journal entry type 'C', To open your journal type 'O', to exit type 'X': ")
    if menu in create_option:
        create_entry()
    elif menu in open_option:
        open_journal()
    elif menu in exit_option:
        exit
    else:
        print("Please type 'C' or 'O' :")
        menu()

menu()