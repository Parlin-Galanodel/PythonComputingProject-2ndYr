#####################
# Task6: Four vectors
#####################
from numpy import array as na
class FourVector(object):
    '''
    An implementation of four vectors in relativity
    practise the  __init__ method
    '''
    
    def __init__(self, ct = 0, *r):
        self.ct = ct
        if r:
            self.x, self.y, self.z = r
        else:
            self.x, self.y, self.z = 0,0,0
         
        
    def __repr__(self):
        return 'FourVector(ct=%g, r=[%g, %g, %g])' %(self.ct,self.x,self.y,self.z)
        
    def __str__(self):
        return '(%g, %g, %g, %g)' %(self.ct, self.x, self.y, self.z)