from namedict import names
from descriptions import desc
from item import *

class ImpossibleError(BaseException):
    """ That's Impossible! """
    def __init__(self, message="That's Impossible!", errors=None, *args, **kwargs):
        super().__init__(message)
        self.errors = errors
        self.raised = False if callable(ImpossibleError) else True

class pBuild(object):
    def __init__(self,p=0, m=0, s=0, to=5):
        super(pBuild, self).__init__()
        self.time = to
        self.item1 = Item("Blank slot", 0,0,0)
        self.item2 = Item("Blank slot", 0,0,0)
        self.item3 = Item("Blank slot", 0,0,0)
        self.items = [self.item1, self.item2, self.item3]
        self.pgain = 0
        self.mgain = 0
        self.sgain = 0
        self.p = p
        self.m = m
        self.s = s
        self.plevel = 0
        self.mlevel = 0
        self.slevel = 0
        self.th1 = 50 # thresholds to levels one, two, and three
        self.th2 = 100
        self.th3 = 150
        self.recalc()

    def change_item(self, item, slot):
        if slot == 1:
            self.item1 = item
        elif slot == 2:
            self.item2 = item
        elif slot == 3:
            self.item3 = item
        self.items = [self.item1, self.item2, self.item3]
        self.recalc()

    def recalc(self):
        self.p = 0
        self.m = 0
        self.s = 0
        for item in self.items:
            self.p += item.getP() + self.pgain
            self.m += item.getM() + self.mgain
            self.s += item.getS() + self.sgain

    def getP(self):
        self.recalc()
        return self.p

    def getM(self):
        self.recalc()
        return self.m

    def getS(self):
        self.recalc()
        return self.s

    def sort_level(self, val):
        if val <= self.th1:
            lev =  0
        elif val <= self.th2:
            lev = 1
        elif val <= self.th3:
            lev = 2
        elif val > self.th3:
            lev = 3
        else:
            raise ImpossibleError(message="Error pBuild.py sortlevel function")
        return lev

    def getPlevel(self):
        self.recalc()
        self.plevel = self.sort_level(self.p)
        self.recalc()
        return self.plevel

    def getMlevel(self):
        self.recalc()
        self.mlevel = self.sort_level(self.m)
        self.recalc()
        return self.mlevel

    def getSlevel(self):
        self.recalc()
        self.slevel = self.sort_level(self.s)
        self.recalc()
        return self.slevel

    def addPGain(self, gain):
        self.recalc()
        self.pgain += gain
        self.recalc()

    def addMGain(self, gain):
        self.recalc()
        self.mgain += gain
        self.recalc()

    def addSGain(self, gain):
        self.recalc()
        self.sgain += gain
        self.recalc()

    def getName(self):
        self.recalc()
        return names[self.getPlevel()][self.getMlevel()][self.getSlevel()]

    def getDescription(self):
        self.recalc()
        return desc[self.getName()]