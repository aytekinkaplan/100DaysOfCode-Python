# Tip Calculator

print("Welcome to the Tip Calculator!")

totalBill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

totalBillWithTip = totalBill * (1 + percentage / 100)

billPerPerson = totalBillWithTip / people
finalBill = "{:.2f}".format(billPerPerson)

print(f"Each person should pay: ${finalBill}")