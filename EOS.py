from .VdWEos import VdWEos

from .CSEos import CSEos


def EOS(eos_name='VanDerWaals', **kwargs):
    
    """
    Ecuacion de estado.

    
    """

    if(eos_name == 'VanDerWaals'):

        a = 0.5

        b = 4.0
        
        if 'a' in kwargs:

            a = kwargs['a']

        if 'b' in kwargs:

            b = kwargs['b']
            
        
        eos = VdWEos(a, b)


    elif(eos_name == 'Carnahan-Starling'):

        a = 0.5

        b = 4.0
        
        if 'a' in kwargs:

            a = kwargs['a']

        if 'b' in kwargs:

            b = kwargs['b']
            
        
        eos = CSEos(a, b)        

        
    else:
        print('Undefined EOS')


    return eos
