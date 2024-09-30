
"""
برنامج لعرض البلاد
"""

def MyCuntery(Cuntery):
   CunteryList={
        "Egy":"Egypt",
        "Ksa": "Sudia arabia",
    }
   for i in CunteryList:
       if(i==Cuntery):
           return CunteryList.values()
       else:
           print("this is not saved")

print(MyCuntery("Egy"))


