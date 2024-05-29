meal_plan = ["Fried Rice", "Salmon Ceasar Salad", "Spaghetti", "Pizza", "Fish and Chips", "Burger", "Tacos"]

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(meal_plan)):
  print(f"{days_of_week[i]}: {meal_plan[i]}")

#changed my mind for a meal for Thursday

meal_plan[3] = "Korean BBQ"

print("\nUpdated meal plan for Thursday:")

print(f"Thursday: {meal_plan[3]}")
