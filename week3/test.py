account_balance=1500
amount=float(input("Enter amount to withdraw:"))

if(amount>+1500):
    print ("Dispensing-Take your cash")
    new_balance=account_balance-amount
    print("Your new balance is",new_balance)