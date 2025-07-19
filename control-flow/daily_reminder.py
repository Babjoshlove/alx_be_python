# daily_reminder.py

print("Welcome to your Daily Task Reminder!")

#Prompt for a Single Task:
task = input("Enter your task:").lower()
Priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ")
#match case
match Priority :
  case "high":
    Reminder = (f"High Priority Task: '{task}'")
  case "low":
    Reminder = (f"Low Priority Task: '{task}'")
  case "medium":
    Reminder = (f"Medium priority Task: '{task}'")
  case _:
    Reminder = (f"Invalid priority")
if time_bound == "yes":
  Reminder += "it requires immediate attention today!"
else:
  Reminder += "Consider completing it when you have free time."
  print(Reminder)

