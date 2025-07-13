#prompt users to enter their monthly income
monthly_income = int(input("Enter your monthly income"))
#prompt users to enter their expenses
monthly_expenses = int(input("Enter your total monthly expenses"))
#calculate 
monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12) + ((monthly_savings) * 12 * 0.05)
print(f"Your monthly savings are {monthly_savings}")
print(f"Projected savings after one year, with interest {projected_savings}")