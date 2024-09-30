"""
   ---------------------  أكتب برنامج ---------------
التحويل من درجة مئوية إلى فهرنهايت

تحويلها من المئوي إلى الفهرنهايت بضربها بقيمة  9/5، وأضافة 32

"""

class Temprature:
    def mytemp(slef):
        temp=input("Enter temperature in Centigrade:")
        f=(9*(int(temp))/5)+32
        print("Temperature in Fahrenheit is: ", f)



temp=Temprature()
temp.mytemp()