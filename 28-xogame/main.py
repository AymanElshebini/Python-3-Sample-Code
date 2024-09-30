#https://www.youtube.com/watch?v=GCYYkOSKj80&list=PLuXY3ddo_8nzCVqXcTFqwcM5R0gZiMRiW

"""
لعبه ox 
---class----
1-menu قائمة اللعبه
2-plyer  الاعب 
3-borde البورد  العبه اكس اوة
3-game logic 

"""
#---player class
class Player:
    def __init__(self):
        self.name=""
        self.symbol=""
    #فنكشن خاصة أدخال أسم المستخدم والتاكد من المدخلات حروف فقط 
    def choose_name(self):
        while True:
            name=input("enter your name : ")
            if name.isalpha():# isalpha() تقبل استرينج فقط
                self.name=name
                break
            print("invliad name.please use letters only. أستخدم الحروف فقط")
     # أستقبال الحرف واحد بس  اكس او اوه       
    def choose_symbol(self):
        while True:
            symbol=input(f"{self.name},choose your symbole(a single letter)")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()
                break
            print("Invild symoble , please choose a single letter.")
#---./player class
#---Menu class           
class Menu:
    def display_main_menu(self):
        print("welcome to my X-O game")
        print("1. Start Game")
        print("2. Quit Game")
        choice=int(input("Enter your choice (1 or 2) : "))
        return choice
    
    def display_engame_menue(self):
        menu_text= """
        Geme Over!
        1. Restart Game
        2. Quit Game
        Enter your choice(1 or 2)           
                   """
        choice=input(menu_text)
        return choice
#---./Menu class      
#---Board class 
class Board:
    def __init__(self):
        self.board=[str(i) for i in range(1,10)]

    def display_bord(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("-"*5)
    def update_bord(self,choice,symnol):
        if self.is_valid_move(choice):
            self.board[choice-1]=symnol
            return True
        return False

        



    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()
           


        

#---./Board class 
            
"""
x=Player()
x.choose_name()
x.choose_symbol()
"""
y= Menu()
y.display_engame_menue()
                   
        


