"""
أكتب برنامج لتسجيل الدخول  والتحقق من الادخال 
"""


def funlogin():

    usernameIn=input("plesse enter User name : ")
    passwordIn=input("plasse enter your password :")
    email="ayman@hotmail.com"
    password="123"
    if  email==usernameIn  and password==passwordIn:
        print("login sucess")
    elif email==usernameIn and password !=passwordIn:
        print("passowrd not correct")   
    elif email !=usernameIn and password ==passwordIn:
        print("UserName not correct")    
    elif email !=usernameIn and password != passwordIn:
        print("User Name and Password not coreccet")    

    else:
        print("try agin")    


funlogin()







