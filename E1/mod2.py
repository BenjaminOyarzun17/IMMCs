# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:44:20 2020

@author: Cesar
"""


import random

class Auto:
    def __init__(self,pasajeros):
        self.pasajeros = pasajeros
    
class Minibus:
    def __init__(self,pasajeros):
        self.pasajeros = pasajeros
    

def obtenerGananciaRandom():
    autos,motos,buses,minibuses = 0,0,0,0
    objAutos = []
    objMinibuses = []
    cantidadVehiculos = autos+motos+buses+minibuses
    if cantidadVehiculos == 0:
        cantidadVehiculos = 1
        
    promedioAuto = 100*autos/cantidadVehiculos
    promedioMoto = 100*motos/cantidadVehiculos
    promedioBuses = 100*buses/cantidadVehiculos
    promedioMinibuses = 100*minibuses/cantidadVehiculos
    while 5*autos + 2/3*motos + 13*buses+ 8*minibuses > 52 or 5*autos + 2/3*motos + 13*buses+ 8*minibuses < 48:
        
        autos = random.randint(5,9)#1,10
        motos = random.randint(1,3)#78
        buses = random.randint(1,2)
        minibuses = random.randint(1,2)
        
    else:
        for auto in range(autos):
            objAutos.append(Auto(random.randint(1,3)))#max = 9
            #objAutos.append(Auto(1))
        for minibus in range(minibuses):
            objMinibuses.append(Minibus(random.randint(1,15)))
            #objMinibuses.append(Minibus(1))
        dineroExtraAutos = []
        dineroExtraMinibuses = []
        for auto in objAutos:
            #print(f"pasajeros del auto numero {objAutos.index(auto)+1}: {auto.pasajeros}")
            dineroExtraAutos.append(800*auto.pasajeros-500*(auto.pasajeros-1))
        for minibus in objMinibuses:
            #print(f"pasajeros del minibus numero {objMinibuses.index(minibus)+1}: {minibus.pasajeros}")
            dineroExtraMinibuses.append(2600*minibus.pasajeros-2500*minibus.pasajeros-2500)
        tarifaAuto = 19300
        tarifaMoto = 7700
        tarifaBus = 50100
        tarifaMinibus = 30800
        #print(f"autos: {autos}, buses:{buses}, minibuses:{minibuses}, motos:{motos}")
        
        gananciaBase = autos*tarifaAuto+motos*tarifaMoto+buses*tarifaBus+minibuses*tarifaMinibus
        gananciaTotal = sum(dineroExtraMinibuses) + sum(dineroExtraAutos) + gananciaBase
        #print(f"ganancia de la columna: ${gananciaTotal}")
        return gananciaTotal  

    


intentosBuenos = []
intentosMalos = []
ganancias = []
for i in range(5):
    for i in range(10000):
        ganancia = obtenerGananciaRandom()
        if ganancia < 200000:
            intentosMalos.append(1)
            ganancias.append(ganancia)
            
        elif ganancia >=200000:
            intentosBuenos.append(1)
            ganancias.append(ganancia)
    fallido = sum(intentosMalos)
    bueno = sum(intentosBuenos)
    razon = fallido/bueno
    print(f"fallido: {fallido}")
    print(f"acertado: {bueno}")
    print(f"razon = {razon}")
    
print(3*sum(ganancias)/len(ganancias)-600000)
print("gol de maradona")
