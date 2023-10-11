import json

with open('storegrocerys.json', 'r') as file:
    groceries_data = json.load(file)

class Store:
    def __init__(self):
        self.shopping_cart = []  # Empty list which simulates the shopping cart.

    def picking_groceries(self, item_name):
        for item in groceries_data:  # Call the groceries:
            if item['Item'].lower() == item_name.lower():   # Key item == item_name
                self.shopping_cart.append(item)  # Adds the groceries to the shopping card
                print(f"{item_name.title()} added to cart! ")
                break

        else:  # If item not in JSON-file.
            print(f"The store seem to be out of {item_name}")

    def calculate_total_price(self):
        # total_price = sum of item ['Price'] for item in func.
        total_price = sum(item['Price'] for item in self.shopping_cart)
        return total_price

    def check_reciept(self):
        if user_choice == 'check' or 'reciept'.lower():
            print(self.shopping_cart)

    def checkout(self):
        pass

store = Store()

while True:
    user_choice = input("What would you like to add to the shopping cart (or 'done' to finish)? ".lower())
    print(*store.shopping_cart, sep=', ')
    if user_choice == 'done':
        break
    store.picking_groceries(user_choice)

total_price = store.calculate_total_price()
print(f"Total price for your shopping cart: ${total_price:.2f}")