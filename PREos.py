import numpy as np


class PREos:
    
    "Ecuaci\'on de estado de Carnahan-Starling"

    def __init__(self,a,b,w):
        self.__a = a
        self.__b = b
        self.__w = w        
        pass

    def Pr(self,T,v):
        "Presi\'on reducida"

        phi = ( 1. + (0.37464 + 1.54226 * self.__w - 0.26992 * self.__w * self.__w) * (1 - np.sqrt(T))  )**2
        
        rho = self.rhoc()/v

        p = rho * T * self.Tc() / (1. - rho * self.__b)  -  self.__a * phi * rho * rho / ( 1.  +  2. * self.__b * rho  -  self.__b * self.__b * rho * rho )
        
        return p/self.Pc()


    def Tc(self):
        "Temperatura cr\'itica"

        return 0.0778 * self.__a / (0.45724 * self.__b)    


    def Pc(self):
        "Presi\'on cr\'itica"

        return 0.0778 * self.Tc() / self.__b
    

    def rhoc(self):
        "Densidad cr\'itica"

        return 0.253077 / self.__b

    
    def __str__(self):
        msg = 'Ecuacion de estado de Peng-Robinson. \na={}\nb={}\nw={}'.format(self.__a,self.__b,self.__w)
        return msg
