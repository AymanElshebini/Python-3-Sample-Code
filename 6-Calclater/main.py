"""
أكتب برنامج  اله حاسبه 
يدخل المستخدم رقمين ثم العمليه 
ويمكن للمستخد اعادة العمليه او الخروج 1
"""

class Calclater:
      def calc(self):
            
            C="Y"
            while (C!="N"): 
                num1=float(input("Enter number1 : "))
                op=input("Enter Oprator: ")
                num2=float(input("Enter number2 : "))
     
                if op=="+":
                        resalet= num1 + num2
                        print(resalet)
                elif op=="-":
                        resalet= num1 + num2
                        print(resalet)
                elif op=="*":
                        resalet= num1 * num2
                        print(resalet) 
                elif op=="/":
                        resalet=num1 /num2
                        print(resalet)     
                elif c=="N":
                      c=input("(Y/N):  ") 
                      print("Exite")        
                else:
                   print("error")  
                  
                        
#exmple_calc=Calclater()     
#exmple_calc.calc()
     
      


class Cal():
    def __init__(self,num1,num2) :
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1 + self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    def sub(self):
        return self.num1 / self.num2
        
num1=int(input("plasse enter first number : "))
num2=int(input("plasse enter scand number : "))

# أخذ نسخة من الكلاس وأعطائها قيم الانبوت 
myobject=Cal(num1,num2)

choice=1
while choice !=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice : "))
    if choice==1:
        print("Result: ",myobject.add()) 
    elif choice==2:
        print("Result : ",myobject.sub()) 
    elif choice==3:
        print("Result: ",myobject.mul())
    elif choice ==4:
        print("Result : ",round(myobject.div(),2))        
    elif choice==0:
        print("Exiting!")    
    else:("Invalid choice!!")    

