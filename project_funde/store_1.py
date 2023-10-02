class Store:
    #กำหนดค่าต่าง ๆ ของสินค้า
    def __init__(self):
        self.products = {
            "apple": 0.5,
            "banana": 0.3,
            "milk": 1.2,
            "bread": 2.0,
            "juice": 1.5,
        }
        
        # Categories
        self.categories = {
            "fruits": ["apple", "banana"],
            "beverages": ["milk", "juice"],
            "bakery": ["bread"]
        }
        
        #กำหนดและแนะนำโปรโมชันของสินค้า
        self.promotions = {
            "apple_banana": "Buy an apple and a banana to get 10% off on both!",
            "milk_bread": "Buy milk and bread together for just $3!"
        }
        
        #กำหนดส่วนลดของสินค้านั้น ๆ
        self.discounts = {
            "banana": 0.1,
            "juice": 0.2,
        }
        
    #แนะนำสินค้า สำหรับลูกค้าที่ไม่รู้ว่าจะซื้ออะไร
    def advise_customer(self):
        advice = [
            "If you're thirsty, try juice or milk!",
            "For a quick snack, bananas and apples are healthy!",
            "Bread is great for sandwiches and toast."
        ]
        return advice
        
    #คำนวนรายการสินค้า
    def calculate_cost(self, cart):
        total = 0
        for item, quantity in cart.items():
            total += self.products[item] * quantity

            if item in self.discounts:
                total -= self.products[item] * self.discounts[item] * quantity

        if "apple" in cart and "banana" in cart:
            total -= (self.products["apple"] + self.products["banana"]) * 0.1
        if "milk" in cart and "bread" in cart:
            total = total - (self.products["milk"] + self.products["bread"]) + 3

        return round(total, 2)
        
    #แสดงว่ารายทั้งหมดพร้อมราคา
    def show_products(self):
        for product, price in self.products.items():
            print(f"{product.capitalize()}: ${price}")
            
    #ค้นหารายการสินค้า
    def search_product(self):
        search_term = input("Enter product name or partial name to search: ").lower()
        matches = [prod for prod in self.products.keys() if search_term in prod]
        
        if not matches:
            print("No products found for your search.")
            return
        
        for match in matches:
            print(f"{match.capitalize()}: ${self.products[match]}")
            for promo, desc in self.promotions.items():
                if match in promo:
                    print(f"Promotion: {desc}")
                    
    #checkout และ show ราคาทั้งหมด
    def checkout(self, cart):
        total_cost = self.calculate_cost(cart)
        print(f"Your total cost is: ${total_cost}")
        
    #เลือกรายการที่จะซื้อ พร้อมจำนวนที่จะซื้อ
    def recursive_ask(self, cart):
        product_name = input("Enter product to buy (or 'done' to checkout): ").lower()

        if product_name == 'done':
            return cart
        elif product_name not in self.products:
            print("Sorry, we don't have that product. Please try again.")
            return self.recursive_ask(cart)

        quantity = int(input(f"How many {product_name}(s) would you like to buy? "))
        cart[product_name] = cart.get(product_name, 0) + quantity

        return self.recursive_ask(cart)

    def run(self):
        cart = {}
        print("Welcome to our store!")

        while True:
            print("\nOptions:")
            print("1: Advise me")
            print("2: Show products")
            print("3: Buy")
            print("4: Search product")
            print("5: Checkout")
            print("6: Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                advice = self.advise_customer()
                for a in advice:
                    print(a)
            elif choice == '2':
                self.show_products()
            elif choice == '3':
                cart = self.recursive_ask(cart)
            elif choice == '4':
                self.search_product()
            elif choice == '5':
                self.checkout(cart)
            elif choice == '6':
                print("Thank you for shopping")
                break
            else:
                print("Please try again.")

store = Store()
store.run()
