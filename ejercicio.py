#un consultorio medico requiere llevar un registro de la asistencias de pacientes en la diferente especialidad 


odontologia = 0 
ginecologia = 0
consultorio_general = 0
maternidad = 0
infancia = 0



import os
os.system("cls")  

def fnt_limpiar_pantalla (cls):
    os.system("cls") 
def fnt_selection (op):
    global odontologia 
    global ginecologia 
    global consultorio_general 
    global maternidad 
    global infancia 
    if opcionesInt == 1:
        odontologia += 1
        print('elegiste odontologia')
    elif  opcionesInt == 2:
        ginecologia += 1
        print('elegiste ginecologia')
    elif opcionesInt == 3:
        consultorio_general += 1
        print('elegiste consultorio general')
    elif opcionesInt == 4:
        maternidad += 1
        print('elegiste maternidad')
    elif opcionesInt == 5:
        infancia += 1
        print('elegiste infancia')
    
        
def fnt_registro():
    
    print(f'la cantidad de pacientes en odontologia es : {odontologia}')
    print(f'la cantidad de pacientes en ginecologia es : {ginecologia}')
    print(f'la cantidad de pacientes en consultorio genrela es: {consultorio_general}')      
    print(f'la cantidad de pacientes en maternidad es : {maternidad}')
    print(f'la cantidad de pacientes en infancia es : {infancia} ')
while True:
    
    opcionesInt = int(input('especilidad a asistir ->  \n1. odontologia \n2. ginecologia \n3. consultorio general\n4. maternidad \n5. infancia \n6. reporte \n7. finalizar -> '))
    
    if opcionesInt < 1 and opcionesInt > 6:
        print('la informacion es invalida ')
    if opcionesInt == 6:
        fnt_registro ()
        
    fnt_selection (opcionesInt)
    fnt_limpiar_pantalla ('cls')
    fnt_limpiar_pantalla (opcionesInt)
    
    
    
    