from constantes import *
from planete import *

def G_const(M1,M2):
    gconst=G*M1*M2
    return gconst

def distance(xm,xs,ym,ys):
    dx=xm-xs
    dy=ym-ys
    return dx,dy

#on veut la modification d'un vecteur (on prendra la norme de r cube)
def rcube(dx,dy):
    r=(dx**2+dy**2)**1.5
    return r

#force appliquée à l'objet en mouvement (m)
def force(gconst,dx,dy,r3):
    fx=-gconst*dx/r3
    fy=-gconst*dy/r3
    return fx,fy

#actualisation de la position par intervalle de temps
def actu(a,b):
    d=distance(a.x,b.x,a.y,b.y)
    r3=rcube(d[0],d[1])
    f=force(G_const(a.masse,b.masse),d[0],d[1],r3)
    a.vx+=(f[0]*delta_t)/a.masse
    a.vy+=(f[1]*delta_t)/a.masse
    a.x+=a.vx*delta_t
    a.y+=a.vy*delta_t
    return a.x,a.y



