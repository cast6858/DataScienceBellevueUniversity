class Cash_Register:

    cart_amount = 0
    def __init__(self):
        self.price = 0

    def add_item(self,price):
        self.price += price
        Cash_Register.cart_amount += 1

    def get_count(self): #item in cart
        return self.cart_amount

    def get_total(self): #total price
        return self.price


