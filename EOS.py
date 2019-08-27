from .VdWEos import VdWEos

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


    else:
        print('Undefined EOS')


    return eos
