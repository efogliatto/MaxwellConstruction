import MaxwellConstruction as mx


# Construccion usando integral

cs = mx.EOS('Carnahan-Starling')

Vrmin,Vrmax = mx.coexistencia(cs, 0.9, plotPV=True, Vspace=(0.43,10,500))    



# for T in [0.9, 0.8, 0.7, 0.6]:

#     Vrmin,Vrmax = mx.coexistencia(vdw, T, plotPV=False, Vspace=(0.43,20,2000))    

#     plt.plot(1/Vrmin,
#              T,
#              linestyle = 'None',
#              color = 'k',
#              marker = 'o',
#              mfc = 'None')

#     plt.plot(1/Vrmax,
#              T,
#              linestyle = 'None',
#              color = 'k',
#              marker = 'o',
#              mfc = 'None')

# # Labels

# plt.ylabel('$T_r$', rotation='horizontal', labelpad=15)

# plt.xlabel(r'$\rho_r$')

# plt.legend(loc='best')

# plt.show()

