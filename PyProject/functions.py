# import essential modules
'''
    In this module, some essential functions used to check the modules were defined and could
    These functions be used to do plottings of ray trace.
'''
import raytracer as rt      # raytracer module which defined ray, spherical and output plane 
                            # classes
                            
import genpolar as gp       # module for task 15 in worksheet
import matplotlib.pyplot as plt
from math import sin, cos


# initial test to make sure rt module works fine.
if __name__ == '__main__':
'''
    test for ray tracer module to make sure it would work as expected.
'''
    # A spherical surface s at z=100 with curvature 0.03 and refractive indices
    # n1=1.0 and n2=1.5, it would focus light
    s = rt.SphericalRefraction(100,0.03,1.0,1.5,100)
    # An output plane at z=250
    o = rt.OutputPlane(300)
    # Try to trace one ray passing through s and o, plot it.
    test_ray=rt.Ray((1.01,0,0),(0.01,0,1))
    # negative curv surface would diverse light
    s2 = rt.SphericalRefraction(150,-0.03,1.0,1.5,100)
    # negative curv while as part of convex would still focus light
    s3 = rt.SphericalRefraction(200,-0.03,1.2,1.0,100)
    s.propagate_ray(test_ray)
    s2.propagate_ray(test_ray)
    s3.propagate_ray(test_ray)
    o.propagate_ray(test_ray)
    points = test_ray.vertices()
    x, y, z = zip(*points)
    plt.figure()
    plt.plot(z,x,'r-')
        # the consequence is very good, do not repeat it any more.
    
    

# The algorithm to find focal point
def FocalPoint(spherical_refraction, ray=None):
    '''
        estimate the focal point by simulating a single beam parallel and 
        close to z-axis. If ray is not provided, this function would use 
        a ray from 10**-8 to z-axis as default.
    '''
    # this function is not complete and so it is only valid for convex.
    if ray is None:         # I set this to be None since ray is mutable object
                            # and could be changed by this function when it is 
                            # used several times and give a wrong answer.
        ray = rt.Ray([10**-8,0,0],[0,0,1])
    # firstly, we propagate the ray by lens
    spherical_refraction.propagate_ray(ray)
    # get the intercept and direction after lens
    p=ray.p()
    k=ray.k()
    # since focal point is on z-axis, x,y coordinates should be 0
    l = 1.0*(0 - p[0])/k[0]
    focal_point = p + l*k
    # z coordinate of focal_point is the position of focal_point.
    z = focal_point[-1]
    return z

    
# # The FocalPoint would be helpful to set an OutputPlane on an optical lens'
# # focal plane, for example:
# o2 = rt.OutputPlane(FocalPoint(s))


def bundlesOfRays(radius, x_shift = 0, y_shift = 0, ray_direction=(0,0,1),\
                    n = 10, m = 6):
    '''
        generate a bundle of rays by using the rtuniform function in genpolar module
        and store the rays in a list, radius is the radius of the bundles of 
        rays, x y shift is how much we would shift the bundles of rays in x, y 
        direction, ray direction is the direction of the rays and n,m is the 
        setting of how much loops and ration of how many times points in nth loop.
    '''
    tmp = []            # temple container
    bundlesOfRays = []
    for r,t in gp.rtuniform(n,radius,m):
        tmp.append((r*cos(t) + x_shift, r*sin(t) + y_shift, 0))
    for i in tmp:
        ray = rt.Ray(i,ray_direction)
        bundlesOfRays.append(ray)
    return bundlesOfRays

def plot_the_source_plane(bundlesOfRays):
    '''
        plot the bundlesOfRays' source position
    '''
    for i in bundlesOfRays:
        x,y,z = i.vertices()[0]
        plt.plot(x,y,'r.')
    plt.axis('equal')

def plot_ray_trace(bundlesOfRays, SphericalRefraction, \
                    outpput_plane=None,type=None):
    '''
        plot the ray trace of a bundlesOfRays passing a SphericalRefraction
        and end at the focal plane of the SphericalRefraction.
    '''
    if outpput_plane is None:
        output_plane = rt.OutputPlane(FocalPoint(SphericalRefraction))
    else:
        output_plane = rt.OutputPlane(outpput_plane)
    if type is None:
        for i in bundlesOfRays:
            SphericalRefraction.propagate_ray(i)
            output_plane.propagate_ray(i)
            x, y, z = zip(*i.vertices())
            plt.plot(z, x)
    else:
        for i in bundlesOfRays:
            SphericalRefraction.propagate_ray(i)
            output_plane.propagate_ray(i)
            x, y, z = zip(*i.vertices())
            plt.plot(z, x, marks)
        
        
def plot_output_spot(raybundle,marks=None):
    '''
        plot the output spot of a bundle of rays on output plane.
        the ray bundle should be propagated through lens manually.
    '''
    for ray in raybundle:
        if marks is None:
            plt.plot(ray.p()[0], ray.p()[1],'r.')
        else:
            plt.plot(ray.p()[0], ray.p()[1],marks)
        plt.axis('equal')
        
# test bundlesOfRays, plot_the_source_plane, plot_ray_trace functions
# and plot_output_spot function.
if __name__ == '__main__':
''' 
    unit test for functions defined in this module 
'''
    raybundle = bundlesOfRays(5, 0, 0, (0.1, 0, 1), 5, 6)
    raybundle2 = bundlesOfRays(5, 0, 0, (0, 0, 1), 5, 6)
    raybundle3 = bundlesOfRays(5, -5, 0, (0, 0, 1), 5, 6)
    plt.figure()
    plot_the_source_plane(raybundle)
    plt.figure()
    plot_ray_trace(raybundle, s)
    plot_ray_trace(raybundle2, s)
    plot_ray_trace(raybundle3, s)
    plt.figure()
    o2=rt.OutputPlane(FocalPoint(s))
    plot_output_spot(raybundle,'r.')
    plt.axis('equal')
    plot_output_spot(raybundle2,'b.')
    plt.axis('equal')
    plot_output_spot(raybundle3,'g.')
    plt.axis('equal')
    plt.axis('equal')
    plt.show()












