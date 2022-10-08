from timeit import repeat
from turtle import color
import matplotlib.pyplot as plt
from matplotlib import animation
from List import *
from calculs import *
from constantes import *
from anim import *

#Initialisation
exlist,eylist=[],[]
maxlist,maylist=[],[]
jxlist,jylist=[],[]
p=0

#Calcul des positions (ici que de la terre on va négliger le déplacement du mouvement pour l'instant)
t=0
while t<4380*delta_t:
    update_e=actu(earth,sun)
    exlist.append(update_e[0])
    eylist.append(update_e[1])
    update_ma=actu(mars,sun)
    maxlist.append(update_ma[0])
    maylist.append(update_ma[1])
    update_j=actu(jupiter,sun)
    jxlist.append(update_j[0])
    jylist.append(update_j[1])

    t+=delta_t

#-------------------------------------------------------------------------------------------------------------------------
#début de l'animation

#Mise en place de l'animation stylée
fig, ax = plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
ax.grid()
#Initialisation des paramètres de tracés
T=casP(earth,ax)
Ma=casP(mars,ax)
J=casP(jupiter,ax)
figure_s, =ax.plot([],[],marker="o",markersize=15,markerfacecolor='yellow')
descr_s=ax.text(0,0,"Soleil")
exdata,eydata=[],[]
maxdata,maydata=[],[]
jxdata,jydata=[],[]

stock_coord=[T,Ma,J]
stock_modifpos=[exlist,eylist,maxlist,maxlist,jxlist,jxlist]
stock_trace=[exdata,eydata,maxdata,maydata,jxdata,jydata]
print(planete.counter)
def animate(k):
    n=0
    a=[]

    #On stock les données pour le tracé
    exdata.append(exlist[k])
    eydata.append(eylist[k])
    maxdata.append(maxlist[k])
    maydata.append(maylist[k])
    jxdata.append(jxlist[k])
    jydata.append(jylist[k])

    #cas des astres en mouvements
    for i in range(planete.counter-1):
        stock_coord[i][0].set_data(stock_trace[n],stock_trace[n+1])
        stock_coord[i][1].set_data(stock_modifpos[n][k],stock_modifpos[n+1][k])
        stock_coord[i][2].set_position((stock_modifpos[n][k],stock_modifpos[n+1][k]))
        a.append(stock_coord[i][0])
        a.append(stock_coord[i][1])
        a.append(stock_coord[i][2])
        n+=2
    #cas du soleil

    ax.axis('equal')
    ax.set_xlim(-8*earth.x,8*earth.x)
    ax.set_ylim(-8*earth.x,8*earth.x)
    return tuple(a)

while p==0:
    ani = animation.FuncAnimation(fig=fig, func=animate, frames=len(exlist), interval=1,blit=True,repeat=False)
    plt.show()
    ani.frame_seq = ani.new_frame_seq()
