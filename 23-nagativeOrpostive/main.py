"""
أكتب برنامج يقوم المستخدم بادخال رقم 
ثم  يقوم البرنامج بالتحقق أذا كان الرقم المدخل سالب أو موجل 
The program takes a number and checks whether it is positive or negative.

"""

def funNagativeor_postive():
    number=int(input("Enter a number:"))
    if(number > 0):
        print("this is postive")
    else:
        print("this is Nagitive number")   


funNagativeor_postive()