##### Module 3 Critical Thinking
##### Colorado State University Global Campus
##### csc500-1
##### Dr Jessica Schwartz 
"""""
"""# Part 1.y


#Part 2:
'''Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
Write a Python program to solve the general version of the above problem. 
Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.'''

from datetime import datetime, timedelta

# ask user if they want to use the current time or set a start time
current_time = input("Would you like to use the current time? (y/n): ").strip().lower()
if current_time == "y":
    start_time = datetime.now()
else:
    start_time = datetime.strptime(input("Enter the start time in 24-hour format (HH:MM): "), "%H:%M")

# get the number of hours to wait for the alarm
hours = float(input("Enter the amount of hours to wait for the alarm: "))
# calculate the future time
future_time = start_time + timedelta(hours=hours)
# display the future time
print("The alarm will go off on: {}".format(future_time.strftime("%Y-%B-%d at %H:%M:%S")))