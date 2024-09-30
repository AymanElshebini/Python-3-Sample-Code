
"""
المثال التالي 
قم الغاء المسافات من الشمال 
والغاء #@
من اليمين 
resalet : i love python.
"""

class Clean:
    def Clean_chracter(self):
        name="            i love python.#@#@#@#@#@#@#@#@#@"
        var1=name.lstrip()
        var2=var1.lstrip("#@")
        var3=var2.title()
        print(var3)


     #نفس المثال ولاكن بحل أخر 
    def Clean_chracter2(self):
        name="            i love python.#@#@#@#@#@#@#@#@#@"
        var=name.lstrip().lstrip("#@").title()
        print(var)
        





var_clean=Clean()
var_clean.Clean_chracter2()

