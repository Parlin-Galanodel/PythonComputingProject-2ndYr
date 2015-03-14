#####################
# Task 6 & 7: Four vectors
#####################
from numpy import array as na
class FourVector(object):
    '''
    An implementation of four vectors in relativity
    practise the  __init__ method
    '''

    def __init__(self, ct = 0, x=0,y=0,z=0,r=na([0, 0, 0])):
        self.ct = ct
        self.x = r[0] or x
        self.y = r[1] or y
        self.z = r[2] or z
        
    def __repr__(self):
        return 'FourVector(ct=%g, r=[%g, %g, %g])' %(self.ct,self.x,self.y,self.z)
        
    def __str__(self):
        return '(%g, %g, %g, %g)' %(self.ct, self.x, self.y, self.z)