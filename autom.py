from planete import *
from List import *
import matplotlib.pyplot as plt
from matplotlib import animation

stock=[earth,sun,mars]

def casP(a,ax):
    trace, =ax.plot([],[],color=a.color)
    figure, =ax.plot([a.x], [0], marker='o', markersize=a.size, markerfacecolor=a.color)
    descr=ax.text(a.x, 0, a.nom)
    return trace,figure,descr

def init():
    fig, ax = plt.subplots(figsize=(20,20))
    ax.set_aspect('equal')
    ax.grid()
    trace_all,figure_all,descr_all=[],[],[]
    for i in range(planete.counter):
        planete=casP(i)
        trace_all.append(stock[0])
        figure_all.append(stock[1])
        descr_all.append(stock[2])
    return trace_all,figure_all,descr_all




