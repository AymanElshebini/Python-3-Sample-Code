"""
 list in python is mutable 
 الليست قابله للتعديل 
"""
a=[10,20,30,40,50]
print(a[-2])#40
print(a[-4:-1])#[20, 30, 40]

# exmples 2 
b=[5,10,15,25]
print(b[::-2])#[25, 10]
print('=' *100)

#exmples 3 
c=[10,20,30,40,50]
c.append(60)# أضافه في نهايه العنصر 
c.append(60)
print(c)
print(max(c))
print('=' *100)

#exmples 4 
d=[4,8,12,16]
d[1:4]="ayman"
print(d)
print('=' *100)

#emples 5
f=[10,20,30,40,50,60,70,80]
print(f[2:5])#[30,40,50]
print(f[:4])#[10, 20, 30, 40]
print(f[3:])#[40, 50, 60, 70, 80]
print('=' *100)
#exmpels 6 
g=["python",[4,5,6,7,8,9]]
print(g[0][1])#y 
print(g[1][3])#7
print('=' *100)

#exmples7 
h=[10,20,30,40,50]
h.pop() #حذف أخر عنصر 
print(h)
h.pop(2) #حذف العنصر الثاني 
print(h)



