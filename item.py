class Item(object):
    def __init__(self, name, p, m, s):
        self.name = name
        self.P = p
        self.M = m
        self.S = s
        self.effect = lambda: print("There is no effect for this item")
        self.dominant = str([key for key, var in locals().items() if var is max([p, m, s])][0])

    def getP(self):
        return self.P

    def getM(self):
        return self.M

    def getS(self):
        return self.S

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def change_effect(self, func):
        self.effect = func

    def use_effect(self):
        return self.effect()

itemlist = []

Schrodingers_Box = Item("Schrodinger's Box", 0, 60, 40)
sch_box_ef = lambda x: print("Schrodinger's Box Effect activated!")
Schrodingers_Box.change_effect(sch_box_ef)
itemlist.append(Schrodingers_Box)

Giant_Sword = Item("Giant Sword", 90,0,10)
itemlist.append(Giant_Sword)

AP_Chemistry = Item("AP Chemistry", 40, 60, 0)
itemlist.append(AP_Chemistry)

iPhone = Item("iPhone", 10, 10, 80)
itemlist.append(iPhone)

Green_Shake = Item("Green Shake", 60, 20, 20)
itemlist.append(Green_Shake)

Mind_Reader = Item("Mind Reader", 30, 70, 0)
itemlist.append(Mind_Reader)

Encryption_Algorithm = Item("Encryption Algorithm", 20, 70, 10)
itemlist.append(Encryption_Algorithm)

Sports_Ball = Item("Sports Ball", 80, 10, 10)
itemlist.append(Sports_Ball)

Megaphone = Item("Megaphone", 20, 10, 70)
itemlist.append(Megaphone)

Extrovertedness = Item("Extrovertedness", 0, 0, 150)
extro_ef = lambda x: print("Extroverted effect activated!")
Extrovertedness.change_effect(extro_ef)
itemlist.append(Extrovertedness)

Community_College = Item("Community College", 10, 30, 60)
itemlist.append(Community_College)

Personal_Trainer = Item("Personal Trainer", 70, 30, 0)
pers_train_ef = lambda x: print("Personal Trainer effect activated!")
Personal_Trainer.change_effect(pers_train_ef)
itemlist.append(Personal_Trainer)