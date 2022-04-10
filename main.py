import json
import sys



# Briefs about us
def welcome():
    msg = "Welcome to Arinjoy's Notes Application\nHere you can store your notes for your future work!"

    print(msg)

def aboutUs():
    about = "This is our Notes Application made by Arinjoy Nath!\nVersion 1.1.0-alpha\n\nAbout Us:\nWe make your life easier by storing your important Notes in your Personal Computer! At this time you can access/store only ONE NOTE and you cannot store MULTIPLE NOTES at a time. But we will soon create this feature and make this app more better than the old!\n\nThanks for Reading\nRegards, Arinjoy"

    print(about)


# Rules
def rules():
    rules = ""

    print(rules)




def showNotes():
    # print("this show notes")

    with open('notes.json', 'r') as f:
        data = json.load(f)

    print("\nList of Notes which you have been stored:")
    for dicts in data:
        print(f"> {dicts}")

    showDictValue = input(f"\nWhich Note you want to see? Type one of the Note Name which are shown above\n> ")

    with open('notes.json', 'r') as f:
        data = json.load(f)

        print(data[f"{showDictValue}"])


def writeNotes():
    # print("this is update notes")

    notesName = input("\nWhat will be the name of your notes?\n> ")
    print(f"\nYour Note Name is selected as {notesName}\n")

    with open('notes.json', 'r') as f:
        data = json.load(f)

    with open('notes.json', 'w') as f:
        typeAnotherNote = input("Now type your note!\n> ")

        data[f"{notesName}"] = typeAnotherNote

        json.dump(data, f)


while True:
    user = input("\nWhat you want to do? Ex - write, show, about us, rules, exit\n> ")


    # Conditional Statements for the user
    if user == "write".lower():
        writeNotes()
    elif user == 'show'.lower():
        showNotes()
    elif user == "about us".lower():
        aboutUs()
    elif user == "rules".lower():
        rules()
    elif user == "exit".lower():
        print("Thanks for using our Notes Application! We hope that you will use it again!")
        sys.exit()
    else:
        print("Your choice is not correct! Try again!")
