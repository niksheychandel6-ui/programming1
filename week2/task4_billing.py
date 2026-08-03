Itemname=input("Enter Item Name:")
ItemPrice=float(input("Enter Item Price:"))
Quantitypurchased=float(input("Enter Quantity Purchased:"))
Totalcost=ItemPrice*Quantitypurchased
GST=Totalcost/100*15
FinalpriceIncludingGST=Totalcost+GST
print("-----RECEIPT------")
print("ITEM:",Itemname)
print("price per item:",ItemPrice)
print("quantity:")
print("subtotal:")
print("GST(15%):")
print("Total:")
print("------------------------")