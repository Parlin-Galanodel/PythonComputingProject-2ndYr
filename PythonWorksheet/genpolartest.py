###################################
# Genpolar test
###################################
import genpolar
import matplotlib.pyplot as plt
from math import sin, cos


#test of rt pairs func
'''
if __name__=='__main__':
    R = [0.0, 0.1, 0.2]
    T = [1, 10, 20]
    l=[]
    for r,t in genpolar.rtpairs(R, T):
            plt.plot(r * cos(t), r * sin(t), 'bo')
            l.append((r * cos(t), r * sin(t)))
    plt.show()
    print l
'''

#test of rtuniform()
if __name__=='__main__':
    for r,t in genpolar.rtuniform(10, 0.1, 6):
        plt.plot(r*cos(t), r*sin(t), 'bo')
    #plt.autoscale(True,'both')
    #plt.axis('equal')
    plt.axis('scaled')
    plt.grid('on', color='b', linestyle='--',linewidth='1')
    plt.show()