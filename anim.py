import matplotlib.pyplot as plt
from matplotlib import animation
from List import *

def casP(a,ax):
    trace, =ax.plot([],[],color=a.color)
    figure, =ax.plot([a.x], [0], marker='o', markersize=a.size, markerfacecolor=a.color)
    descr=ax.text(a.x, 0, a.nom)
    return trace,figure,descr
