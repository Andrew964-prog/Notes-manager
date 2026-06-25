import os


if not os.path.exists("Note"):
    os.mkdir("Note")

# Create Note Function
def create_note():

    Note_Name = input("\nEnter Note Name => ").strip().upper()
    path = os.path.join("Note", (Note_Name + ".txt"))
    if os.path.exists(path):
        print("This Note Is Already Exist\n")
        return
    
    with open(path, "w") as file:
        Note_Text = input("Enter Your Note Text => ").strip().lower()
        file.write(Note_Text)
        print("Note Created Successfully\n")


# Read Note Function
def read_note():
    
    Note_Name = input("\nEnter Note Name => ").strip().upper()
    try:
        path = os.path.join("Note", (Note_Name + ".txt"))
        with open(path, "r") as file:
            content = file.readlines()

        print("--- Note Content ---\n")

        for i, c in enumerate(content, start=1):
            print(f"{i}- {c}")

        print("-" * 15)
        print("\n")

    except FileNotFoundError:
        print("File Was Not Found")
    except Exception:
        print("Unexpected Error")


# Delete Note Function
def delete_note():

    Note_Name = input("Enter Note Name => ").strip().upper()
    try:
        path = os.path.join("Note", (Note_Name + ".txt"))
        os.remove(path)
        print("Deleted Successfully\n")
    except FileNotFoundError:
        print("This Note Was Not Found\n")
    except Exception:
        print("Unexpected Error")


# Show All Notes Function
def show_notes():
    notes = os.listdir("Note")
    
    if not notes:
        print("There Is No Notes Yet\n")
        return
    
    for i, n in enumerate(notes, start=1):
        print(f"{i}- {n.removesuffix(".txt")}")


# Search Note Function
def search_note():
    
    notes = os.listdir("Note")

    if not notes:
        print("There Is No Notes Yet\n")
        return
    
    while True:
        Note_Name = input("Enter Note Name => ").strip().upper()

        for i in notes:
            if Note_Name == i.removesuffix(".txt"):
                print("Note Was Found")
                print(Note_Name)
                return

        print("Was Not Found\n")
        continue


# Edit Note Function
def edit_note():

    notes = os.listdir("Note")

    if not notes:
        print("There Is No Notes Yet\n")
        return
    
    Note_Name = input("Enter Note Name => ").strip().upper()
    path = os.path.join("Note", (Note_Name + ".txt"))

    try:
        with open(path, "r") as file:
            content = file.readlines()


        print("\nContent :\n")

        for i, c in enumerate(content, start=1):
            print(f"{i}- {c.strip()}")

        while True:
            try:
                line = int(input("Enter A Number Of Line You Want To Edit => "))

                if line <= 0 or line > len(content):
                    print(f"Must Be Between 1 To {len(content)}\n")
                    continue

                new_text = input("Enter New Text => ").strip().lower()

                content[line-1] = (new_text + "\n")

                with open(path, "w") as file:
                    file.writelines(content)
                    print("Note Updated Successfully\n")
                    return

            except ValueError:
                print("You Must Enter A Line Number\n")
                continue

    except FileNotFoundError:
        print("Note Was Not Found\n")




# Add Text Function
def add_text():
    
    notes = os.listdir("Note")

    if not notes:
        print("There Is Not Notes Yet\n")
        return
    
    Note_Name = input("Enter Note Name => ").strip().upper()

    try:
        path = os.path.join("Note", (Note_Name + ".txt"))
        with open(path, "r") as file:
            content = file.read()

        print("Cureent Note Content : ")
        print(content)

        new_text = input("\nEnter New Text => ").strip().lower()

        with open(path, "a") as file:
            file.write("\n" + new_text)
            print("Added Successfuly\n")

    except FileNotFoundError:
        print("This Note Was Not Found\n")



# Delete Line Function
def delete_line():
    
    notes = os.listdir("Note")

    if not notes:
        print("There Is No Notes Yet\n")
        return
    
    Note_Name = input("Enter Note Name => ").strip().upper()

    try:
        path = os.path.join("Note", (Note_Name + ".txt"))
        with open(path, "r") as file:
            content = file.readlines()

        print("\nCurrent Note Content : \n")
        for i , c in enumerate(content, start=1):
            print(f"{i}- {c.strip()}")

        print("-" * 15)
        
        while True:
            
            try:
                line = int(input("Choose Line To Delete => "))

                if line <= 0 or line > len(content):
                    print(f"Must Be Between 1 To {len(content)}")
                    continue

                for i , c in enumerate(content, start=1):
                    if line == i:
                        while True:
                            dicision = input("Are You Sure You Want To Delete This Line ? (y/n)").strip().lower()
                            if dicision == 'y':
                                del content[line-1]
                                print("Line Deleted Successfully\n")
                                break
                            elif dicision == 'n':
                                print("Ok\n")
                                return
                            else:
                                print("Invalid Dicision\n")
                                continue


            except ValueError:
                print("You Must Enter A number")
                continue

            with open(path, "w") as file:
                file.writelines(content)
                return

                
    except FileNotFoundError:
        print("This Note Was Not Found")


while True:
    print("\nMENU :\n")
    print("(1) Create Note")
    print("(2) Read Note")
    print("(3) Delete Note")
    print("(4) Show All Notes")
    print("(5) Search Note")
    print("(6) Add Text To Note")
    print("(7) Edit Note")
    print("(8) Delete Specific Line")
    print("(9) Exit")

    try:
        choose = int(input("Choose An Operation => "))
        
        match choose:
            case 1:
                create_note()
            case 2:
                read_note()
            case 3:
                delete_note()
            case 4:
                show_notes()
            case 5:
                search_note()
            case 6:
                add_text()
            case  7:
                edit_note()
            case 8:
                delete_line()    
            case 9:
                print("Good Bye")
                break
            case _:
                print("Invalid Option")
    except ValueError:
        print("\nInvalid Option")
        print("Must Enter An Integer\n")