import numpy as np


class VdWEos:
    
    "Ecuaci\'on de estado de Van der Waals"

    def __init__(self,a,b):
        self.__a = a
        self.__b = b
        pass

    def Pr(self,T,v):
        "Presi\'on reducida"
        
        return 8.*T/(3.*v - 1.) - 3./v**2


    def Tc(self):
        "Temperatura cr\'itica"

        return 8. * self.__a / (27. * self.__b)


    def Pc(self):
        "Presi\'on cr\'itica"

        return self.__a / (27. * self.__b**2)

    def rhoc(self):
        "Densidad cr\'itica"

        return 1. / (3. * self.__b)

    
    def __str__(self):
        msg = 'Ecuacion de estado de VanDerWaals. \na={}\nb={}'.format(self.__a,self.__b)
        return msg
