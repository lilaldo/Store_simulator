import json
import random
import time

with open('storegroceries.json', 'r') as file:
    groceries_data = json.load(file)


# Costumer attributes
class Me:
    pass



class Store:
    pass


# Cashier stuff
class Cashier:
    def __init__(self, name, scanning_speed):
        self.name = name
        self.scanning_speed = scanning_speed

    def cashier(self):
        print(f"Oh, {self.name} is working in the register!")

    def scanning(self, num_items):
        for items in shopping.shopping_cart:
            print(f"{self.name} is scanning {items['Item']}...")
            time.sleep(num_items / self.scanning_speed)


class Shopping:
    def __init__(self):
        self.shopping_cart = []  # Empty list which simulates the shopping cart.

    def picking_groceries(self, item_name):
        if item_name in ['check', 'cart']:  # Makes the program not to continue the function if checking the cart.
            return
        for item in groceries_data:  # Call the groceries:
            if item['Item'].lower() == item_name.lower():  # Key item == item_name
                self.shopping_cart.append(item)  # Adds the groceries to the shopping card
                print(f"{item_name.title()} added to cart! ")
                break

        else:  # If item not in JSON-file.
            print(f"The store seem to be out of {item_name}")

    def calculate_total_price(self):
        # total_price = sum of item ['Price'] for item in func.
        total_price = sum(item['Price'] for item in self.shopping_cart)
        return total_price

    def check_cart(self):
        # Only show the item, cause you cant remember all the prices, can you?
        cart_items = [item['Item'] for item in self.shopping_cart]
        cart_items_str = ', '.join(cart_items)  # Converts cart dict to readable string-variable.
        print(f"Your cart contains {cart_items_str}")
        return

    def checkout(self):
        print("Goes to checkout. . .")
        line = random.randint(1, 10)
        if line == 1:
            print(f"Oh theres {line} costumer before me...")
        else:
            print(f"Oh theres {line} costumer before me...")
            time.sleep(line / 2)
            print("Still standing in line... *Checking phone*")
            time.sleep(line / 2)
            print("Oh its my turn! ")
            return


cashiers = [
    Cashier("Jessica", 2.0),
    Cashier("Pedro", 3.0),
    Cashier("Brian", 0.6),
    Cashier("André", 1.0)
]

shopping = Shopping()


while True:
    shopper = input("What would you like to add to the shopping cart (or 'done' to finish)? ".lower())
    if shopper == 'cart':
        shopping.check_cart()
    elif shopper == 'done':
        standing_cashier = random.choice(cashiers)
        shopping.checkout()
        standing_cashier.cashier()
        standing_cashier.scanning(len(shopping.shopping_cart))
        break
    else:
        shopping.picking_groceries(shopper)

total_price = shopping.calculate_total_price()
print(f"Total price for your shopping cart: ${total_price:.2f}")
cash_card = input("Would you like to pay with cash or card? ")
#if cash_card == 'Cash'.lower():

