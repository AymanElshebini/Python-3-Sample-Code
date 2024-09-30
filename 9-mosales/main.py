"""
أنشاء مثلث من النجوم 6 صفوف 
*
**
***
****
*****
********
"""

count=1
for i in range(0,6):
    for j in range(0,count):
        print("*",end="")
    count+=1
    print("\n")

