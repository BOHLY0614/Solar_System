from timeit import repeat
from turtle import color
import matplotlib.pyplot as plt
from matplotlib import animation
from List import *
from calculs import *
from constantes import *
from anim import *
import numpy as np

#Initialisation
earth_xlist,earth_ylist=[],[]
mars_xlist,mars_ylist=[],[]
jupiter_xlist,jupiter_ylist=[],[]
p=0

#Calcul des positions (ici que de la terre on va négliger le déplacement du mouvement pour l'instant)
t=0
while t<4380*delta_t:
    update_e=actu(earth,sun)
    earth_xlist.append(update_e[0])
    earth_ylist.append(update_e[1])
    update_ma=actu(mars,sun)
    mars_xlist.append(update_ma[0])
    mars_ylist.append(update_ma[1])
    update_j=actu(jupiter,sun)
    jupiter_xlist.append(update_j[0])
    jupiter_ylist.append(update_j[1])

    t+=delta_t

#-------------------------------------------------------------------------------------------------------------------------
#début de l'animation

#Mise en place de l'animation stylée
fig, ax = plt.subplots(figsize=(10,10))
ax.set_aspect('equal')
ax.grid()
#Initialisation des paramètres de tracés
earth_plot=casP(earth,ax)
mars_plot=casP(mars,ax)
jupiter_plot=casP(jupiter,ax)
figure_s, =ax.plot([],[],marker="o",markersize=15,markerfacecolor='yellow')
descr_s=ax.text(0,0,"Soleil")
earth_xdata,earth_ydata=[],[]
mars_xdata,mars_ydata=[],[]
jupiter_xdata,jupiter_ydata=[],[]

stock_coord=[earth_plot,mars_plot,jupiter_plot]
stock_modifpos=[earth_xlist,earth_ylist,mars_xlist,mars_ylist,jupiter_xlist,jupiter_ylist]
stock_trace=[earth_xdata,earth_ydata,mars_xdata,mars_ydata,jupiter_xdata,jupiter_ydata]
def animate(k):
    n=0
    a=[]

    #On stock les données pour le tracé
    earth_xdata.append(earth_xlist[k])
    earth_ydata.append(earth_ylist[k])
    mars_xdata.append(mars_xlist[k])
    mars_ydata.append(mars_ylist[k])
    jupiter_xdata.append(jupiter_xlist[k])
    jupiter_ydata.append(jupiter_ylist[k])

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
    figure_s.set_data(0,0)
    descr_s.set_position((0,0))

    ax.axis('equal')
    ax.set_xlim(-8*earth.x,8*earth.x)
    ax.set_ylim(-8*earth.x,8*earth.x)
    return tuple(a)

while p==0:
    ani = animation.FuncAnimation(fig=fig, func=animate, frames=len(earth_xlist), interval=1,blit=True,repeat=False)
    plt.show()
    ani.frame_seq = ani.new_frame_seq()
