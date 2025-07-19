# daily_reminder.py

print("Welcome to your Daily Task Reminder!")

#Prompt for a Single Task:
task = input("Enter your task:").lower()
Priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ")
#match case
match Priority :
  case "high":
    reminder = (f"High Priority Task: '{task}'")
  case "low":
    reminder = (f"Low Priority Task: '{task}'")
  case "medium":
    reminder = (f"Medium priority Task: '{task}'")
  case _:
    reminder = (f"Invalid priority")
if time_bound == "yes":
  reminder += "it requires immediate attention today!"
else:
  reminder == "Take your time but make sure it is completed today"
  print(reminder)

