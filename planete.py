from msilib.schema import MsiAssembly
from xml.dom.pulldom import default_bufsize
from xml.sax.handler import feature_external_ges


class planete:
    counter=0
    def __init__(self,masse,x,y,vx,vy,nom,size,color):
        self.masse=masse 
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.nom=nom
        self.size=size
        self.color=color
        planete.counter+=1




