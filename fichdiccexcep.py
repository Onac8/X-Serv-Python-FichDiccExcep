#!/usr/bin/python3
# -*- coding: utf-8 -*-

fich = open('/etc/passwd', 'r')
lineas = fich.readlines()
fich.close()

dicc = {}

for linea in lineas:
    elementos = linea.split(':')
    #print (elementos[0], elementos[-1][:-1]) #el 1º y ultimo - \n
    dicc[elementos[0]] = elementos[-1][:-1] #key + value

print(dicc['root'])
try: #Exceptions in python3
    print(dicc['imaginario'])
except KeyError:
    print("[imaginario]: Oops! That key isn't in my dictionary.")
