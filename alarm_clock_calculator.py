# Part 2: Alarm Clock Calculator

#Pseudo Code
#1. Prompt the user to enter the current time in hours (0-23).
#2. Prompt the user to enter the number of hours to wait for the alarm.
#3. Calculate the future time by adding the current time and the wait time, then taking the result modulo 24.
#4. Display the future time.

#Source Code
# Prompt the user to enter the current time in hours (0-23)
current_time = int(input("Enter the time now in hours (0-23): "))

# Prompt the user to enter the number of hours to wait for the alarm
wait_hours = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the future time
#https://docs.python.org/3/library/operator.html#operator-arithmetic
future_time = (current_time + wait_hours) % 24

# Display the future time
#https://docs.python.org/3/library/string.html#format-string-syntax
print(f"The alarm will go off at: {future_time:02d}:00")
