from pbuild import pBuild
from item import *

class Player(object):
    def __init__(self, name="Levanald"):
        self.name = name
        self.build = pBuild()
        self.P = self.build.getP()
        self.M = self.build.getM()
        self.S = self.build.getS()
        self.current_Plevel = self.getbuild().getPlevel()
        self.current_Mlevel = self.getbuild().getMlevel()
        self.current_Slevel = self.getbuild().getSlevel()
        self.record = []

    def change_item(self, item, slot):
        self.record.append([self.build.getP(), self.build.getM(), self.build.getS()])
        self.getbuild().change_item(item, slot)
        self.P = self.build.getP()
        self.M = self.build.getM()
        self.S = self.build.getS()
        self.current_Plevel = self.getbuild().getPlevel()
        self.current_Mlevel = self.getbuild().getMlevel()
        self.current_Slevel = self.getbuild().getSlevel()

    def getname(self):
        return self.name

    def getbuildname(self):
        return self.build.getName()

    def getdescription(self):
        return self.build.getDescription()

    def getbuild(self):
        return self.build

    def getrecord(self):
        return self.record

me = Player(name="Tejas")

me.change_item(Personal_Trainer, 1)
me.change_item(Giant_Sword, 2)
me.change_item(Sports_Ball, 3)

print(me.getbuild().item1.getname())
print(me.getbuild().getPlevel())
print(me.getbuild().getMlevel())
print(me.getbuild().getSlevel())
print(me.getbuildname())