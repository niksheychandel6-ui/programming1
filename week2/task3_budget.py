MonthlyIncome=float(input("Enter your monthly income:"))
Rent=float(input("Enter your rent:"))
Transportcost=float(input("Enter your transport cost:"))
Foodcost=float(input("Enter your food cost:"))
Entertainmentcost=float(input("Enter your entertainment cost:"))
Totalexpense=Rent+Transportcost+Foodcost+Entertainmentcost
RemainingBalance=MonthlyIncome-Totalexpense
print("-----Monthly Budget Calculator-----")
print("Total Expense:",Totalexpense)
print("Remaining Balance:",RemainingBalance)
print("-------------------------")
