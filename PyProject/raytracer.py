# Task 1: Write a doc string for this module
'''
The Project aimed to build a 3D raytracer to investigate the
imaging performance of simple lenses and optimise the design
of a biconvex lens
'''

from numpy import array as na
from numpy import dot, cross            # inner product and cross product
                                        # of two numpy array
from math import sqrt                   # square root function in math module
from numpy.linalg import norm   #, inv  # norm of vector or matrix
                                        # inverse of a matrix
                                        # inv is not need any more
                                    
#from numpy import matrix               # do not need it any more
                                        # matrix method is abandoned

def normalise(v):               # normalise a vector
                                # this function would be used latter
    '''
        A func used to normalise a vector
    '''
    normv = norm(v)
    return 1.*v/normv      # 1. is used to convert potential int to
                           # float.



# Task 2, Ray class:
class Ray(object):
    '''
        Ray class is used to model a ray, it contains the coordinates
        need by a ray vector and could provide some method to 
        modify the ray itself
    '''
    
    def __init__(self,r1=[0,0,0],r2=[1,1,1]):
        '''
            initialization method which could be provide two 3D
            list as parameters, these two list would be converted
            to the coordinate of current point and direction respectively.
        '''
        self.__currentPoint = na(r1)      # na is numpy array
        self.__direction = na(r2)         # r1 & r2 converted to array
        # I do not want to change these two initial attributes, so I create
        # a list used to store the position and direction pairs as a
        # description of this ray instead of initialising current point
        # and direction to be two lists.
        self.__points = [(self.__currentPoint, self.__direction)]
            # Considering about the initial direction is set by user, 
            # original vector would be read comfortably when users
            # want to check the original value and so I do not normalise
            # it here.
        
    def p(self):
        '''
            A function to extract the current point
        '''
        return self.__points[-1][0]
        
    def k(self):
        '''
            A function to extract the current ray direction
        '''
        return self.__points[-1][1]
        
    def append(self, p, k=None):
                # if k not given, it would be seen as same direction
                # as the ray. For robust consideration because
                # I might append point manually in testing. It is 
                # not convenient to get k value every time.
        '''
            append a new point and direction to the ray
            p, k must be 3D array (same dimension with r1, r2
        '''
        p = na(p)       # p, k converted to numpy array for consistency
        if k is None:   # is operator is used here since when 
                        # an array compared to None, error occurs
            k = self.__direction
        k = na(k)       # k is a numpy array
        temp = p,k      # convert p, k to a tuple for appending
        self.__points.append(temp)
        
    def vertices(self):
        '''
            return all the points along the ray
        '''
        return zip(*self.__points)[0] # unpack self.__point to list of 
                                      # points and direction, then return
                                      # point part
    
    def points(self):
        # return all the points on the ray by position and direction pairs
        # I think this gives better description of the ray. 
        return self.__points
        
    def __repr__(self):               # representation of ray.
        p = zip(*self.__points)[0]
        k = zip(*self.__points)[1]
        return "A ray:\n""ray points: %s \n"\
               "ray direction: %s \n" %(p, k)
                                      
class OpticalElement(object):       # provided OpticalElement class
                                      # it is a general base class
    def propagate_ray(self, ray):
        "propagate a ray through the optical element"
        raise NotImplementedError()
            
            
# Task 3: SphericalRefraction class
class SphericalRefraction(OpticalElement):

    def __init__(self, z0=1, curvature=0.1, n1=1, n2=1.2,\
                 aperture_radius=30):    # default value just for convenience
                                         # in testing code, no special meanings
        """
           spherical refracting surface centred on the optical axis
           which can be represented by five parameters:
                1. z0 - the intercept of the surface with the z-axis
                2. curvature - the curvature of the surface
                    (use the convention that a positive curvature
                     corresponds to the centre of curvature at z>z0 
                     and negative curvature corresponds to a centre 
                     of curvature at z<z0. A curvature of zero 
                     corresponds to a plane surface (i.e., infinite
                     radius of curvature.))
                3. n1, n2 - the refractive indices either side of the
                    surface
                4. aperture radius - the maximum extent of the surface
                    from the optical axis
        """
        self.__z0 = z0
        self.__curvature = curvature
        self.__n1 = n1
        self.__n2 = n2
        self.__aperture_radius = aperture_radius
        
    def __repr__(self):     # representation method to display a spherical refraction
        a = (self.__z0,self.__curvature,self.__n1,self.__n2,self.__aperture_radius)
        return 'z0= %s\ncurvature= %s\nn1= %s,\tn2=%s\nradius=%s' %a
        
    # Task 4
    def intercept(self,ray):
        '''
            calculates the first valid intercept of a ray with the
            spherical surface. 0 curvature is dealt as a special 
            case. If there is no valid intercept, the function
            returns None.
        '''
        p = ray.p()
        k = normalise(ray.k())        
        if self.__curvature != 0:
            # Find the parameter would be used firstly           
            R = 1./self.__curvature           # radius of the lens
            O = 1.*na((0,0,self.__z0+R))      # position of the centre of lens
            r = p-O                           # r vector in the graph on page 20
                                              # of my lab book
            # Do the calculation
            #assert dot(r,k)-dot(r,r)+R**2   # old check step
            #assert type(r)==type(k)         # old check step
            if ((dot(r,k))**2-dot(r,r)+R**2) <= 0:    # delta < 0, no solution
                return None   # no intercept
                # if l1 == l2,two same solution which means tangency, there is 
                # no valid intercept.
                
            # when delta >=0 the two solutions are below
            l1 = -dot(r,k) + sqrt((dot(r,k))**2-dot(r,r)+R**2)
            l2 = -dot(r,k) - sqrt((dot(r,k))**2-dot(r,r)+R**2)
            # l1, l2 are two different solutions, only one is the valid intercept
            # we want.
            if R > 0:
                l = min(l1,l2)      # smaller value is true l
            else:
                l = max(l1,l2)      # greater value is true l
            intercept_point = p + l*k
        else:
            # curvature of the optical element is 0,
            # then it is just a flat surface
            l = (1.*self.__z0-p[2])/k[2]
            intercept_point = p + l*k
        # The intercept must lie in the sphericalRefraction to be valid, which
        # means that radius of the intercept is smaller than aperture_radius
        # of the refraction.
        apture_rad = reduce(lambda x,y:x**2+y**2, \
                            intercept_point[:-1])
        if apture_rad <= self.__aperture_radius**2:
            return intercept_point
        else:
            return None
    
    #Task 5.
    def refraction(self,k,N,n1,n2):
        '''
            This function refract the ray by Snell's law. It takes 
            4 parameters, incident direction, surface normal,
            and the refractive indices n1 and n2. It should return the 
            refracted ray direction (a unit vector).
            If the ray is subject to total internal reflection,
            it returns None.
        '''
        # # # sin_theta1=cross(k,N) #This vector's norm is sin(theta1)
        # # # sin_theta2=sin_theta1*n1/n2 #This vector's norm is sin(theta2)
        # # # sin_theta2=sin_theta2*sin_theta2
        # # # sin_theta2=sin_theta2[0]**2+sin_theta2[1]**2+sin_theta2[2]**2
                # # # # # This is just [in(theta2)]**2, but could be used 
                # # # # # to judge whether total reflected or not.
        # # # if sin_theta2 >= 1:
            # # # return None
        # # # else:
            # # # # #do the calculation by converting and converting and converting
            # # # M=[[0,-n2*N[2],n2*N[1]],[-n2*N[2],0,n2*N[0]],[-n2*N[1],\
                # # # n2*N[0],0]]
            # # # M=matrix(M)
            # # # X=matrix(n1*sin_theta1)
            # # # X=X.reshape(3,1)
            # # # M=inv(M)
            # # # d=M*X
            # # # d=d.reshape(1,3)
            # # # d=na(a)
            # # # d=d[0][0],d[0][1],d[0][2]
            # # # d=na(d)
            # # # return normalise(d)

    # Matrix method is stupid and complex compared to the formula I found online
                        
            # Rewrite it by Snell's law in 3D, or vector form.
            # I am worried on using theta in formula and so I do not use
            # the formula on wikipedia.
            # The formula comes from StarkEffects.com
            # (http://www.starkeffects.com/snells-law-vector.shtml)
        Nn = -1.*N  #negative N, since the formula use N as norm toward Incident
        n = 1.*n1/n2*cross(Nn,cross(N,k))-Nn*sqrt(1.-(1.*n1/n2)**2* \
            dot(cross(Nn,k),cross(Nn,k)))
            #n is a unit vector represent the direction of refracted wave.

    # It is another formula from wikipedia of Snell's Law below, I used it to do a double check
    # of the formula above to make sure the consequence is true.
        #~ r=n1/n2; c=dot(N,k);
        #~ n=r*k-(r*c-sqrt(1.-r**2*(1-c**2)))*N
            
        temp_vector=cross(k,N)      # cross product for finding sin(theta1)
        temp = norm(temp_vector)    # norm is sin(theta1)

        if 1.*n1/n2*temp < 1:       # refraction angle less than 90 degree
            return n
        else:
            return None
        
    #Task 6.
    def propagate_ray(self,ray):
        new_point = self.intercept(ray)
        if new_point is None:       # is operator is used here since when 
                                    # an array compared to None, future warning
                                    # occurs, it is not a disaster but annoyed.                                    
            return None         # do nothing when no intercept point
        else: 
            # k, n1, n2 are parameters would be used to find 
            # refract direction
            k = normalise(ray.k())
            n1 = self.__n1
            n2 = self.__n2
            if self.__curvature == 0:
                # curvature==0 yield a unit vector along z-axis
                N=1.*na([0,0,1])
            elif self.__curvature > 0:
            # curvature>0, N is vector PO(P is interception, O is centre
            # of the sphericalRefraction)
                R = 1./self.__curvature
                O = na((0, 0, self.__z0+R))
                p = new_point
                N = O-p
                N = normalise(N)
            else:
            # if curvature<0, the only difference is that N vector is 
            # OP instead of PO
                R = 1./self.__curvature
                O = na((0, 0, self.__z0+R))
                p = new_point
                N = p-O
                N = normalise(N)
            v = self.refraction(k,N,n1,n2)
            # refraction function would give None if total reflection occurred
            if v is None:   # is operator is used here since when 
                            # an array compared to None, interpreter 
                            # would give a warning, that dose not stop
                            # the program but it's very annoying.
                return None         #do nothing if total reflected
            else:
                ray.append(new_point,v)
                return None # this func always return None even though
                            # the ray is updated by the function
                # By returning None, the ray without valid intercept or 
                # refract direction are abandoned.
    
# Task 8.
# Write a class OutputPlane, that is an OpticalElement. Implement
# methods intercept and propagate_ray.
class OutputPlane(SphericalRefraction):
    # the OutputPlane was required to be an OpticalElement.
    # Considering about it is a special case of SphericalRefraction(curvature
    # =0, refraction index on both sides are equal, big radius.
    # I made it a subclass of SphericalRefraction which is an subclass
    # of OpticalElement instead of inheriting from OpticalElement directly.
    '''
        The object worked as screen behind any lens used in 
        this experiment. In initialising OutputPlane, only its
        position, a.k.a, z0 was necessary.
    '''
    def __init__(self, position=10):
        z0 = position
        curvature = 0                 # output plane is flat plane
        n1 = n2 = 1                     # No refraction
        aperture_radius = 10000        # Screen must be big enough
        super(OutputPlane,self).__init__(z0,curvature,n1,n2,aperture_radius)
    

   
# Task 7.Test your code. Create a refracting surface and a ray and check
# propagate_ray correctly propagates and refracts the ray. Try a range
# of initial rays to check your refracting object behaves as you expect.
if __name__ == '__main__':
    # testing parameters, argument values for rays and lens
    ray1_argv = ([0,0,0],[10,10,3])         # no intercept
    ray2_argv = ([0,0,0],[1,1,3])        # intercept with an angle
    ray3_argv = ([4,0,0],[0,0,3])       # parallel to z-axis but not perpendicular
                                        # to the surface
    ray4_argv = ([0,0,0],[0,0,3])       # z-axis
    lens1_argv = (5,0.005,1,1.2,10)     # glass lens1 with positive curvature
    lens2_argv = (10,0,1.5,1.5,10)      # plane surface
    lens3_argv = (15,-0.005,1.5,0.7,20) # negative curvature
    # generate rays and lens by arguments above.
    r1 = Ray(*ray1_argv)
    r2 = Ray(*ray2_argv)
    r3 = Ray(*ray3_argv)
    r4 = Ray(*ray4_argv)
    s1 = SphericalRefraction(*lens1_argv)
    s2 = SphericalRefraction(*lens2_argv)
    s3 = SphericalRefraction(*lens3_argv)
    ray = r1,r2,r3,r4
    lens = s1,s2,s3
    O = OutputPlane(20)         # OutputPlane at z0=20
    c = 1                       # counter used to mark different rays
    import matplotlib.pyplot as plt
    # propagate rays through three lens and then propagate it onto output plane
    for i in ray:
        for j in lens:
            print c
            print "intercept:%s\n" %str(j.intercept(i))
            j.propagate_ray(i)
        O.propagate_ray(i)
        print i,'\n'
        print ("###########################################"\
            "############\n")
        c+=1
    for i in ray:
        x,y,z = zip(*i.vertices())
        print '~~~~~~~~~~~~~~~~~~'
        print z
        print x
        plt.plot(z,y)
    print s1
    print s2
    print s3
    plt.show()
    
class Planoconvex(OpticalElement):
    '''
        This is the class to describe a planoconvex, Z0 is the position near
        on z-axis near to light source, separation is the distance on z-axis
        between the two surface, refractive_index is the refractive_index
        in lens.
    '''
    def __init__(self, z0, curvature, separation, refractive_index):
        # generate two surfaces of the lens.
        if curvature > 0:
            aperture_radius = sqrt(2./curvature*separation-separation*separation)
            
            s_front = SphericalRefraction(z0, curvature, 1, refractive_index,\
                                          aperture_radius)
            s_back = SphericalRefraction(z0+separation, 0, refractive_index,\
                                         1, aperture_radius)
        elif curvature <0:
            aperture_radius = sqrt(-2.*separation/curvature-separation*separation)
            
            s_front = SphericalRefraction(z0, 0, 1, refractive_index,\
                                          aperture_radius)
            s_back = SphericalRefraction(z0+separation, curvature, \
                                         refractive_index,\
                                         1, aperture_radius)
        else:
            raise Exception('At least one curved surface')
        
        # binding the two surfaces to instance of planoconvex
        self.s1 = s_front
        self.s2 = s_back
            
    def propagate_ray(self, ray):
        self.s1.propagate_ray(ray)
        self.s2.propagate_ray(ray)
        
    def __repr__(self):
        s1 = str(self.s1)
        s2 = str(self.s2)
        s = 'Front surface:\n' + s1 + '\n' + 'Back surface:\n' + s2
        return s
                                     
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
