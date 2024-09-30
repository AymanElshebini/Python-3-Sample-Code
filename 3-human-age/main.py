"""
أكتب برنامج يقوم المستخدم بادخال عمر الانسان 
ثم يقوم بطباعه هل هذا الانسان 
رضيع - طفل - ام شاب - ام رجل - عجوز - ام معمر 
"""

class Peoples:
    #---------------------طريقة أولي ------------------
    def PeopleAge(self):
        age=int(input("Enter Age :  "))
        if(age == 0):
            return "plasse Enter your age"
        elif(age < 3):
            print("infant")
        elif(age >=3 and age<=18):
            print("child") 
        elif(age >=18 and age<=35):
            print("Yoth") 
        elif(age >=35 and age <=55):
            print("man")
        elif(age >=55 and age<=80):
            print("old") 
        else:print("senior") 
    #---------------------same code but using List------------------
    def PeopleAge2(self):  
        age=int(input("Enter your Age:"))
        AgeList=['plasse Enter your age','infant','child','man','old','senior']
        if(age==0):
            return AgeList[0]
        elif(age <=3):
            return AgeList[1]
        elif(age > 3 and age <18):
            return AgeList[2]
        elif(age >=18 and age<35 and age <=55):
            return AgeList[3]
        elif(age >=55 and age <=80):
            return AgeList[4]
        else:
            return(AgeList[5])
  
#object class  
obPeoples=Peoples()
obPeoples.PeopleAge()

    


  


