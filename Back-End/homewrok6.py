class Mallar():

    def __init__(self,marka,model,il,qiymet,sayi) -> None:
        self.marka=marka
        self.model = model
        self.il = il
        self.qiymet = qiymet
        self.sayi = sayi

    def __str__(self) -> str:
        return f"Marka:{self.marka}\nModel:{self.model}\nYear:{self.il}\nPrice:{self.qiymet}\nMiqdar:{self.sayi}"

    def __len__(self):
        return f"Mallarin sayi:{self.sayi}"

    def change_marka(self,new_marka):
        self.marka = new_marka

    def change_model(self,new_model):
        self.model = new_model


class Comp(Mallar):

    def __init__(self, marka, model, il, qiymet, sayi,yaddas,ram,os) -> None:
        super().__init__(marka, model, il, qiymet, sayi)
        self.yaddas = yaddas
        self.ram = ram
        self.os = os

    def __str__(self) -> str:
        return f"Marka:{self.marka}\nModel:{self.model}\nYaddas:{self.yaddas}gb\nRam:{self.ram}gb\nOs:{self.os}\nYear:{self.il}\nPrice:{self.qiymet}$\nMiqdar:{self.sayi}" 

class Phone(Comp):

    def __init__(self, marka, model, il, qiymet, sayi, yaddas, ram, os,battery,sim) -> None:
        super().__init__(marka, model, il, qiymet, sayi, yaddas, ram, os)
        self.battery = battery
        self.sim = sim
    def __str__(self) -> str:
        return f"Marka:{self.marka}\nModel:{self.model}\nYaddas:{self.yaddas}gb\nRam:{self.ram}gb\nOs:{self.os}\nBaterya:{self.battery}mah\nSim:{self.sim}\nYear:{self.il}\nPrice:{self.qiymet}$\nMiqdar:{self.sayi}"    

class Soyuducu(Mallar):

    def __init__(self, marka, model, il, qiymet, sayi,) -> None:
        super().__init__(marka, model, il, qiymet, sayi)



telefon1=Phone('apple','İphone 12 pro max',2020,1100,10,128,6,'ios',3800,2)
telefon2=Phone("samsung","note 20",2020,1200,15,256,12,'Android',5100,2)
telefon1.sim=1
telefon1.change_model('Iphone 11 pro')
print(telefon1)
print('******************')
telefon2.change_model('pixel')
telefon2.change_marka('Google')
telefon2.qiymet=800
telefon2.ram=8
print(telefon2)

komp1=Comp("apple","macbook pro",2020,1200,20,256,8,"macos")
komp2=Comp('asus','rog strix',2020,1500,5,512,16,"windows 10")
print(komp1)
print('***************')
print(komp2)