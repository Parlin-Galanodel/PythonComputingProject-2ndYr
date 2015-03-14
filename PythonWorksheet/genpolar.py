from math import pi
def rtpairs(R,T):
    pairs=zip(R,T)
    for r,t in pairs:
        n=0
        while n <= t:
            x=r,n*2*pi/t
            n+=1
            yield x

def rtuniform(n, rmax, m):
    R=[]
    T=[]
    for i in xrange(n+1):
        R.append(1.*i*rmax/n)
        T.append(1.*i*m)
    T[0]=1
    return rtpairs(R,T)