#crete list  from 2 to 10
def myfuncation():
    rnum1=int(input("enter number1:"))
    rum2=int(input("enter number2:"))
    resalet=range(rnum1,rum2)
    for item in resalet:
        print(item)
myfuncation()


# حساب قاعدة مثلث 
def tri_area(base, height):
    Area = 1/2 * base *  height
    return Area
print(tri_area(10,20))




def ShowList():
    MyList=["Egypt","Usa","China"]
    addnew=input("plasse enter countery")
    MyList.append(addnew)
    return MyList

print(ShowList())


# الاعداد الزوجيه 
mylist=[1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    if i%2==0:
        print(i)



for i in range(1,10):
    if i%2==0:
        print(i)
#-------------------------------
        
  #--------------------الاعداد الفرديه       

for i in range(1,10):
  if i%3==0:
   print(i)




mylist=[1,2,3,4,5,6,7,8,9,10]

for item in mylist:
    if item%3==0:
        print(item)
