from planete import *

#le soleil est placé à 0,0 car centre de notre système (et sans vitesse initiale). De plus, nous démarerons à l'apogée
sun=planete(2e30,0,0,0,0,"Soleil",10,"yellow")
earth=planete(5.972e24,1.52e11,0,0,29e3,"Terre",6,"blue")
mars=planete(6.41e23,2.27e11,0,0,.245e5,"Mars",3,"red")
jupiter=planete(1.9e27,8.17e11,0,0,.124e5,"Jupiter",10,"orange")