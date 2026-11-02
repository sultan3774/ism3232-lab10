# stock_tool.py
# Author: Sultan Ali


class StockLookup:
    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product):
        if product in self.stock:
            return self.stock[product]
        return None
