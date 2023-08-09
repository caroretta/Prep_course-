# Herramientas_3.py
#Para modulo 8

class Herramientas_3:
    def __init__(self,lista_n):
        if (type(lista_n) != list):
            self.lista_n = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista_n = lista_n

    def primo(self,x):  
        "Verifica si es primo"
        primo = True
        for div in range(2, x):
                if (x % div == 0):
                    primo = False
                    break
        return primo
    
    def verificar_primo(self):
        resultados_primo=[]
        for i in self.lista_n:
            if(self.primo(i)):
                #primo=str(i) + "es un numero primo"
                resultados_primo.append(True)
            else:
                #no_primo=str(i) +"no es un numero primo"
                resultados_primo.append(False)
        return resultados_primo
     
    def mas_repetido(self):
        unitario=[]
        repetidos=[]
        cantidad_de_veces=[]
        mayor=0
        menor=0 
    
        for i in self.lista_n:
            if  self.lista_n.count(i)>1:
                if not(i in repetidos):
                    repetidos.append(i)
                    cantidad_de_veces.append(self.lista_n.count(i))
                else:
                    unitario.append(i)

        for j, x in enumerate(cantidad_de_veces):
            if x>mayor:
                mayor=x
                numero=j
            else:
                menor=x
        resultado = "Mayor cantidad de repeticiones: " + str(mayor) + "\n"
        
        for h, y in enumerate(repetidos):
            if numero==h:
                
                resultado += "El numero más repetido es: " + str(y)
        return resultado
    
    def conversion_lista(self,origen,destino):

        parametros_esperados = ['celsius','kelvin','farenheit']
        lista_conversion = []
        resultado_conversion=[]
        if str(origen) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        
        for j in self.lista_n:
            resultado_conversion.append(self.conversion(j,origen,destino))
        return resultado_conversion
    
    def conversion(self,valor,origen,destino):

        valor_flo=float(valor)
        celsius= (valor_flo - 32)/1.8
        celsius_k=valor_flo-273.15

        if origen=="celsius":
            if destino=="fahrenheit":
                fahrenheit = valor_flo * (9/5) + 32
                #print(f"{valor_flo} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit")
                return fahrenheit
            elif destino=="kelvin":
                kelvin=valor_flo + 273.15
                #print(f"{valor_flo} grados Celsius equivalen a {kelvin:.2f} grados Kelvin")
                return kelvin
            elif destino=="celsius":
                #print(f"{valor_flo} grados Celsius equivalen a {valor_flo:.2f} grados Celsius")
                return valor_flo
            else:
                print("Conversion destino incorrecto")
        elif origen=="fahrenheit":
            if destino=="celsius":
                #print(f"{valor_flo} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius")
                return celsius
            elif destino=="kelvin":
                kelvin_fahr= celsius + 273.15
                #print(f"{valor_flo} grados Fahrenheit equivalen a {kelvin_fahr:.2f} grados Kelvin")
                return kelvin_fahr
            elif destino=="fahrenheit":
                #print(f"{valor_flo} grados Fahrenheit equivalen a {valor_flo:.2f} grados Fahrenheit")
                return valor_flo
            else:
                print("Conversion destino incorrecto")
        elif origen=="kelvin":
            if destino=="celsius":
                #print(f"{valor_flo} grados Kelvin equivalen a {celsius_k:.2f} grados Celsius")
               return celsius_k
            elif destino=="fahrenheit":
                fahrenheit_k= ((celsius_k*1.8)+32)
                #print(f"{valor_flo} grados Kelvin equivalen a {fahrenheit_k:.2f} grados Fahrenheit")
                return fahrenheit_k
            elif destino=="kelvin":
                #print(f"{valor_flo} grados Kelvin equivalen a {valor_flo:.2f} grados Kelvin")
                return valor_flo
            else:
                print("Conversion destino incorrecto")
        else:
            print("Conversion origen incorrecto")
        
    
    def factorial_lista(self):
        f1=[]
        for y in self.lista_n:
            f1.append(self.factorial(y))
            #re_factorial= "El factorial de" + str(y) + "es" + str(f1)
        return f1
    
    def factorial(self,numero):
        "Calcula el factorial de un numero"
        if type(numero)!= int:
            return "El numero debe ser un entero"
        if numero<0:
            return "El numero debe ser positivo"
        if numero<=1:
            return 1
        if (numero>1):
            numero=numero* self.factorial(numero-1)
        return numero
    