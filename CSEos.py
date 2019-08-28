import numpy as np


class CSEos:
    
    "Ecuaci\'on de estado de Carnahan-Starling"

    def __init__(self,a,b):
        self.__a = a
        self.__b = b
        pass

    def Pr(self,T,v):
        "Presi\'on reducida"

        rho = 1/v

        c = 0.13045*rho
        
        return 2.786*rho*( T*(1 + c + c*c - c*c*c)/(1.0-c)**3 - 1.3829*rho )


    def Tc(self):
        "Temperatura cr\'itica"

        return self.__a * 0.18727 / (self.__b * 0.4963)


    def Pc(self):
        "Presi\'on cr\'itica"

        return 0.18727 * self.Tc() / self.__b
    

    def rhoc(self):
        "Densidad cr\'itica"

        return 0.5218 / self.__b        

    
    def __str__(self):
        msg = 'Ecuacion de estado de Carnahan-Starling. \na={}\nb={}'.format(self.__a,self.__b)
        return msg
