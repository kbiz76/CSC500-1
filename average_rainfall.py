num_years = int(input("Enter the number of years: "))

total_rainfall = 0
total_months = 0

for year in range(1, num_years + 1):
    print(f"Year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
    total_months += 12

average_rainfall = total_rainfall / total_months

print(f"\nTotal number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
