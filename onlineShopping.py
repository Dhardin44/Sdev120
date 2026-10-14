class ItemToPurchase:
    """ A class that represents items to purchase """

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """ A class representing a shopping cart"""

    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                found = True
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_description()


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()


def execute_menu(choice, shopping_cart):
    if choice == 'o':
        print("OUTPUT SHOPPING CART")
        shopping_cart.print_total()

    elif choice == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        shopping_cart.print_descriptions()

    elif choice == 'a':
        print("ADD ITEM TO CART")
        item = ItemToPurchase()
        item.item_name = input("Enter the item name:\n")
        item.item_description = input("Enter the item description:\n")
        item.item_price = int(input("Enter the item price:\n"))
        item.item_quantity = int(input("Enter the item quantity:\n"))
        shopping_cart.add_item(item)

    elif choice == 'r':
        print("REMOVE ITEM FROM CART")
        name_to_remove = input("Enter name of item to remove:\n")
        shopping_cart.remove_item(name_to_remove)

    elif choice == 'c':
        print("CHANGE ITEM QUANTITY")
        item_to_modify = ItemToPurchase()
        item_to_modify.item_name = input("Enter the item name:\n")
        item_to_modify.item_quantity = int(input("Enter the new quantity:\n"))
        shopping_cart.modify_item(item_to_modify)


if __name__ == '__main__':

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    my_cart = ShoppingCart(customer_name, current_date)

    print()
    print_menu()
    user_choice = input("Choose an option:\n")

    while user_choice != 'q':
        if user_choice in ['a', 'r', 'c', 'i', 'o']:
            execute_menu(user_choice, my_cart)
            print()
            print_menu()
            user_choice = input("Choose an option:\n")
        else:
            user_choice = input("Choose an option:\n")

