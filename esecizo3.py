
#Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma. Poi crea le classi Quadrato e Cerchio che ereditino dalla classe Forma e che implementino il metodo area() in modo appropriato per ogni forma. Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.

import math


class Forma:
    def __init__(self,area):
        self.area=area

class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__(lato)


    




#class Cerchio(Forma):
