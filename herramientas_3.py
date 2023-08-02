# Herramientas_3.py
#Para modulo 8

class Herramientas_3:
    def __init__(self,lista_n):
        self.lista_n=lista_n

    def primo(self,x):  
        "Verifica si es primo"
        primo = True
        for div in range(2, x):
                if (x % div == 0):
                    primo = False
                    break
        return primo
    
    def verificar_primo(self):
        for i in self.lista_n:
            if(self.primo(i)):
                print(i,"es un numero primo")
            else:
                print(i,"no es un numero primo")

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
        print("Mayor cantidad de repeticiones:",mayor)
        
        for h, y in enumerate(repetidos):
            if numero==h:
                numero_1=y
        print("El numero más repetido es:",numero_1)

    def conversion_lista(self,origen,destino):

        for j in self.lista_n:
            self.conversion(j,origen,destino)

    def conversion(self,valor,origen,destino):

        valor_flo=float(valor)
        celsius= (valor_flo - 32)/1.8
        celsius_k=valor_flo-273.15

        if origen=="celsius":
            if destino=="fahrenheit":
                fahrenheit = valor_flo * (9/5) + 32
                print(f"{valor_flo} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit")
            elif destino=="kelvin":
                kelvin=valor_flo + 273.15
                print(f"{valor_flo} grados Celsius equivalen a {kelvin:.2f} grados Kelvin")
            elif destino=="celsius":
                print(f"{valor_flo} grados Celsius equivalen a {valor_flo:.2f} grados Celsius")
            else:
                print("Conversion destino incorrecto")
        elif origen=="fahrenheit":
            if destino=="celsius":
                print(f"{valor_flo} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius")
            elif destino=="kelvin":
                kelvin_fahr= celsius + 273.15
                print(f"{valor_flo} grados Fahrenheit equivalen a {kelvin_fahr:.2f} grados Kelvin")
            elif destino=="fahrenheit":
                print(f"{valor_flo} grados Fahrenheit equivalen a {valor_flo:.2f} grados Fahrenheit")
            else:
                print("Conversion destino incorrecto")
        elif origen=="kelvin":
            if destino=="celsius":
                print(f"{valor_flo} grados Kelvin equivalen a {celsius_k:.2f} grados Celsius")
            elif destino=="fahrenheit":
                fahrenheit_k= ((celsius_k*1.8)+32)
                print(f"{valor_flo} grados Kelvin equivalen a {fahrenheit_k:.2f} grados Fahrenheit")
            elif destino=="kelvin":
                print(f"{valor_flo} grados Kelvin equivalen a {valor_flo:.2f} grados Kelvin")
            else:
                print("Conversion destino incorrecto")
        else:
            print("Conversion origen incorrecto")

    def factorial_lista(self):
        for y in self.lista_n:
            print("El factorial de",y,"es",self.factorial(y))

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
    