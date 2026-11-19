class supermarket:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
            print("Product:", self.name)
            print("Price: $", self.price)
            print("Quantity:", self.quantity)

    def add_items(self, amount):
        self.quantity += amount

    def remove_items(self, amount):
        if amount <= 0:
            print("Cannot remove that quantity")
        elif amount > self.quantity:
            print("Cannot remove that quantity")
        else:
            self.quantity -= amount

    def calculate_total(self):
        return self.price * self.quantity

    def remove_item(self,amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print("return successfully")
        else:
            print("Cannot remove that quantity")


#What is the name of our class?
#Ans1.The name of our class is supermarket.
#Is name an attribute or a method?
#Name is an attribute.
#Why are we using self.name?
#We are using self.name to store the data in the given variables.
#What is the purpose of __init__()?
#The purpose of __init__() is to initialize an object when it is created from a class.

#Activity 2B Adding a method
bread = supermarket("Bread", 3, 2)
print(bread.name)
print(bread.price)
print(bread.quantity)

#Activity 2C

#Activity 3 Mutltiple products
milk = supermarket ("Milk", 4, 1)
apples = supermarket("Apples", 2, 3)

bread.display_info()
milk.display_info()
apples.display_info()

#Did we created 3 classes?
#No we created only 1 class.
#We created three objects from the same class.
#Why does bread contain different info?
#Because each object stores its own data.
#Do we need a new class for bananas?
#No, just create another object.

bananas = supermarket ("Bananas", 5, 2)
milk.add_items(5)
milk.display_info()
apples.add_items(5)
apples.display_info()

milk.remove_items(2)
milk.display_info()
apples.remove_items(5)
apples.display_info()

total1=milk.calculate_total()
total2=bread.calculate_total()
total3=apples.calculate_total()

grand_total= bread.calculate_total() + milk.calculate_total() + apples.calculate_total()
print(grand_total)

# Print receipt
print("================================")
print("        MY SUPERMARKET")
print("================================")

products = [bread, milk, apples]

grand_total = 0

for item in products:
    item_total = item.calculate_total()
    print(f"Product: {item.name}")
    print(f"Price: ${item.price}")
    print(f"Quantity: {item.quantity}")
    print(f"Total: ${item_total}")
    print("--------------------------------")
    grand_total += item_total

print(f"GRAND TOTAL: ${grand_total}")
print("================================")
print("Thank you for shopping!")












