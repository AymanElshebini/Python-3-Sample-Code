""""
أكتب برنامج يشيل علامة الموجب من النص 
+
يستبدلها 
|

I Love Python + I love Programing 

"""
var ="I Love Python  + I love Programing "
print(var.replace("+","|")) #تحويل الحرف من + الي   | الحرف

print(" | ".join(var.split(" + "))) #طريقه اخري من الحل 




var1=["ayman","ahmed","alie","smaya"]
var1[-1]=["A","B","C","D"]
print(var1)