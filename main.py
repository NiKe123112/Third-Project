def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def view_notes():
   try:
     with open("notes.txt", "r") as file:
         content = file.read()
         if content:
             print("\nYour Notes:")
             print(content)
         else:
             print("No notes found.")
   except FileNotFoundError:
     print("No notes file found.")

try:
  with open("notes.txt", "r") as file:
      content = file.read()
      if content:
          print("\nYour Notes:")
          print(content)
      else:
          print("No notes found.")
except FileNotFoundError:
  print("No notes file found.")
def delete_notes():
  with open("notes.txt", "w") as file:
      pass  # clears the file
  print("All notes deleted.")

while True:
  print("\n--- Note Taker ---")
  print("1. Add a Note")
  print("2. View Notes")
  print("3. Delete All Notes")
  print("4. Exit")

  choice = input("Choose an option: ")

  if choice == "1":
      add_note()
  elif choice == "2":
      view_notes()
  elif choice == "3":
      delete_notes()
  elif choice == "4":
      print("Goodbye!")
      break
  else:
      print("Invalid choice. Try again.")
