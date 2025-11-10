class SushiMenu:
    def __init__(self):

     self.menu_items = {
        "California Roll": 8.99,
        "Spicy Tuna Roll": 9.99,
        "Salmon Nigiri": 7.99,
        "Shrimp Tempura Roll":10.99,
        "Avocado Roll": 6.99,
        "Mochi Ice Cream": 4.99
    }
    def display_menu(self):
        print("\nSushi Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")
    def get_price(self, item_name):
        return self.menu_items.get(item_name, None)