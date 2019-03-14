"""
>>> conversion = ConversorTemperatura('CaF',100) #estas son pruebas unitarias que nos permiten #realizar las pruebas necesarias sin tener que
>>> conversion.CalcularIgualdadTemperatura()#realizar las pruebas necesarias sin tener que crer otro archivo python para realizarlas mediante
>>> conversion.getIgualdaddeTemperatura()#el simbolo del sistema
212.0

>>> conversion = ConversorTemperatura('FaC',100)# esta tambien es prueba unitaria y en esta colocamos los parametro ocupados
>>> conversion.CalcularIgualdadTemperatura()# en esta parte le decimos que realice el metodo donde estan las acciones
>>> conversion.getIgualdaddeTemperatura() # aqui mandamos a llamar el parametro de salida y el la linea de abajo el resultado esperado
37.77777777777778
"""

class ConversorTemperatura: #declaramos nuestra clase con este nombre referente a lo que realizara
    __temperatura = float(0) #en esta variable almacenaremos la cantidad de temperatura a convertir
    __conversion = '' # en esta variable almacenaremos la conversion que nesecitamos de una a otra o viceversa
    __igualdadTemperatura = float(0) # aqui guardaremos el valor final de la conversion

    def __init__(self, conversion, temperatura): # declaramos nuestro metodo constructor y definimos los parametros de entrada
        self.__conversion = conversion
        self.__temperatura = temperatura

    def CalcularIgualdadTemperatura(self): # declaramos el metdo que realizara la conversion de temperaturas
        if(self.__conversion == 'CaF'): # este if con su condicion indica que se realizara una de las conversiones
            self.__igualdadTemperatura = ((1.8*self.__temperatura)+32) # realiza la conversion de las temperaturas y el resultado lo almacena el la variable de salida
        elif (self.__conversion == 'FaC'): # este elif indica que si no se cumple la primera sera esta la condicion que se cumpla
            self.__igualdadTemperatura = ((self.__temperatura-32)/1.8)
        else: # este el es por si ninguna de las ateriores condicones se cumple
            self.__igualdadTemperatura = 'Error de datos'

    def getIgualdaddeTemperatura(self): # en este metodo se le declara para mostrar el dato de salida
        return self.__igualdadTemperatura

if __name__ == '__main__':     # para poder realizar las pruebas unitarias en el simbolo del sistema solo con (python  nombre.py e python  nombre.py -v)
    import doctest
    doctest.testmod()
#python  nombre.py sirve para ejecutar el programa
#python  nombre.py -v sirve para ver las operaciones que se realizaron el el programa