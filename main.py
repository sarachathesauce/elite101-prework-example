print("Welcome to Sarah's Restaurant!")
name = input("What is your name?")
print("How can I help you today," + name + "?")

#options:
while True:
  print("\n  Main Menu   ")
  print("1. View Menu")
  print("2. View Today's Specials")
  print("3. Place an Order")
  print("4. Make a Reservation")
  print("4. Exit")
  
  choice = input("Please select an option from 1-4:")

  if choice == "1":
    print("Option 1: Still in development!")
  elif choice == "2":
    print("Option 2: Still in development!")
  elif choice == "3":
    print("Option 3: Still in development!")
  elif choice == "4":
    print("Alright then, Goodbye," + name + "!")
    break
