from Misiones.misiones import Misiones

def menu_misiones() :
    while True: 
        viaje_galaxia=Misiones()
        opcion=input('''
A continuación se presentan las posibles opciónes para que comiences tu misón:
1. Crear una nueva misión
2. Modificar una misón existente
3. Visualizar las misiones
4. Guardar misiones
5. Cargar misiones
6. Regresar al menú principal
                     
Opción: ''').strip()
        if opcion=='1' :
           viaje_galaxia.agregar_mision()
        elif opcion=='2' :
            viaje_galaxia.modoficar_mision()
        elif opcion=='3' :
            viaje_galaxia.visualizar_misiones()
        elif opcion=='4' :
            viaje_galaxia.guardar_mision()
        elif opcion=='5' :
            viaje_galaxia.cargar_misiones()
        elif opcion=='6' :
            print('Regresando al menú principal...')
            break
        else :
            print('\nIngreso inválido')
