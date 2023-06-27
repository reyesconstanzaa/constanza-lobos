from mailbox import NoSuchMailboxError
from traceback import print_tb
import numpy as np
import csv


class pelicula:
        def __init__(self, nombre):
            self.nombre = nombre
            self.asientos = [["." for _ in range(15)] for _ in range(10)]


def mostrar_menu(peliculas):
    print("peliculas en cartelera")
    for i, pelicula in enumerate(peliculas):
        print(f"{i + 1}.{pelicula.nombre}")
        print("0. salir")


def mostrar_asientos(pelicula):
    print("asientos para la pelicula: ", pelicula.nombre)
    print(" ABCDEFGHIJKLMNO")
    for i, fila in enumerate(pelicula.asientos, start=1):
        print(f"{i:2}", end="")
        print("".join(fila))


def comprar_entrada(pelicula, es_alumno):
    nombre=input("ingrese su nombre: ")
    fila_columna = input("ingrese la fila y columna (Ejemplo: 1B): ")
    fila, columna = int(fila_columna[ :-1]) - 1, ord(fila_columna[-1]) - ord("A") 
    if pelicula.asientos[fila][columna] == "x" :
     print("el asiento ya esta reservado") 
     return
    elif pelicula.asientos[fila][columna] == ".":
        pelicula.asientos[fila][columna] = "x" 
        descuento = 0.3 if es_alumno else 0.0
        print("Compra exitosa!!")
        print("Nombre: ", nombre)
        print("Asientos: ", fila_columna)
        print("Descuento de Estudiante:", "si" if es_alumno else "No" )
        print("Total a pagar: ", calcular_precio(descuento))
    else:
        print("El asiento no esta disponible.") 


def calcular_precio(descuento):
    precio_base = 10 #precio base de una entrada
    precio_final = precio_base - (precio_base * descuento)
    return precio_final


def guardar_boleta(pelicula, nombre):
    with open("boleta.csv", "a", newline="") as archivo:
        writer = csv.writer(archivo) 
        for i, fila  in enumerate(pelicula.asientos):
            writer.writerow([pelicula.nombre])
            for j, asientos in enumerate(fila):
                if asiento == "X":
                    writer.writerow([pelicula.nombre, f"{i+1}{chr(j+ord("A"))}", nombre])

def listar_boletas():
    with open("boleta.csv", "r") as archivo:
        reader = csv.reader(archivo)
        print("boleta emitidas: ")
        for boleta in reader:
             print("pelicula", boleta[0])
             print("Asiento", boleta[1])
             print("Nombre", boleta[2])


def cargar_peliculas():
    peliculas = []
    with open ("peliculas.csv","r") as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            pelicula = pelicula(row[0])
            peliculas.append(pelicula)
            for _ in range (10):
                fila = next(reader)
                pelicula.asientos.append(fila)
                return pelicula




    

    






    

        
