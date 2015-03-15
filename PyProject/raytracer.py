# Task 1:
'''
The Project aimed to build a 3D raytracer to investigate the
imaging performance of simple lenses and optimise the design
of a biconvex lens
'''

from numpy import array as na

from numpy import dot, cross        # inner product and cross product
                                    # of two numpy array
from math import sqrt
from numpy.linalg import norm #, inv  # norm of vector or matrix
                                    # inverse of a matrix
                                    # inv is not need any more
                                    
#from numpy import matrix           # do not need it any more

def normalise(v):               #normalise a vector
    '''
        A func used to normalise a vector
    '''
    normv=norm(v)
    return 1.*v/normv      # 1. is used to convert potential int to float.



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
        self.__currentPoint=na(r1)      # na is numpy array
        self.__direction=na(r2)         # r1 & r2 converted to array
        self.__points=[(self.__currentPoint, self.__direction)]
        
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
                # as the ray. For robust consideration 
        '''
            append a new point and direction to the ray
            p, k must be 3D array (same dimension with r1, r2
        '''
        p=na(p)     # p, k converted to numpy array for consistency
        if k is None:   # is operator is used here since when 
                        # an array compared to None, error occurs
            k=self.__direction
        k=na(k)     # k is a numpy array
        temp=p,k    # convert p, k to a tuple for appending
        self.__points.append(temp)
        
    def vertices(self):
        '''
            return all the points along the ray
        '''
        return zip(*self.__points)[0] #unpack self.__point to list of 
                                      #points and direction, then return
                                      #point part
                                      
class OpticalElement(object):         #provided OpticalElement class
                                      #it is a general base class
    def propagate_ray(self, ray):
        "propagate a ray through the optical element"
        raise NotImplementedError()
            
            
# Task 3: SphericalRefraction class
class SphericalRefraction(OpticalElement):
    def __init__(self, z0=1, curvature=0.1, n1=1, n2=1.2,\
                 aperture_radius=30):    # default value just for convenience
                                         # in testing code
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
        self.__z0=z0
        self.__curvature=curvature
        self.__n1=n1
        self.__n2=n2
        self.__aperture_radius=aperture_radius
        
    # Task 4
    def intercept(self,ray):
        '''
            calculates the first valid intercept of a ray with the
            spherical surface. 0 curvature is dealt as a special 
            case. If there is no valid intercept, the function
            returns None.
        '''
        p=ray.p()
        k=normalise(ray.k())        
        if self.__curvature != 0:
            # Find the parameter would be used firstly           
            R=1./self.__curvature
            O=1.*na((0,0,self.__z0+R))
            r=p-O
            # Do the calculation
#            assert dot(r,k)-dot(r,r)+R**2
#            assert type(r)==type(k)
            if ((dot(r,k))**2-dot(r,r)+R**2) <0:
                return None   # no intercept
            l1=-dot(r,k)+sqrt((dot(r,k))**2-dot(r,r)+R**2)
            l2=-dot(r,k)-sqrt((dot(r,k))**2-dot(r,r)+R**2)
            if l1==l2:
                return None
            elif R>0:
                l=min(l1,l2)
            else:
                l=max(l1,l2)
            intercept_point=p+l*k
        else:
            # curvature of the optical element is 0,
            # then it is just a flat surface
            l=(1.*self.__z0-p[2])/k[2]
            intercept_point=p+l*k
        apturerad=reduce(lambda x,y:x**2+y**2, \
                            intercept_point[:-1])
        if apturerad <= self.__aperture_radius**2:      # intercept is on the 
                                                        # lens
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
                # # # # This is just [in(theta2)]**2, but could be used 
                # # # # to judge whether total reflected or not.
        # # # if sin_theta2 >= 1:
            # # # return None
        # # # else:
            # # # #do the calculation by converting and converting and converting
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
    # Martix method is stupid and complex compared to the formula I found online
            
            
            # Rewrite it by Snell's law in 3D, vector form to be exactly.
            # The formula comes from StarkEffects.com
            # (http://www.starkeffects.com/snells-law-vector.shtml)
        Nn=-1.*N     #negative N, since the formula use N as norm toward Incident
        n=1.*n1/n2*cross(Nn,cross(N,k))-Nn*sqrt(1.-(1.*n1/n2)**2* \
            dot(cross(Nn,k),cross(Nn,k)))
            # n is a unit vector represent the direction of refracted wave.
            
        temp_vector=cross(k,N)      # cross product for finding sin(theta1)
        temp=norm(temp_vector)      # norm is sin(theta1)
        if 1.*n1/n2*temp < 1:       # refraction angle less than 90 degree
            return n
        else:
            return None
        
    #Task 6.
    def propagate_ray(self,ray):
        new_point=self.intercept(ray)
        if new_point is None:  # is operator is used here since when 
                               # an array compared to None, error occurs
            return None            #do nothing when no intercept point
        else:
            k=normalise(ray.k())
            n1=self.__n1
            n2=self.__n2
            if self.__curvature == 0:
                N=1.*na([0,0,1])
            elif self.__curvature > 0:
                R=1./self.__curvature
                O=na((0,0,1.*self.__z0+R))
                p=ray.p()
                N=O-p
                N=normalise(N)
            else:
                R=1./self.__curvature
                O=na((0,0,1.*self.__z0+R))
                p=ray.p()
                N=p-O
                N=normalise(N)
            v=self.refraction(k,N,n1,n2)
            if v is None:   # is operator is used here since when 
                            # an array compared to None, error occurs
                return None        #do nothing if total reflected
            else:
                ray.append(new_point,v)
                return None # this func always return None even though
                            # the ray is updated by the func.
                # By returning None, the ray without valid intercept or 
                # diffract direction are abandoned.
    
# Task 8.
# Write a class OutputPlane, that is an OpticalElement. Implement
# methods intercept and propagate_ray.
class OutputPlane(SphericalRefraction):
    # the OutputPlane was required to be an OpticalElement, so it 
    # is a subclass of SphericalRefraction which is an subclass
    # of OpticalElement.
    '''
        The object worked as screen behind any lens used in 
        this experiment.
    '''
    def __init__(self, position):
        z0=position
        curvature=0                 # outputplane is flat plane
        n1=n2=1                     # No refraction
        aperture_radius=1000        # Screen must be big enough
        super(OutputPlane,self).__init__()




   
# Task 7.Test your code. Create a refracting surface and a ray and check
# propagate_ray correctly propagates and refracts the ray. Try a range
# of initial rays to check your refracting object behaves as you expect.
if __name__=='__main__':
    # testing parameters
    ray1_argv=([0,0,0],[10,10,3])   # no intercept
    ray2_argv=([0,0,0],[1,1,0.5])   # intercept
    ray3_argv=([4,0,0],[0,0,3])     # perpendicular
    lens1_argv=(1,0.025,1,1.5,5)    # glass lens1 with curvature
    lens2_argv=(2,0,1,1.5,5)        # plane surface
    lens3_argv=(3,-0.025,1,1.5,5)   # negative curvature
    r1=Ray(*ray1_argv)
    r2=Ray(*ray2_argv)
    r3=Ray(*ray3_argv)
    s1=SphericalRefraction(*lens1_argv)
    s2=SphericalRefraction(*lens2_argv)
    s3=SphericalRefraction(*lens3_argv)
    ray=r1,r2,r3
    lens=s1,s2,s3
    c=1
    for i in ray:
        for j in lens:
            print c,
            print ("intercept:%s\n") %str(j.intercept(i))
            print ("ray parameters: p:%s,\n\t"
                "k:%s,\n\t"
                "vertices:%s\n") %(i.p(), i.k(), i.vertices())
            j.propagate_ray(i)
            print ("ray parameters: p:%s,\n\t"
                "k:%s,\n\t"
                "vertices:%s\n") %(i.p(), i.k(), i.vertices())
            c+=1
            print ("###########################################"\
            "############\n")
 
 
            
   
    
    
    