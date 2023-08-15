import csv
from datetime import datetime
import os

def agregar_medicion(temperatura, humedad, llovio):
    # Obtener la marca de tiempo actual
    marca_tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Crear una lista con los datos a guardar
    medicion = [marca_tiempo, temperatura, humedad, llovio]
    
    # Si el archivo CSV no existe, agregar encabezados
    if not os.path.exists('clase10_ej2.csv'):
        with open('clase10_ej2.csv', mode='w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(["Marca de Tiempo", "Temperatura", "Humedad", "Llovio"])
    
    # Abrir el archivo CSV en modo append y escribir la medicion
    with open('clase10_ej2.csv', mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(medicion)
    
    print("Medición agregada al archivo.")

# Obtener los valores de temperatura, humedad y llovio desde el usuario
temperatura = float(input("Ingrese la temperatura en grados centígrados: "))
humedad = float(input("Ingrese el valor de humedad: "))
llovio = input("¿Llovió? (True/False): ").lower() == 'true'

# Llamar a la función para agregar la medición al archivo CSV
agregar_medicion(temperatura, humedad, llovio)