import numpy as np


class VdWEos:
    
    "Ecuaci\'on de estado de Van der Waals"

    def __init__(self,a,b):
        self.__a = np.float64(a)
        self.__b = np.float64(b)
        pass

    def Pr(self,T,v):
        "Presi\'on reducida"
        
        return np.float64( 8.*T/(3.*v - 1.) - 3./v**2 )


    def Tc(self):
        "Temperatura cr\'itica"

        return np.float64( 8. * self.__a / (27. * self.__b) )


    def Pc(self):
        "Presi\'on cr\'itica"

        return np.float64( self.__a / (27. * self.__b**2) )

    def rhoc(self):
        "Densidad cr\'itica"

        return np.float64( 1. / (3. * self.__b) )

    def hvl(self, rhol, rhov, T):
        "Calor latente"
        hv = np.float64( (3./2. + 1/(1.-self.__b*rhov))*T - 2.*self.__a*rhov )
        hl = np.float64( (3./2. + 1/(1.-self.__b*rhol))*T - 2.*self.__a*rhol )
        return (hv - hl)
        
    
    def __str__(self):
        msg = 'Ecuacion de estado de VanDerWaals. \na={}\nb={}'.format(self.__a,self.__b)
        return msg
