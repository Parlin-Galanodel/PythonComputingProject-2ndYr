#####################
# Task 8 & 9: Four vectors
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
        return self.__ct
        
    def r(self):
        return self._r
        
    def copy(self):
        return FourVector(self.__ct, *self._r)