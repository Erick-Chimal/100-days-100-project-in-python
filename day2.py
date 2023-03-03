# day 2 Tip Calculator and time left if you live to 90


age = int(input("What is your current age? "))
years_remaining = 90 - age
x = years_remaining * 365 
y = years_remaining * 52
z = years_remaining * 12
print(f"You have {x} days, {y} weeks, and {z} months left. ")

welcome_mssg = "Tip Calculator"
center = welcome_mssg.center(100, " ")
print(center)
bill = float(input("What was the the total bill? $"))
tip = int(input("How much tip do you want to give 10, 12 or 15? "))
people = int(input("how many people to split the bill? "))
tip_as_percantage = tip / 100
total_tip_amount = bill * tip_as_percantage
total_bill =  bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = float(round(bill_per_person, 2))
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should play: ${final_amount}")
