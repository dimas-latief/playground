import math
class Transaction():
    '''
    This is every new transaction that customer will have
    params:
        1. total_price -> total shop in $
        2. discount_rules -> in per 100 (float)
        3. shop_category -> Non Groceries / Groceries
    return: No
    Print: will print information of the object created
    '''
    def __init__(self, total_price, discount_rules = 0, shop_category = "Non Groceries"):
        self.total_price = total_price
        self.shop_category = shop_category
        self.total_price_deduction = 0
        if self.shop_category != "Non Groceries":
            self.discount_rules = 0
        else: 
            self.discount_rules = discount_rules
        print(f"New transaction is in process, with total price of ${total_price} and Categories in {shop_category}")

    def total_price_deduction_rules(self):
        '''
        For every $100 got deduction of $5 dollar
        example if shop $990 then will have $45 price deduction
        Param: self.total_price
        return: self.total_price_deduction
        '''
        self.total_price_deduction = math.floor(self.total_price/100) * 5
        return self.total_price_deduction