class SushiMenu:
    #defines a class for sushi menu to store menu items
    def __init__(self):
        #init initializes the object, self refers to the menu items

        self.menu_items = {
            #creates a list of menu items, self.menu_items makes it so that each
            #item belongs to the list so that other functions like display menu can access
          # item name - string
          # item price - float
            "California Roll": 8.99,
            "Spicy Tuna Roll": 9.99,
            "Salmon Nigiri": 7.99,
            "Shrimp Tempura Roll":10.99,
            "Avocado Roll": 6.99,
            "Mochi Ice Cream": 4.99
        }
# DISPLAY THE MENU:
    def display_menu(self):
        #function to print the menu to the screen
        print("\nSushi Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")
        # loops over each item and price pair in the menu items and prints
        # :.2f gives 2 decimals at the end of the price
# GET ITEM VALUE:
    def get_price(self, item_name):
        # looks up item name in the menu
        return self.menu_items.get(item_name, None)
        # returns the item name if found but if not then returns nothing

    

# CHATBOT STARTS HERE:
print("Welcome to Sarah's Sushi Restaurant!")
name = input("What is your name?")
# input prompts for name and then uses name to greet user
print("How can I help you today," + name + "?")

menu = SushiMenu()
# sets up menu_items dictionary

#options:
while True:
    print("\n  Main Menu   ")
    print("1. View Menu")
    print("2. Place an Order")
    print("3. Make a Reservation")
    print("4. Exit")
  
    choice = input("Please select an option from 1-4:")
    # infinite loop that shows the main menu of options till exit
    # choice prompts menu option

    if choice == "1":
        print("Our Menu:")
        menu.display_menu()
        # calls function menu.display to print all menu items & prices

    elif choice == "2":
        order_total = 0
        order_list = []
        print("Please enter the the items you'd like!")
        print("(Type 'done' when finished)")
        menu.display_menu()
        # initializes order total aka the sum & order list aka items chosen
        # shows menu again to prompt order

        while True:
            item = input("Enter an item name: ")
            if item.lower() == "done":
                break
        # loops accepting item name until user types done
        # i added item.lower() to make the 'done' not case sensitive

            price = menu.get_price(item)
            # looks up the price
            if price:
                #if there is a price,adds item to the chosen items and adds price to order sum
                order_list.append(item)
                order_total += price
                print(f"Added {item} to your order. Current total: ${order_total:.2f}")
           # if no price because the item you selected isn't on the menu list, tells user item not found
            else:
                print("Sorry, that's not on the menu..")


        # checks if there is an order existing (greater than 0) if not says nothing ordered
        # if yes, asks for pickup or delivery, not case sensitive, if delivery adds $5
        if order_total > 0:
            print("\nWould you like pickup or delivery?")
            delivery_type = input("Enter 'pickup' or 'delivery': ").lower()

            if delivery_type == "delivery":
                delivery_fee = 5.00
                order_total += delivery_fee
                print(f"Delivery fee of ${delivery_fee:.2f} added.")

            print(f"Your final order total is: ${order_total:.2f}")
            print("Thanks for ordering! It'll be ready soon.")
        else:
            print("Nothing ordered.")

    # collects input for dates, times, and number of guests
    # f string to print confirmation of reservation
    # could add editable validation for improvements
    elif choice == "3":
        print("\n Making a Reservation:")
        date = input("Enter Date (Mon DD):")
        time = input("Enter time (0:00 PM):")
        guests = input("How many guests? Number answer please!")
        print(f"Thank you, {name}. We have reserved you a table: {guests} guests on {date} at {time}.")

# prints goodbye and breaks the while loop for the menu
    elif choice == "4":
        print("Alright then, Goodbye," + name + "!")
        break
# means you didn't choose an option from 1-4 and asks for a valid one
    else:
        print("Please enter a valid option from 1-4!")
