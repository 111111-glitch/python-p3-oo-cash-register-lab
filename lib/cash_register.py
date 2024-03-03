class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
            self.total += price

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            self.total -= self.items.pop()

    def remove_all_items(self):
        self.total = 0.0
        self.items = []

    def get_all_items(self):
        return self.items
