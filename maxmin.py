'''
Este programa te permite comparar 2 numeros usando funciones y luego ver la cantidad de veces que cada funcion se llamo
'''

maxCalled = 0
minCalled = 0

def max_val(a,b):
    '''
    Esta funcion te dice cual es el numero mayor entre 2 que recibe
        
    
    :param a: Primer numero a comparar
    :type a: int
    
    :param b: Segundo numero a comparar
    :type b: int
    
    :return: Regresa el valor mas grande de los 2
    :rtype: int
    
    '''

    global maxCalled
    maxCalled = maxCalled + 1
  
    if(a > b):
        return a   
    elif(b > a):
        return b
    else:
        return a

def min_val(a,b):
    '''
    Esta funcion te dice cual es el numero menor entre 2 que recibe
    
    
    :param a: Primer numero a comparar
    :type a: int
    
    :param b: Segundo numero a comparar
    :type b: int
    
    :return: Regresa el valor mas pequeño de los 2
    :rtype: int
    
    '''
    global minCalled 
    minCalled = minCalled + 1
  
    if(a < b):
        return a
    elif(b < a):
        return b
    else:
        return a 

def print_usage(init_msg, max_val=True, min_val=True):
    '''
    Esta funcion te dice la cantidad de veces que cada una de las funciones anteriores fue llamada
    
    :param init_msg: EL mensaje inicial a imprimir
    :type init_msg: str
    
    :param max_val: Esta se usa para determinar si se va a imprimir el uso de la funcion max_val
    :type max_val: bool
    
    :param min_val: Se usa para determinar si se va a imprimir el uso de la funcion min_val
    :type min_val: bool
   
    '''
    global maxCalled, minCalled
    print (init_msg)
    if max_val:
        print('functin max_val was called', maxCalled, ' times')
    if min_val:
        print('function min_val was called', minCalled, ' times')

if __name__ == '__main__':
    print('Calling function max_val')
    max_val(1,4)
    max_val(2,b=1)
    max_val(b=4,a=3)

    print('Calling function min_val')
    min_val(1,4)
    min_val(2,4)
    min_val(4,b=9)

    print_usage('The usage of functions min_val and max_val')
