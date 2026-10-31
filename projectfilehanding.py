from datetime import datetime
import os
print("welcome to the personal journal manager")
while True:
    print("please select an option\n")
    print("1. Add entry")
    print("2. View all Entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Exit ")
    v=int(input("User input :\n"))
    if v == 1:
        entry=input("Enter your journal entry:\n")
        time=datetime.now()
        
        with open("data.txt","a") as file:
            file.write(entry + "\n")
            print("[" + str(time) + "]")
        print("Entry added sucessfully")
    elif v == 2:
        with open("data.txt","r") as file:
            file.seek(0)
            data=file.read()
            if data:
                print("Your journal entries: ")
                print("--------------------------------")
                print(data)               
            else:
                print("no journal entries found. start entry by adding a new entry!")
    elif v == 3:
         keyword = input("Enter a keyword or date to search: ")

         found = False

         if os.path.exists("data.txt"):
          with open("data.txt", "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True

          if not found:
            print("No entries found for:", keyword)

          else:
           print("No journal entries found!")
    elif v == 4:

        if os.path.exists("data.txt"):

            confirm = input("Are you sure you want to delete all entries? (yes/no): ")

            if confirm.lower() == "yes":
                os.remove("data.txt")
                print("All journal entries have been deleted.")

            else:
                print("Deletion cancelled!")

        else:
            print("No journal entries to delete.")
    elif v == 5:
        print("thank you using for personal journal manager, goodbye!")
        break

    else:
        print("fooled")