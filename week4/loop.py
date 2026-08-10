num_items = int(input("Enter number of items to purchase: "))
grand_total = 0
for i in range(num_items):
    print("Item",i+1)
    item_name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    total_price = price * quantity
    grand_total=grand_total + total_price
    print("-------")
    print("item_name:",item_name)
    print("item_price:",price)
    print("quantity:",quantity)
    Item_total = price * quantity
    print("total price:",total_price)

    print("grand_total:",grand_total)

