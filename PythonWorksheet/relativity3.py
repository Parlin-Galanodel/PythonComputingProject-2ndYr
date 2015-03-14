#####################
# Task 10-13: Four vectors
#####################
from numpy import array as na
class FourVector(object):
    '''
    An implementation of four vectors in relativity
    When instantiate a FourVector, users must chose to use either (x,y,z) or r, these redundant args are
    intended to give options to initialise FourVector.
    '''
    def __init__(self, ct = 0, x = 0, y = 0, z = 0, r = [0, 0, 0]):
    #ct, x, y, z are private, not allowed to be accessed outside this object.
        if len(r) != 3:
            raise Exception('r must be a 3D vector')
        elif r != [0,0,0] and (x != 0 or y != 0 or z != 0):
            raise Exception('instantiate four vector by only one option way')
        else:
            self.__ct = ct
            self.__x = r[0] or x
            self.__y = r[1] or y
            self.__z = r[2] or z
            self._r = na([self.__x, self.__y, self.__z])  
        
    def __repr__(self):
        return 'FourVector(ct=%g, r=[%g, %g, %g])' %(self.__ct,self.__x,self.__y,self.__z) 
        
    def __str__(self):
        return '(%g, r=( %g, %g, %g))' %(self.__ct, self.__x, self.__y, self.__z)      
        
    def ct(self):
    # return the time like component 
        return self.__ct   
        
    def r(self):
    # return the space like component
        return self._r 
        
    def copy(self):
    # return a copy of the four vector
        return FourVector(self.__ct, *self._r)
        
#Task 10
    def __add__(self,other):
        ct = self.ct() + other.ct()
        r = self.r() + other.r()
        return FourVector(ct,*r)
        
    def __iadd__(self,other):
        self.__ct += other.__ct
        self._r += other._r         # self add on space like component 
        # x,y,z = r unify the attributes
        self.__x += other.__x
        self.__y += other.__y
        self.__z += other.__z
        return self
        
    def __sub__(self,other):
        ct = self.ct() - other.ct()
        r = self.r() - other.r()
        return FourVector(ct, *r)
        
    def __isub__(self, other):
        self.__ct -= other.__ct
        self._r -= other._r
        self.__x -= other.__x
        self.__y -= other.__y
        self.__z -= other.__z
        return self
        
#Task 11
    def inner(self,other):
        '''
            A func used to calculate the inner product of this four vector and another one
            by the formula <v1|v2>=ct1*ct2-<r1|r2>
        '''
        ct=self.__ct * other.__ct
        r=self._r * other._r
        r=reduce(lambda x, y : x+y,r)
        return ct-r
        
    def magsquare(self):
    # magsquare is the value of inner product with itself
        return self.inner(self)
        
#Task 12
    def boost(self,beta):
        '''
            Lorentz transformation in z direction
        '''
        gama = 1./(1.-beta**2)**0.5
        ct = gama*self.__ct - beta * gama * self.__z
        x = self.__x
        y = self.__y
        z = self.__z * gama - beta * gama * self.__ct
        return FourVector(ct, x, y, z)