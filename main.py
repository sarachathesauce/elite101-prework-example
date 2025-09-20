print("Welcome to the FTC I:SO chatbot!")
name = input("What is your name?")
age = input( name + ", How old are you?")
print("Oh, to be "+ age +"again!")
print("How can I help you today," + name + "?")

#options:
while True:
  print("1. See a team's stats")
  print("2. Check the latest match in a league")
  print("3. Check a match's score")
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
