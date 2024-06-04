class ItemToPurchase:
  item_name = "none"
  item_price = 0
  item_quantity = 0

  #class to print the item cost
  def print_item_cost(self):
    total_cost = self.item_price * self.item_quantity
    print(f'{self.item_name} {int(self.item_quantity)} @ ${self.item_price:.2f} = ${total_cost:.2f}')

items = []
num_items = int(input("Enter the number of items: "))

#loop the number of items entered to acquire item name,price, and quatity for number of items
for i in range(num_items):
  print(f"\nItem {i+1}")
  item = ItemToPurchase()
  item.item_name = input("Enter the item name:\n")
  item.item_price = float(input("Enter the item price:\n"))
  item.item_quantity = float(input("Enter the item quantity:\n"))
  items.append(item)

print("\nTOTAL COST")
total_cost = 0
#loop through items to print item cost and determine total cost
for item in items:
  item.print_item_cost()
  total_cost += item.item_price * item.item_quantity

#print total cost
print(f'Total: ${total_cost:.2f}')
