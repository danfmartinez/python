# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 17:40:15 2020

@author: Daniel
"""

def prestamo(informacion: dict) -> dict:
    
    # definimos las variables 
    i_d = informacion["ingreso_deudor"] #float
    i_c = informacion["ingreso_codeudor"] #float
    c_p = informacion["cantidad_prestamo"] #float
    I = informacion["independiente"] #str Si/No
    C = informacion["casado"] # str Si/No
    tipo = informacion["tipo_propiedad"] # str Urbano/Rural/Semiurbano
    edu = informacion["educacion"] # str Graduado/No Graduado
   
    # Si dependientes es 3+, se cambia a 3, de lo contrario sigue igual.
    if  informacion["dependientes"] == "3+":
        D = 3 #int
    else :
        D = informacion["dependientes"] #int
        
    # Evaluacion solicitudes de credito    
    if informacion["historia_credito"] == 1:
        if i_c > 0 and i_d/9 > c_p:
            aprobar = True
        else:
            if D > 2 and I == "Si":
                aprobar = i_c/12 > c_p
            else: 
                aprobar = c_p < 200
    else:
        if I == "Si":
            if C == "Si" and D > 1:
                aprobar = False
            else :
                if i_d/10 > c_p or i_c/10 > c_p:
                    aprobar = c_p < 180
                else :
                    aprobar = False
        else:
            if tipo == "Semiurbano" and D < 2:
                aprobar = False
            else :
                if edu == "Graduado" :
                    aprobar = i_d/11 > c_p and i_c/11 > c_p
                else :
                    aprobar = False    
                    
    # retornamos un nuevo diccionario con la decision 
    return dict(id_prestamo = informacion["id_prestamo"], aprobado = aprobar)


informacio = {"id_prestamo":"RETOS2_001",
            "casado":"Si",
            "dependientes": "3+" ,
            "educacion":"Graduado",
            "independiente": "No ",
            "ingreso_deudor": 1830,
            "ingreso_codeudor": 0,
            "cantidad_prestamo":100,
            "plazo_prestamo": 360,
            "historia_credito": 1,
            "tipo_propiedad":"Urbano"}

print (prestamo(informacio))






