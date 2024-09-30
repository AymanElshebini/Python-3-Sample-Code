"""
أكتب برنامج لمعرفة الارقام المتكررة في اليست 

"""

def myfun():
    numbers=[1,1,2,2,1,3,4,5,6,7,8,9,9,6,4,4]
    unicn_umber_list=[]
    for number in numbers:
        if number not in unicn_umber_list:
            unicn_umber_list.append(number)
    return unicn_umber_list



x=myfun()
print(x)
