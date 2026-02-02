import os
import json
from os.path import exists

list_name = ""
def load_list():
    print("====Contact Book====")
    lists = os.listdir('./contact_lists')
    for i in range(0, len(lists)):
        print(f"{i + 1}. {os.path.splitext(lists[i])[0]}")
    print("-" * 8)
    global list_name
    list_name = input("Choose book name,\nor enter new name to create one more: ")
    if list_name + '.json' in lists:
        with open(f'./contact_lists/{list_name}.json') as f:
            data = json.load(f)
            return data
    with open(f'./contact_lists/{list_name}.json', 'w') as f:
        json.dump([], f)
    return []

def main_menu(l):
    clear()
    user_choice = input(f"""
====Contact Book====
1. Add new contact
2. Find contact
3. Show contact list
4. Delete contact
5. Edit contact
6. EXIT
{'-' * 8}
CHOOSE OPTION: 
""")

    match user_choice:
        case '1':
            add_contact(l)
        case '2':
            find_contact(l)
        case '3':
            show_list(l)
        case '4':
            delete_contact(l)
        case '5':
            edit_contact(l)
        case '6':
            exit()
        case _:
            main_menu(l)

#help methods
def clear():
    print('\n' * 100)
def save_list(l):
    with open(f'./contact_lists/{list_name}.json', 'w') as f:
        json.dump(l, f)
def find(l, name):
    for x in l:
        if x["name"] == name:
            return x
    return None

#

def add_contact(l):
    clear()
    print("=" * 20)
    name = input("Enter name: ")
    exist = find(l, name)
    if not exist:
        print("=" * 20)
        phon = input("Enter phon number: ")
        l.append({"name": name, "phon": phon})
        l.sort(key = lambda x: x["name"])
        save_list(l)
    else:
        print("Contact already exist!")
        input("Press ENTER to continue")
    main_menu(l)
def show_list(l):
    clear()
    print("=" * 20)
    for i in range(len(l)):
        print(f"{i + 1}. {l[i]["name"]} - {l[i]["phon"]}")
        print("=" * 20)
    if not l:
        print("List is empty!")
        print("=" * 20)
    input("Press ENTER to continue")
    main_menu(l)
def find_contact(l):
    clear()
    print("=" * 8)
    name = input("Enter name to search: ")
    x = find(l, name)
    if x:
        print("-" * 8)
        print(f"{x["name"]} - {x["phon"]}")
        print("-" * 8)
        input("Press ENTER to continue")
        main_menu(l)
    else:
        print("Contact name was not found!")
        input("Press ENTER to continue")
        main_menu(l)

def delete_contact(l):
    clear()
    print("=" * 8)
    name = input("Enter name contact to delete: ")
    x = find(l, name)
    if x:
        l.remove(x)
        print("-" * 8)
        print("Contact removed!")
        input("Press ENTER to continue")
        main_menu(l)
    else:
        print("=" * 20)
        print("Contact name was not found!")
        print("=" * 20)
        input("Press ENTER to continue")
        main_menu(l)

def edit_contact(l):
    clear()
    print("=" * 8)
    name = input("Enter name contact to edit: ")
    x = find(l, name)
    if x:
        print("=" * 20)
        new_name = input("name: (Press enter to save old name) ")
        print("=" * 20)
        new_number = input("phon number: (Press enter to save old number) ")
        if new_name: x["name"] = new_name
        if new_number: x["phon"] = new_number
        save_list(l)
        input("Updated! Press ENTER to continue")
        main_menu(l)
    else:
        print("=" * 20)
        print("Contact name was not found!")
        print("=" * 20)
        input("Press ENTER to continue")
        main_menu(l)

