#####
#Part 1: Average Rainfall calculation
#Pseudocode
#1. Ask the user for the number of years to calculate rainfall for
#2. Initialize total_rainfall and total_months variable
#3. Create a month array
#4. Create an outer loop to iterate through the years 
#5. Create an inner loop to iterate each month
#6. For every month as the user for the total_rainfall for the month
#7. Calculate the total_months
#8. Calculate the average_rainfall
#9. Display the total number of months, total rainfall, and average rainfall per month
#####
#number of years to calculate
num_years = int(input("Enter the number of years to calculate: "))

total_rainfall = 0
total_months = 0
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#loop through the number of years and then loop through the number of months in that year
for year in range(1, num_years + 1):
    print(f"<== Year {year} ==>")
    for month in range(12):
        rainfall = float(input(f"In year {year} enter the inches of rainfall for {months[month]}: "))
        total_rainfall += rainfall
    total_months += 12

#calculate average rainfall
average_rainfall = total_rainfall / total_months

print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
