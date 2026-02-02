import os
import json

def load_list():
    print("====Contact Book====")
    lists = os.listdir('./contact_lists')
    for i in range(0, len(lists)):
        print(f"{i + 1}. {os.path.splitext(lists[i])[0]}")
    print("-" * 8)
    list_name = input("Choose book name,\nor enter new name to create one more: ")
    if list_name + '.json' in lists:
        with open(f'./contact_lists/{list_name}.json') as f:
            data = json.load(f)
            return data
    with open(f'./contact_lists/{list_name}.json', 'w') as f:
        json.dump([], f)
    return []

def main_menu():
    print("\n" * 100)
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
            add_contact()
        case '2':
            find_contact()
        case '3':
            show_list()
        case '4':
            delete_contact()
        case '5':
            edit_contact()
        case '6':
            exit()
        case _:
            main_menu()

def save_list():
    pass
def add_contact():
    pass
def show_list():
    pass
def find_contact():
    pass
def delete_contact():
    pass
def edit_contact():
    pass

load_list()
main_menu()