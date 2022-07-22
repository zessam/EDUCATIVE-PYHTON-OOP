class Point:
    def __init__(self, x = None, y = None,z = None) :
        self.x = x;
        self.y = y;
        self.z = z;
    
    def sqSum(self, x = None, y = None,z = None):
        print((x*x)+(y*y)+(z*z));
    

Soln = Point()
Soln.sqSum(1,3,5)