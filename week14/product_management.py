class InventoryManagement:
    def __init__(self):
        self.productlist = []
        self.salelist = []
        self.product_id = 1

    def product_registration(self):
        name = input("Enter Product Name: ")
        for product in self.productlist:
            if product["name"].lower() == name.lower():
                print(f"Product {product['name']} is already registered.")
                return
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Product Stock: "))
        prodcut = {"ID": self.product_id, "Name": name, "Price": price, "Stock": stock}
        self.productlist.append(prodcut)
        self.product_id += 1

    def update_stock(self):
        product_id = int(input("Enter Product ID you want to update: "))
        for product in self.productlist:
            if product["ID"] == product_id:
                quantity = int(input("Enter new stock quantity : "))
                product["Stock"] = quantity
                print("Product", {product['Name']}, " has been updated to ", {quantity}, "stock.")
                return
        print("Product", {product['Name']}, "not found.")

    def sell_product(self):
        id = int(input("Enter Product ID you want to update: "))
        quantity_sale = int(input("Enter product quantity to Sale : "))
        for product in self.productlist:
            if product["ID"] == id:
                new_stock = product["Stock"] - quantity_sale
                product["Stock"] = new_stock
                total = quantity_sale * product["Price"]
                sale = {"ID": id, "Quantity": quantity_sale, "Total": total}

    def search_product(self):
        product_id = int(input("Enter Product ID you want to search: "))

        for product in self.productlist:
            if product["ID"] == product_id:
                print("Product ID: ", product["ID"])
                print("Product Name: ", product["Name"])
                print("Product Price: ", product["Price"])
                print("Product Stock quantity: ", product["Stock"])
                return
        print("Product", {product['Name']}, "not found.")

    def display_summary(self):
        total_products = len(self.productlist)
        item_sold = 0
        sales_value = 0

        for sale in self.salelist:
            item_sold += sale["Quantity"]
            sales_value += sale["Total"]

        print("---------------------Sales Summary----------------------")
        print("Total number of products: ", total_products)
        print("Total number item sold : ", item_sold)
        print("Total number of sales value: ", sales_value)

        print("-----------------Current Stock levels--------------------")
        for product in self.productlist:
            print(product["Name"], "-Stock: ", product["Stock"])

    def menu_system(self):
        while True:
            print("=================Inventory=================")
            print("1. Add Product")
            print("2. View All Product")
            print("3. Update Product stock")
            print("4. Sell product")
            print("5. Search product")
            print("6. View Sales Summary")
            print("7. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.product_registration()

            elif choice == 2:
                self.search_products()

            elif choice == 3:
                self.update_stock()

            elif choice == 4:
                self.sell_product()

            elif choice == 5:
                self.search_product()

            elif choice == 6:
                self.display_summary()

            elif choice == 7:
                print("Thank you for using purchase system.")
                break

            else:
                print("Please enter a valid choice.")

pro = InventoryManagement()
pro.menu_system()









