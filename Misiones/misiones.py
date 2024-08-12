from leer_csv import cargar_datos_csv
from Misiones.mision import Mision

class Misiones:

    def __init__(self, misiones=[]) :
        self.misiones=misiones

    def agregar_mision(self) :
        if len(self.misiones)<5 :
            self.misiones.append(Mision().crear_mision())
        else :
            print('Lo sentimos, ya no podemos agregar otra misón')

    def modoficar_mision(self) :
        if self.misiones==[] :
            print('\nNo hay misiones disnonibles')
        else :
            i=0
            for mision in self.misiones :
                i+=1
                print(f'{i}. ')
                mision.imprimir_mision()
                print()
            opcion=input('Ingrese el número de la misión que desea modificar: ').strip()
            while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>len(self.misiones) :
                print('\nIngreso Inválido')
                opcion=input('Ingrese el número de la misión que desea modificar: ').strip()
            opcion=int(opcion)
            mision_seleccionada=self.misiones[opcion-1]
            while True: 
                opcion=input('''
¿Qué aspecto de la misón desea modificar?
1. Nombre de la misión
2. Planeta donde se llevará acabo la misión
3. Nave Espacial
4. Armas
5. Integrantes de la misión
6. Regresar al menú de misiones
>>> ''').strip()
                if opcion=='1' :
                    mision_seleccionada.cambiar_nombre()

                elif opcion=='2' :
                    mision_seleccionada.cambiar_planeta()

                elif opcion=='3' :
                    mision_seleccionada.cambiar_nave()

                elif opcion=='4' :
                    while True :
                        ingreso=input('''
1. Intercambiar arma
2. Eliminar arma
3. Agregar arma 
4. Regresar
>>> ''').strip()
                        if ingreso == '1' :
                            mision_seleccionada.cambiar_arma()
                        elif ingreso == '2' :
                            mision_seleccionada.eliminar_arma()
                        elif ingreso == '3' :
                            mision_seleccionada.agregar_arma()
                        elif ingreso == '4' :
                            print('\nRegresando...')
                            break
                        else :
                            print()
                            print('Ingreso Inválido')

                elif opcion=='5' :
                    while True :
                        ingreso=input('''
1. Intercambiar integrante 
2. Eliminar integrante 
3. Agregar integrante 
4. Regresar
    >>> ''').strip()
                        if ingreso=='1' :
                            mision_seleccionada.cambiar_integrante()
                        elif ingreso=='2' :
                            mision_seleccionada.eliminar_integrante()
                        elif ingreso=='3' :
                            mision_seleccionada.agregar_integrante()
                        elif ingreso=='4' :
                            print('\nRegresando...')
                            break
                        else :
                            print()
                            print('Ingreso Inválido')

                elif opcion=='6' :
                    print('\nRegresando...')
                    break

                else: 
                    print()
                    print('Ingreso Inválido')



    def visualizar_misiones(self) :
        if self.misiones==[] :
            print('\nNo hay misiones disponibles')
        else:
            i=0
            for mision in self.misiones :
                i+=1
                print(f'{i}. ')
                mision.imprimir_mision()
                print()
            opcion=input('Ingrese el número de la misión que desea ver: ').strip()
            while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>len(self.misiones) :
                print('\nIngreso Inválido')
                opcion=input('Ingrese el número de la misión que desea ver: ').strip()
            opcion=int(opcion)
            mision_seleccionada=self.misiones[opcion-1]
            while True :
                seleccion=input('''
    ¿Qué aspecto de la misón desea profundizar?
    1. Datos de la nave espacial
    2. Datos de las armas
    3. Datos de los integrantes
    4. Regresar al menú de misones
    >>> ''').strip()
                if seleccion=='1' :
                    nave_seleccionada=mision_seleccionada.selected_starship
                    for nave in cargar_datos_csv()['starships'] :
                        if nave['name']==nave_seleccionada :
                            print(f'Nombre: {nave['name']} ')
                            print(f'Modelo: {nave['model']}')
                            print(f'Fabricante: {nave['manufacturer']}')
                            print(f'Velocidad máxima en atmósfera: {nave['max_atmosphering_speed']}')
                            print(f'Longuitud: {nave['length']}')
                            print(f'Tripulación: {nave['crew']}')
                            print(f'Pasajeros: {nave['passengers']}')
                            print(f'Capacidad de carga: {nave['cargo_capacity']}')
                            print(f'Consumibles: {nave['consumables']}')
                            print(f'Clasificación del hiperpropulsor: {nave['hyperdrive_rating']}')
                            print(f'MGLT: {nave['MGLT']}')
                            print(f'Clase de nave estelar: {nave['starship_class']}')
                            print()
                            print('-'*20)

                elif seleccion=='2' :
                    print()
                    print('-'*20)
                    armas_seleccionadas=mision_seleccionada.selected_weapons
                    for arma_selec in armas_seleccionadas :
                        for arma in cargar_datos_csv()['weapons'] :
                            if arma['name']==arma_selec:
                                print(f'Nombre: {nave['name']} ')
                                print(f'Modelo: {arma['model']}')
                                print(f'Fabricante: {arma['manufacturer']}')
                                print(f'Longuitud: {arma['length']}')
                                print(f'Tipo: {arma['type']}')
                                print(f'Descripción: {arma['description']}')
                                print()
                                print('-'*20)
                    
                elif seleccion=='3' :
                    print()
                    print('-'*20)
                    integrantes_seleccionados=mision_seleccionada.selected_chacarter
                    for integrante_selec in integrantes_seleccionados :
                        for integrante in cargar_datos_csv()['characters'] :
                            if integrante['name']==integrante_selec:
                                print(f'Nombre: {integrante['name']}')
                                print(f'Especie: {integrante['species']}')
                                print(f'Género: {integrante['gender']}')
                                print(f'Altura: {integrante['height']}')
                                print(f'Peso: {integrante['weight']}')
                                print(f'Planeta natal: {integrante['homeworld']}')
                                print(f'Descripción: {integrante['description']}')
                                print()
                                print('-'*20)

                elif seleccion=='4' :
                    print('\nRegresando...')
                    break
                
                else: 
                     print('\nIngreso Inválido')

    def guardar_mision(self) :
        if self.misiones==[]:
            print('\nNo hay misiones disponibles para guardar.')

        else: 
            with open('misiones_guardadas.txt', 'a') as archivo:
                for mision in self.misiones:
                    archivo.write(f'Mision:\n')
                    archivo.write(f'Nombre de la mision: {mision.name}\n')
                    archivo.write(f'Planeta: {mision.selected_planet}\n')
                    archivo.write(f'Nave Espacial: {mision.selected_starship}\n')
                    archivo.write('Armas:\n')
                    for arma in mision.selected_weapons:
                        archivo.write(f'- {arma}\n')
                    archivo.write('Integrantes:\n')
                    for integrante in mision.selected_chacarter:
                        archivo.write(f'- {integrante}\n')
                    archivo.write('-' * 40 + '\n')
        print('Las misiones han sido guardadas exitosamente en "misiones_guardadas.txt".')


    def cargar_misiones(self) :
        try:
            with open('misiones_guardadas.txt', 'r') as archivo:
                contenido=archivo.read()
                misiones=contenido.split('-' * 40 + '\n')
                
                for mision_str in misiones:
                    if mision_str.strip(): 
                        lineas=mision_str.strip().split('\n')
                        nombre=lineas[1].split(': ')[1]
                        planeta=lineas[2].split(': ')[1]
                        nave=lineas[3].split(': ')[1]
                        
                        armas=[]
                        indice_armas=lineas.index('Armas:') + 1
                        while not lineas[indice_armas].startswith('Integrantes:'):
                            armas.append(lineas[indice_armas].strip('- '))
                            indice_armas+=1
                        
                        integrantes=[]
                        indice_integrantes=lineas.index('Integrantes:') + 1
                        while indice_integrantes<len(lineas):
                            integrantes.append(lineas[indice_integrantes].strip('- '))
                            indice_integrantes+=1
                
                        mision=Mision(nombre, planeta, nave, armas, integrantes)
                        self.misiones.append(mision)

            print('Las misiones han sido cargadas exitosamente desde "misiones_guardadas.txt".')

        except FileNotFoundError:
            print('No se encontró el archivo "misiones_guardadas.txt". Asegúrate de que el archivo existe y tiene misiones guardadas.')
        except Exception as e:
            print(f'Ocurrió un error al cargar las misiones: {e}')
