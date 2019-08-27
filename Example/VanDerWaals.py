import MaxwellConstruction as mx

import vdWColumn as Column

import numpy as np

import matplotlib.pyplot as plt



# Solucion analitica

analitica = [ [], [], [] ]

for T in np.linspace(0.5, 0.99, int((0.99-0.5)/0.01)):
    
    cl, cg = Column.interphaseDensities(T)

    analitica[0].append(T)

    analitica[1].append(cl)

    analitica[2].append(cg)


plt.plot( analitica[1], analitica[0], label = 'Analítico', color='r')
plt.plot( analitica[2], analitica[0], linestyle = '-', color='r')




# Construccion usando integral

vdw = mx.EOS('VanDerWaals')

for T in [0.9, 0.8, 0.7, 0.6]:

    Vrmin,Vrmax = mx.coexistencia(vdw, T, plotPV=False, Vspace=(0.43,20,2000))    

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

plt.legend(loc='best')

plt.show()

