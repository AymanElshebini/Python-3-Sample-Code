"""
      ---------------------  أكتب برنامج ---------------
      Python program to check whether the given number is even or not.
      لمعرفة الرقم الزوجي أو الفردي 
      برنامج عند أستخدامة يعرف العدد زوجي أو فردي
even زوجي
odd فردي

الرقم الزوجي هو عدد صحيح يقبل القسمة على 2 دون ترك باقي، مثل 2، 4، 6، 8، 10، وهكذا.

الرقم الفردي هو عدد صحيح لا يمكن قسمته بالتساوي على 2، ويتبقى 1. تتضمن الأمثلة 1، 3، 5، 7، 9، وما إلى ذلك.
"""

class MyOdd:

    def Exmple1(self):
        EnterNumber=input("Enter a Number: ")
        x=int(EnterNumber) % 2
        if x==0:
            print("This number is Even العدد زوجي")
        else:
             print("this number is Odd  العدد فردي'") 
             return x
        
    def Exmple2(self):
         EnterNumber=int(input("Enter a Number: "))
         if EnterNumber % 2 ==0:
              print("This number is Even العدد زوجي")
         else:
            print("this number is Odd  العدد فردي'") 
            return EnterNumber
    #عرض الارقام الفرديه                
    def Exmple3(self):
        LOwerNumber=int(input("Enter Lower Number أدخل اقل رقم : "))
        UpperNumber=int(input("Enter Upper Number : أدخل أكبر رقم "))
        for i in  range(LOwerNumber,UpperNumber +1):
            if(i %2 !=0):
                print("this is odd number الارقام الفرديه",i)


     

Myreslet=MyOdd()
Myreslet.Exmple3()


        
                
    