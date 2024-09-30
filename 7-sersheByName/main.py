"""
يدخل المستخدم عدة اسماء ثم يحدد عددهم 
وبعد ذالك يبحث عن اسم من بين الاسماء التي ادخلها مسبقا 
"""
#https://www.youtube.com/watch?v=fydWFFmhixY&list=PLNTw7D3PcbITQP3tCei7eqGGKaJqo3JmG&index=7
Count=int(input("Enter the Number of Names:  "))
myList=[]
for i in range(0,Count):
    Name=input("Enter Name: "+ str(i+1) + ":" )
    myList.append(Name)
search=input("Enter the name you want to search for the list:")  
for j in myList:
    if search == j:
        print("Exist")
        break
    else:
        continue    


