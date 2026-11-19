def get_items():
    items={}

    while True:
        item=input("Enter item:")

        if item.lower() == "done":
            break
        price=float(input("Enter item price:"))
        items[item]=price

    return items
def print_items(items):
    print("Items:")
    total_price=0

    for item,price in items.items():
        print(item,price)
        total=price+total_price
        print("Total:",total)
