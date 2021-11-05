#!/usr/bin/python3
# Escriba un programa en python 3 que determine la ocurrencia de c/u de las vocales

texto = input("ingrese un texto/frase/nombre: ")

vocales = ["a", "e", "i", "o", "u", "á",  "é", "í", "ó", "ú", "A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú"]

for x in vocales: #Funcion para determinar la cantidad de vocales
    veces=0
    for y in texto:
        if x==y:
            veces+=1
    print("La vocal", x, "aparece", veces, "veces")