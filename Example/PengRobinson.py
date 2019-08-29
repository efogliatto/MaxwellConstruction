import MaxwellConstruction as mx

import matplotlib.pyplot as plt

import numpy as np


# # Solucion de referencia

# CS_vapor = np.loadtxt('CS_vapor.dat', unpack = True)

# CS_liquid = np.loadtxt('CS_liquid.dat', unpack = True)

# plt.plot(CS_vapor[0], CS_vapor[1], linestyle='-', color='b', label='Referencia')

# plt.plot(CS_liquid[0], CS_liquid[1], linestyle='-', color='b')



# Construccion usando integral

prob = mx.EOS('Peng-Robinson', a = 3./49., b = 2./21., w = 0.344)

for i,T in enumerate(np.linspace(0.5,0.99,10)):

    if T >= 0.8:
        Vrmin,Vrmax = mx.coexistencia(prob, T, plotPV=False, Vspace=(0.3,50,10000))

    else:
        Vrmin,Vrmax = mx.coexistencia(prob, T, plotPV=False, Vspace=(0.28,4000,200000))        

    
    

    if i == 1:
    
        plt.plot(1/Vrmin,
                 T,
                 linestyle = 'None',
                 color = 'k',
                 marker = 'o',
                 mfc = 'None',
                 label = 'Integral')

    else:
        
        plt.plot(1/Vrmin,
                 T,
                 linestyle = 'None',
                 color = 'k',
                 marker = 'o',
                 mfc = 'None')        

    plt.plot(1/Vrmax,
             T,
             linestyle = 'None',
             color = 'k',
             marker = 'o',
             mfc = 'None')
    
    


# Labels

plt.ylabel('$T_r$', rotation='horizontal', labelpad=15)

plt.xlabel(r'$\rho_r$')

plt.xscale('log')

plt.legend(loc='best')

plt.show()




# # Unico caso

# prob = mx.EOS('Peng-Robinson', a = 3./49., b = 2./21., w = 0.344)

# Vrmin,Vrmax = mx.coexistencia(prob, 0.5, plotPV=True, plotLog=True, Vspace=(0.28,4000,200000))


