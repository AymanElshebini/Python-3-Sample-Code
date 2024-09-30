"""
أكتب نمرين 
نرتيب الارقام تصاغديا 


"""
list1=[1900,2000,6000,2,30]
list2=[]
l=len(list1)
for i in range(l):
    min=list1[0]
    for j in range(l):
        #print(list1[i],list1[j])
        if(min > list1[j]):
            min=list1[j]
    list2.append(min)    
    list1.remove(min)
    l-=1
print(list2)        
