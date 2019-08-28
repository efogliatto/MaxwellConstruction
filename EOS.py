from .VdWEos import VdWEos

from .CSEos import CSEos

from .PREos import PREos


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


        
    elif(eos_name == 'Peng-Robinson'):

        a = 0.5

        b = 4.0

        w = 0.344
        
        if 'a' in kwargs:

            a = kwargs['a']

        if 'b' in kwargs:

            b = kwargs['b']

        if 'w' in kwargs:

            w = kwargs['w']            
            
        
        eos = PREos(a, b, w)      

        
    else:
        print('Undefined EOS')


    return eos
