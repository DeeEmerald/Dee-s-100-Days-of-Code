#Program for Tip Calculator 
print("Welcome to Deb's Tip Calculator")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 4? 8? 12?\n"))
people = int(input("How many people are sharing the bill?\n"))
tip_as_percent = tip / 100
tip_amount = bill * tip_as_percent
total_bill = bill + tip_amount
print(total_bill)
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 3)
final_amount = "{:.3f}".format(bill_per_person)
print(f"Each person pays - £{final_amount}")
print("Thank you for calculating with Deb's Tip Calculator")