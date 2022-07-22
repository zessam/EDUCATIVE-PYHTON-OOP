class Student:
    def __init__(self, name = None, rollnumber = None):
        self.__name = name
        self.__rollnumber = rollnumber
    def setName(self):
         self.__name = input("Enter the name ")

    def getName(self):
        print("The name is: ", self.__name)

    def setRollNumber(self):
        self.__rollnumber = input("Enter the rollnumber " )


    def getRollNumber(self):
        print("The rollnumber is: ", self.__rollnumber)


obj = Student()
obj.setName()
obj.setRollNumber()
obj.getName()
obj.getRollNumber()