import math
class Transaction():
    '''this is every new transaction that customer will have'''
    def __init__(self, total_price, discount_rules = 0, shop_category = "Non Groceries"):
        self.total_price = total_price
        self.shop_category = shop_category
        self.total_price_deduction = 0
        if self.shop_category != "Non Groceries":
            self.discount_rules = 0
        else: 
            self.discount_rules = discount_rules
        print(f"New transaction is in process, with total price of ${total_price} and Categories in {shop_category}")