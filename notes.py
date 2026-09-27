# enter = input("Enter Your Choice: ")

# if enter == "1":
#     note = input("Enter your note: ")

#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")


# elif enter == "2":
#     with open("notes.txt", 'r') as file:
#         print(file.read())









# #     print("You selected View all notes")
# # elif enter == "3":
# #     print("You selected Search notes")
# # elif enter == '4':
# #     print("You selected Exit")
# # else:
# #     print("Invalid choice")
    

while True:
    print("\n==== PERSONAL NOTES MANAGER ====")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Exit")

    enter = input("Enter your choice: ")

    if enter == "1":
        note = input("Enter your choices: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved!")

    elif enter == "2":
        print("\n==== YOUR NOTES ====")

        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

            if notes:
                print(notes)
            else:
                print("No notes available.")
        except FileNotFoundError:
            print("No notes available.")
    elif enter == "3":
        search = input("Enter word to search: ")

        try:
            with open("notes.txt", "r") as file:
                found = False

                for note in file:
                    if search.lower() in note.lower():
                        print(note, end='')
                        found = True
                if found == False:
                    print("No matching notes found.")
        except FileNotFoundError:
            print("No notes available.")
    elif enter == "4":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")


