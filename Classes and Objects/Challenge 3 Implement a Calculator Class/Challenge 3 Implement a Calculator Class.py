class Calculator:
    def __init__(self, num1 = None, num2 = None):
        self.num1 = num1;
        self.num2 = num2;
    
    def add(self, num1, num2):
        print(num1+num2);
    def subtract(self, num1, num2):
        print(num2-num1);
    def multiply(self, num1, num2):
        print(num1*num2);
    def divide(self, num1, num2):
        print(num2/num1);


Soln = Calculator();
Soln.add(10, 94);
Soln.subtract(10, 94);
Soln.multiply(10, 94);
Soln.divide(10, 94);