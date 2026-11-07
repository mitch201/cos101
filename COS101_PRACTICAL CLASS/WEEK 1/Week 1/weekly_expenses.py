#Student weekly expense calculator
#This program calculates a students total expenses for the week.
#input
name=input("Student Name:")
daily_transport_cost = float(input("Daily Transport Cost:"))
daily_feeding_cost = float(input("Daily Feeding cost:"))
days=int(input("Days on campus:"))
other_weekly_expenses=float(input("Other_Weekly_Expenses:"))


#process
transport_total=daily_transport_cost * days
feeding_total=daily_feeding_cost * days
weekly_total=transport_total + feeding_total + other_weekly_expenses

#output
print("\n====Weekly Expense summary")
print("Student Name:",name)
print(f"Transport Total:#{transport_total:.2f}")
print(f"Feeding total:#{feeding_total:.2f}")
print(f"Other Weekly Expenses:#{other_weekly_expenses:.2f}")
print(f"Weekly Total:#{weekly_total:.2f}")
      
      
      
    
