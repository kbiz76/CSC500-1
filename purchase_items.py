class ItemToPurchase:
  item_name = "none"
  item_price = 0
  item_quantity = 0

  #class to print the item cost
  def print_item_cost(self):
    total_cost = self.item_price * self.item_quantity
    print(f'{self.item_name} {int(self.item_quantity)} @ ${self.item_price:.2f} = ${total_cost:.2f}')

#Create the first item
print("Item 1")
item_1 = ItemToPurchase()
item_1.item_name = input("Enter the item name:\n")
item_1.item_price = float(input("Enter the item price:\n"))
item_1.item_quantity = float(input("Enter the item quantity:\n"))

#Create the second item
print("\nItem 2")
item_2 = ItemToPurchase()
item_2.item_name = input("Enter the item name:\n")
item_2.item_price = float(input("Enter the item price:\n"))
item_2.item_quantity = float(input("Enter the item quantity:\n"))

#Print Total cost
print("\nTOTAL COST")
total_cost = 0
item_1.print_item_cost()
item_2.print_item_cost()
total_cost = (item_1.item_price * item_1.item_quantity) + (item_2.item_price * item_2.item_quantity)

#print total cost
print(f'Total: ${total_cost:.2f}')
