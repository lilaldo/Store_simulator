import json

with open('storegrocerys.json', 'r') as file:
    groceries_data = json.load(file)

class Store:
    def __init__(self):
        self.shopping_cart = []

    def picking_groceries(self, item_name):
        price = print(f"Total price: {groceries_data['Price']}")
        self.pick = input("what would you like to add to the shopping-cart? ")
        return self.pick


store = Store()

# Print the available groceries
# print("Available groceries:")
# for item in groceries_data:
#    print(f"{item['Item']}: ${item['Price']:.2f}")

while True:
    items = store.picking_groceries()
    if any(items.lower() == grocery['Item'].lower() for grocery in groceries_data):
        store.shopping_cart.append(items)
        print(f"{store.shopping_cart[-1]} added to cart.".title())
    else:
        print("Item not available. Please choose from the available groceries.")