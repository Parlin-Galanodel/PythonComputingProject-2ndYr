'''
    This module is a final version of packed function used to do planoconvex
    lens, it is modified from single_surface module.
'''
# the function module contains all the things we need, import all its contens
# to the global name space.
from functions import *

s_argv = input('input the arguments of the planoconvex lens\n'\
               'in the order psoition, curvature, refractive index and separation\n'\
               'seperate by comma:\n')


raybundle_argv = input('input the parameters of ray bundle you want to generate\n'\
                       'in the order of raybundle radius, [x coordinate of center\n'\
                       'y coordinate of the center, ray direction as a vector\n'\
                       'number of layers, ratio of points to layer]:\n')


s = rt.Planoconvex(*s_argv)
s_argv = 'lens arguments: %s' %repr(s_argv)

if type(raybundle_argv) is not tuple:
    raybundle = bundlesOfRays(raybundle_argv)
    r_argv = raybundle_argv
    r_argv = 'ray source radius: %s' %r_argv
else:
    raybundle = bundlesOfRays(*raybundle_argv)
    r_argv = raybundle_argv[0]
    r_argv = 'ray source radius: %s' %r_argv


plt.subplot(221)
plot_the_source_plane(raybundle)
plt.title('source plane')

plt.subplot(222)
plot_ray_trace(raybundle, s)
plt.title('ray trace')

plt.subplot(223)
plot_output_spot(raybundle)
plt.title('output spot')

rms=[]
for i in raybundle:
    x, y, z = i.p()
    lsquare = x**2 + y**2
    rms.append(lsquare)

plt.subplot(224)
temp = sum(rms)
RMS = 1.*temp/len(rms)
maximum = max(rms)**0.5
minimum = min(rms)**0.5
l = map(lambda x:x**0.5,rms)
avrgl = 1.*sum(l)/len(l)


s0 = 'spot RMS is: %g' % RMS
s1 = 'spot average radius is: %g' % avrgl
s2 = 'spot Maximum radius is: %g' % maximum
s3 = 'spot Minimum radius is: %g' % minimum

plt.text(0.02, 0.9, s_argv)
plt.text(0.02, 0.75, r_argv)
plt.text(0.02, 0.6, s0)
plt.text(0.02, 0.45, s1)
plt.text(0.02, 0.3, s2)
plt.text(0.02, 0.15, s3)
plt.title('statistics')

plt.show()
