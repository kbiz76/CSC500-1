class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                total = item.price * item.quantity
                print(f"{item.name} {item.quantity} @ ${item.price:.2f} = ${total:.2f}")
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu(cart):
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option:"
    )
    while True:
        print(menu)
        option = input().strip()
        if option == 'q':
            break
        elif option == 'a':
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        elif option == 'r':
            name = input("Enter the name of the item to remove:\n")
            cart.remove_item(name)
        elif option == 'c':
            name = input("Enter the item name:\n")
            description = input("Enter the new description (or 'none' to leave unchanged):\n")
            price = float(input("Enter the new price (or 0 to leave unchanged):\n"))
            quantity = int(input("Enter the new quantity (or 0 to leave unchanged):\n"))
            item = ItemToPurchase(name, description, price, quantity)
            cart.modify_item(item)
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        else:
            print("Invalid option. Please choose again.")

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print(f"\nCustomer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()

