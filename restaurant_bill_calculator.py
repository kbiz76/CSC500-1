# Part 1: Restaurant Bill Calculator

# Pseudocode
#1. Prompt to enter the charge for the food.
#2. Calculate the tip amount as 18%.
#3. Calculate the tax amount as 7%.
#4. Calculate the total amount as the sum of the food charge, tip amount, and tax amount.
#5. Print the output of the food charge, tip amount, tax amount, and total amount.

# Source Code

# prompt to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# calculate the tip amount (18%), tax amount (7%), total amount
#https://docs.python.org/3/library/operator.html#operator-arithmetic
tip_amount = food_charge * 0.18
tax_amount = food_charge * 0.07
total_amount = food_charge + tip_amount + tax_amount

# print the amounts
#https://docs.python.org/3/library/string.html#format-string-syntax
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip Amount (18%): ${tip_amount:.2f}")
print(f"Tax Amount (7%): ${tax_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")

