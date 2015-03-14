########################
# Task 1-5, worksheet 2
########################

class Shape:
    counterOfRed=0
    def __init__(self,color=None):
        self.__color=color
        if self.__color in ('Red', 'red', 'RED', 'R', 'r'):
            Shape.counterOfRed+=1
        
    def getColor(self):
        return self.__color
        
    def setColor(self, newColor):
        origin=self.__color
        self.__color=newColor
        if origin not in ('Red', 'red', 'RED', 'R', 'r') \
                       and newColor in ('Red', 'red', 'RED', 'R', 'r'):
            Shape.counterOfRed+=1
        elif origin in ('Red', 'red', 'RED', 'R', 'r') \
                    and newColor not in ('Red', 'red', 'RED', 'R', 'r'):
            Shape.counterOfRed-=1
        elif origin in ('Red', 'red', 'RED', 'R', 'r') and \
                     newColor in ('Red', 'red', 'RED', 'R', 'r'):
            pass
        else: pass
        
    def __del__(self):      #Destructor, activate when instances are deleted
        if self.__color in ('Red', 'red', 'RED', 'R', 'r'):
            Shape.counterOfRed-=1
        
        
class Square(Shape):
    def __init__(self,length=0):
        self.__length=length
        color=None
        Shape.__init__(self,color)
        
    def Area(self):
        return length**2
        

    
class Triangle(Shape):
    def __init__(self,length=0):
        self.__length=length
        color=None
        Shape.__init__(self,color)
    
    def Area(self):
        return length**2*3**0.5/2
        
class Circle(Shape):
    def __init__(self,length=0):
        self.__length=length
        color=None
        Shape.__init__(self,color)
            
    def Area(self):
        from math import pi
        return pi*length**2

# Task 4:
def f(x):
    '''
    func used to set color to Red for instances of Shape
    '''
    if isinstance(x,Shape):
        x.setColor('Red')
    else:
        raise Exception('not compatiable')

#Counter
def i():
    return Shape.counterOfRed
    
