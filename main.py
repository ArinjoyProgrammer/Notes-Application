import json
import sys



# Briefs about us
def welcome():
    msg = "Welcome to Arinjoy's Notes Application\nHere you can store your notes for your future work!"

    print(msg)

def aboutUs():
    about = "This is our Notes Application made by Arinjoy Nath!\nVersion 1.0.0-alpha\n\nAbout Us:\nWe make your life easier by storing your important Notes in your Personal Computer! At this time you can access/store only ONE NOTE and you cannot store MULTIPLE NOTES at a time. But we will soon create this feature and make this app more better than the old!\n\nThanks for Reading\nRegards, Arinjoy"

    print(about)




def showNotes():
    # print("this show notes")

    with open('notes.json', 'r') as f:
        data = json.load(f)

        print(data["notes"])


def writeNotes():
    # print("this is write notes")

    typeNote = input("Type your note below to store\n\n")

    with open("notes.json", 'r') as f:
       data = json.load(f)

       data["notes"] = typeNote

    with open('notes.json', 'w') as f:
        json.dump(data, f)

        updateMsg = "\n\nUPDATE MESSAGE - Your Notes has been updated!"
        print(updateMsg)





while True:
    user = input("\nWhat you want to do? Ex - write, show, about us, exit\n> ")


    # Conditional Statements for the user
    if user == "write".lower():
        writeNotes()
    elif user == 'show'.lower():
        showNotes()
    elif user == "about us".lower():
        aboutUs()
    elif user == "exit".lower():
        print("Thanks for using our Notes Application! We hope that you will use it again!")
        sys.exit()
    else:
        print("Your value is not correct!")

