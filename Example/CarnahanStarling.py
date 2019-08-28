import MaxwellConstruction as mx


# Construccion usando integral

cs = mx.EOS('Carnahan-Starling')

Vrmin,Vrmax = mx.coexistencia(cs, 0.7, plotPV=True, Vspace=(0.35,50,1000))    

