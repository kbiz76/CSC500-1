class ItemToPurchase:
    name = "none"
    description = "none"
    price = 0
    quantity = 0

class ShoppingCart:
    customer_name = "none"
    current_date = "January 1, 2020"
    cart_items = []

    def add_item(item):
        ShoppingCart.cart_items.append(item)

    def remove_item(item_name):
        found = False
        for item in ShoppingCart.cart_items:
            if item.name == item_name:
                ShoppingCart.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(item):
        found = False
        for cart_item in ShoppingCart.cart_items:
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

    def get_num_items_in_cart():
        total_quantity = 0
        for item in ShoppingCart.cart_items:
            total_quantity += item.quantity
        return total_quantity

    def get_cost_of_cart():
        total_cost = 0
        for item in ShoppingCart.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    def print_total():
        print(f"{ShoppingCart.customer_name}'s Shopping Cart - {ShoppingCart.current_date}")
        print(f"Number of Items: {ShoppingCart.get_num_items_in_cart()}")
        if not ShoppingCart.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in ShoppingCart.cart_items:
                total = item.price * item.quantity
                print(f"{item.name} {item.quantity} @ ${item.price:.2f} = ${total:.2f}")
            print(f"Total: ${ShoppingCart.get_cost_of_cart():.2f}")

    def print_descriptions():
        print(f"{ShoppingCart.customer_name}'s Shopping Cart - {ShoppingCart.current_date}")
        print("Item Descriptions")
        for item in ShoppingCart.cart_items:
            print(f"{item.name}: {item.description}")

def print_menu():
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
            item = ItemToPurchase()
            item.name = input("Enter the item name:\n")
            item.description = input("Enter the item description:\n")
            item.price = float(input("Enter the item price:\n"))
            item.quantity = int(input("Enter the item quantity:\n"))
            ShoppingCart.add_item(item)
        elif option == 'r':
            name = input("Enter the name of the item to remove:\n")
            ShoppingCart.remove_item(name)
        elif option == 'c':
            item = ItemToPurchase()
            item.name = input("Enter the item name:\n")
            item.description = input("Enter the new description (or 'none' to leave unchanged):\n")
            item.price = float(input("Enter the new price (or 0 to leave unchanged):\n"))
            item.quantity = int(input("Enter the new quantity (or 0 to leave unchanged):\n"))
            ShoppingCart.modify_item(item)
        elif option == 'i':
            ShoppingCart.print_descriptions()
        elif option == 'o':
            ShoppingCart.print_total()
        else:
            print("Invalid option. Please choose again.")

ShoppingCart.customer_name = input("Enter customer's name:\n")
ShoppingCart.current_date = input("Enter today's date:\n")
print(f"\nCustomer name: {ShoppingCart.customer_name}")
print(f"Today's date: {ShoppingCart.current_date}")
print_menu()
