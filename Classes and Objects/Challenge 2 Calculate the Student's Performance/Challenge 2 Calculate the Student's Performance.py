class Student:
    def __init__(self, name=None, phy=None, chem=None, bio=None):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self, phy, chem, bio):
        print((phy+chem+bio/300)*100)

    def Total(self, phy, chem, bio):
        print(phy+chem+bio)


Soln = Student()
Soln.Total(80, 90, 40)
Soln.totalObtained(80, 90, 40)
