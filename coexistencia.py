import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.integrate import quadrature
from scipy.optimize import newton
from scipy.signal import argrelextrema
from PyAstronomy import pyaC



def coexistencia(eos, Tr, plotPV=False, plotLog=False, Vspace=(0.4,50,10000), root_method = 'step'):
    """
    Densidades de coexistencia

    Argumentos
    eos: Ecuacion de estado
    T: temperatura reducida
    plotPV: Grafico de presion-volumen
    Vspace: rango de volumen reducido para analizar. (start, stop, nsteps)
    """


    Vr = np.linspace(Vspace[0], Vspace[1], Vspace[2])

    pr = eos.Pr(Tr, Vr)



    # Initial guess for the position of the Maxwell construction line:
    # the volume corresponding to the mean pressure between the minimum and
    # maximum in reduced pressure, pr.
    iprmin = argrelextrema(pr, np.less)
    iprmax = argrelextrema(pr, np.greater)
    Vr0 = np.mean([Vr[iprmin], Vr[iprmax]])



    def get_Vlims(pr0):
        
        """Cruce por cero de pr0 - pr
        
        Devuelve solo los extremos
        """

        Vextreme = pyaC.zerocross1d(Vr, pr0-pr)              

        # Excepciones
        assert len(Vextreme) == 3, '{} intersecciones entre PV y pr0. Posiblemente sea necesario modificar los límites de Vr'.format(len(Vextreme))
        
        return Vextreme[0], Vextreme[2]
    
    

    def get_area_difference(Vr0):
        """Return the difference in areas of the van der Waals loops.

        Return the difference between the areas of the loops from Vr0 to Vrmax
        and from Vrmin to Vr0 where the reduced pressure from the van der Waals
        equation is the same at Vrmin, Vr0 and Vrmax. This difference is zero
        when the straight line joining Vrmin and Vrmax at pr0 is the Maxwell
        construction.

        """

        pr0 = eos.Pr(Tr, Vr0)
        Vrmin, Vrmax = get_Vlims(pr0)
        # return quad(lambda vr: eos.Pr(Tr, vr) - pr0, Vrmin, Vrmax)[0]
        return quadrature(lambda vr: eos.Pr(Tr, vr) - pr0, Vrmin, Vrmax, maxiter=1000, tol=1e-10)[0]



    def step(adiff, Vr0):
        """
        Busqueda de igualdad de areas mediante la reducci\'on progresiva de Vr0.
        Lento pero robusto. Util cuando no funciona Newton
        """

        fdiff = np.float64(get_area_difference(Vr0))

        sdiff = fdiff

        v0 = Vr0
        v1 = Vr0
    
        while np.greater(fdiff*sdiff,0):
            v0 = v1
            v1 = 0.999*v1
            sdiff = np.float64(get_area_difference(v1))
    
        return 0.5*v0 + 0.5*v1
            
    



    # Calculo de Vr0 que iguala las areas

    if root_method == 'newton':
        
        Vr0 = newton(get_area_difference, Vr0)

    elif root_method == 'step':

        Vr0 = step(get_area_difference, Vr0)

    else:

        assert True, 'Unknown method'
        


    # Estimacion de p0 y limites

    pr0 = eos.Pr(Tr, Vr0)
    
    Vrmin, Vrmax = get_Vlims(pr0)    

    



    if plotPV:
        
        plt.plot(Vr, pr, linewidth=2, color='r')

        plt.axhline(pr0)

        Vrslice = []

        prslice = []

        for i in range(len(Vr)):

            if (Vr[i]>=Vrmin) and (Vr[i]<=Vrmax):

                Vrslice.append(Vr[i])

                prslice.append(pr[i])
        
        
        plt.fill_between(Vrslice, pr0, prslice, interpolate=True, alpha=0.3)

        if plotLog:
            plt.yscale('log')
            plt.xscale('log')
            
        plt.xlabel('Volumen molar reducido')

        plt.ylabel('Presion reducida')        

        plt.show()


        

    return Vrmin,Vrmax
