
#برنامج حساب عمرك بالايام

def ClacDays(age):
    return "your days is: "+str(age*365)+"Days "
print(ClacDays(11))


#برنامج أدخل لة عمرك يحسب كام ساعة عشتها

def ClacHoursLive(YourAge):
    resaelt= YourAge * 365 * 24
    return str(resaelt)
print(ClacHoursLive(int(input(" ehter your age : "))))