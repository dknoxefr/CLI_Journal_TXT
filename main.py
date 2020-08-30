#!/usr/bin/env python3

##This will be a python script that creates a command line journal

the_date = []
the_entry = []
create_option = ["C", "c"]
open_option = ["O", "o"]
exit_option = ["X", "x"]

def create_entry():
    '''Gets inputs from user, appends it to a text file and reloads the menu'''
    get_date = input("What is today's date (mm-dd-yy): ")
    the_date.append(get_date)
    dizzy = ''.join(the_date)

    get_entry = input("What's on your mind?: ")
    the_entry.append(get_entry)
    entry = ''.join(the_entry)

    with open('Journal.txt', 'a') as journal:
        print(dizzy, entry, file=journal)
    menu()

def menu():
    menu = input("To create a new journal entry type 'C', To open your journal type 'O', to exit type 'X': ")
    if menu in create_option:
        create_entry()
    elif menu in open_option:
        with open('Journal.txt') as open_journal:
            for j_entry in open_journal:
                print(j_entry)
    elif menu in exit_option:
        exit
    else:
        print("Please type 'C' or 'O' :")
        menu()

menu()