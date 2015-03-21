'''
    This module is a final version of packed function used to do single 
    spherical refracting surface.
'''
# the function module contains all the things we need, import all its contens
# to the global name space.
from functions import *

s_argv = input('input the arguments of the spherical refraction surface\n'\
               'in the order psoition, curvature, n1, n2 and radius'\
               'seperate by comma:\n')

print 'generating surface...'
s = rt.SphericalRefraction(*s_argv)
print 'done.'


raybundle_argv = input('input the parameters of ray bundle you want to generate\n'\
                       'in the order of raybundle radius, [x coordinate of center\n'\
                       'y coordinate of the center, ray direction as a vector\n'\
                       'number of layers, ratio of points to layer]:\n')

print 'generating raybundle...'
if type(raybundle_argv) is not tuple:
    raybundle = bundlesOfRays(raybundle_argv)
else:
    raybundle = bundlesOfRays(*raybundle_argv)
print 'done.'

print 'analysing...'

plt.figure()
plot_the_source_plane(raybundle)
plt.title('source plane')

plt.figure()
plot_ray_trace(raybundle, s)
plt.title('ray trace')

plt.figure()
plot_output_spot(raybundle)
plt.title('output spot')

rms=[]
for i in raybundle:
    x, y, z = i.p()
    lsquare = x**2 + y**2
    rms.append(lsquare)
temp = sum(rms)
RMS = 1.*temp/len(rms)
maximum = max(rms)**0.5
minimum = min(rms)**0.5

print 'maximum raidus is %g' % maximum
print 'minimum radius is %g' % minimum
print 'RMS spot radius is %g' % RMS

plt.show()





















