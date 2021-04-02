# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:49:32 2020

@author: Daniel
"""


def ruteo(distancias: dict, ruta_inicial: list)-> dict:
    
    # Se validan los datos del diccionario 
    validacion = True
    datos = distancias.items()
    for clave, valor in datos:
        if clave[0] == clave[1] and valor != 0:
            validacion = False
        if clave[0] != clave[1] and valor <= 0:
            validacion = False 
    
    # si son validos los datos, se ejecuta para encontrar la mejor ruta        
    if validacion == True:
        
        # Se calcula la distancia de la ruta inicial 
        mejor_distancia = 0
        for i in range (len(ruta_inicial)-1):
            mejor_distancia += distancias[ (ruta_inicial[i],ruta_inicial[i+1] ) ]
        
        
        ruta_actual = ruta_inicial.copy()
        mejoro = True
        while mejoro == True:
            
            mejoro = False
            
            # se crean las parejas a intercambiar 
            for i in range (1,len(ruta_actual)-1):
                a = ruta_actual[i]
                
                for j in range (i+1, len(ruta_actual)-1):
                    b = ruta_actual[j]
                    pareja = (a,b)
                    
                    # se halla la ruta con las parejas intercambiadas  
                    ruta_intercambiada = ruta_actual.copy()
                    ruta_intercambiada[i] = b
                    ruta_intercambiada[j] = a 
                    
                    #calculo la distancia de la ruta intercambiada  
                    distancia_intercambio = 0             
                    for n in range (len(ruta_intercambiada)-1):
                        distancia_intercambio += distancias[(ruta_intercambiada[n],ruta_intercambiada[n+1] )]
                    
                    # se guarda la mejor distancia 
                    if distancia_intercambio < mejor_distancia:
                        mejor_distancia = distancia_intercambio
                        mejor_ruta_iteracion = ruta_intercambiada.copy()
                        mejoro = True
            
            # si existe una mejor ruta, vuelvo hacer el recorrido con la mejor ruta.    
            if mejoro == True:
                ruta_actual = mejor_ruta_iteracion.copy()
        
        # mejor ruta
        return dict(ruta = '-'.join(ruta_actual), distancia = mejor_distancia)
    
    # si no son validos los datos, se imprime un mensaje         
    else:
        return ("Por favor revisar los datos de entrada.")
    
distancias = {
    ('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

ruta_inicial= ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

print(ruteo(distancias, ruta_inicial))
