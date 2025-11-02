class VendingMachine():

    def __init__(self, amount, stocks):
        self.amount = amount
        self.stocks = stocks

    def amounts(self):
       return self.amount
    def stocks(self):
        if self.stocks <= 0:
            print("Out of stock")
            return False
        
        else:
            self.stocks -= 1
            print("Transaction was successful")
            return True
        
                
class chips:
    count = 50

    def __init__(self, price, chip_types, stock ):
        self.price = price
        self.chip_types = chip_types
        self.stock = stock
        chips.count -= 1
    def get_price(self):
        return f"{self.price}{self.stock}" # INSTANCE 
    
    @classmethod
    def get_count(cls):
        return f"Total # of Stocks in Chips {cls.count}"
    
    


    
    
    
    def NameOfChips(self,type):
         

                   

        



class drinks:




class candy:









# Vending Machine Project
 
print("Welcome to the vending machine!")
payment_type = input("Coin or Cash")
try:
    choice = input("Insert a {payment_type}: \n 1. Chips \n  Drinks \n Candy")
    if choice == 1:
        chips()

    elif choice == 2:
        drinks()

    elif choice == 3:
        candy()
except:
    ValueError("Please enter a number")
