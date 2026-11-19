class ShoppingCart:
    def __init__(self, customer_name, product_name, price, quantity):
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total = 0
        self.discount = 0
        self.final_total = 0

    def calculate_total(self):
        self.total = self.price * self.quantity
        return self.total

    def apply_discount(self):
        if self.total >= 500:
            self.discount = self.total * 0.10
        else:
            self.discount = 0
        self.final_total = self.total - self.discount
        return self.final_total

    def display_cart(self):
        print("Customer Name:", self.customer_name)
        print("Product:", self.product_name)
        print("Quantity:", self.quantity)
        print("Total Price: $", self.total)
        print("Discount: $", self.discount)
        print("Total After Discount: $", self.final_total)
        print("-----------------------------------")


cart1 = ShoppingCart("Nikshey", "Laptop", 1200, 1)
cart2 = ShoppingCart("John", "Headphones", 150, 3)


print("=== Cart 1 ===")
cart1.calculate_total()
cart1.apply_discount()
cart1.display_cart()

print("=== Cart 2 ===")
cart2.calculate_total()
cart2.apply_discount()
cart2.display_cart()
