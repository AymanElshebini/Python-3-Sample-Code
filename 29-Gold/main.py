
"""
Price_Gold=int(input("Enter price gold  : "))
Price_gram=float(input("Enter grame : "))
masna3a=int(input("Enter masn3ia : "))
resaelt=(Price_Gold + masna3a) * Price_gram
print(resaelt)

"""



class Gold():
    def __init__(self,price,gram,wages):
        self.price=price
        self.gram=gram
        self.wages=wages

    def gold_colclation(self):
        result=(self.price + self.wages) * self.gram
        return result
InPrice=float(input("Enter price Gold : "))    
InGram=float(input("Enter Gram :"))   
InWages=float(input("Enter Wages : "))

myobject=Gold(InPrice,InGram,InWages)
result=myobject.gold_colclation()
print(f"price  you will pay : {result}")



      
