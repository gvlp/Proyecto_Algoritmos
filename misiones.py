from leer_csv import cargar_datos_csv
from mision import Mision

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
            print('No hay misiones proximamente...')
        else :
            for i, mision in self.misiones :
                print(f'{i+1}. ')
                mision.imprimir_mision()
                print()
            opcion=input('Ingrese el número de la misión que desea modificar: ').strip()
            while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>len(self.misiones) :
                print('\nIngreso Inválido')
                opcion=input('Ingrese el número de la misión que desea modificar: ').strip()
            opcion=int(opcion)
            mision_seleccionada=self.misiones[opcion-1]
            opcion=input('''
¿Qué aspecto de la misón desea modificar?
1. Nombre de la misión
2. Planeta donde se llevará acabo la misión
3. Nave Espacial
4. Armas
5. Integrantes de la misión
>>> ''').strip
            while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>5 :
                print('\nIngreso Inválido')
                opcion=input('''
¿Qué aspecto de la misón desea modificar?
1. Nombre de la misión
2. Planeta donde se llevará acabo la misión
3. Nave Espacial
4. Armas
5. Integrantes de la misión
>>> ''').strip
            if opcion=='1' :
                mision_seleccionada.cambiar_nombre()

            elif opcion=='2' :
                mision_seleccionada.cambiar_planeta()

            elif opcion=='3' :
                mision_seleccionada.cambiar_nave()

            elif opcion=='4' :
                ingreso=input('''
Intercambiar arma (1)
Eliminar arma (2)
Agregar Arma (3)
>>> ''')
                while not ingreso.isnumeric() or int(ingreso)<1 or int(ingreso)>3 :
                    print('\nIngreso Inválido')
                    ingreso=input('''
Intercambiar arma (1)
Eliminar arma (2)
Agregar arma (3)
>>> ''')
                if ingreso=='1' :
                    mision_seleccionada.cambiar_arma()
                elif ingreso=='2' :
                    mision_seleccionada.eliminar_arma()
                elif ingreso=='3' :
                    mision_seleccionada.agregar_arma()

            elif opcion=='5' :
                ingreso=input('''
Intercambiar integrante (1)
Eliminar integrante (2)
Agregar integrante (3)
>>> ''')
                while not ingreso.isnumeric() or int(ingreso)<1 or int(ingreso)>3 :
                    print('\nIngreso Inválido')
                    ingreso=input('''
Intercambiar integrante (1)
Eliminar integrante (2)
Agregar integrante (3)
>>> ''')
                if ingreso=='1' :
                    mision_seleccionada.cambiar_integrante()
                elif ingreso=='2' :
                    mision_seleccionada.eliminar_integrante()
                elif ingreso=='3' :
                    mision_seleccionada.agregar_integrante()

            else: 
                print('Ingreso Inválido')


    def visualizar_misiones(self) :
        if self.misiones==[] :
            print('No hay misiones disponibles')
        else:
            for i, mision in self.misiones :
                print(f'{i+1}. ')
                mision.imprimir_mision()
                print()
            opcion=input('Ingrese el número de la misión que desea modificar: ').strip()
            while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>len(self.misiones) :
                print('\nIngreso Inválido')
                opcion=input('Ingrese el número de la misión que desea modificar: ').strip()
            opcion=int(opcion)
            mision_seleccionada=self.misiones[opcion-1]
            opcion=input('''
    ¿Qué aspecto de la misón desea profundizar?
    1. Datos de la nave espacial
    2. Datos de las armas
    3. Datos de los integrantes
    >>> ''').strip
            while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>3 :
                print('\nIngreso Inválido')
                opcion=input('''
    ¿Qué aspecto de la misón desea profundizar?
    1. Datos de la nave espacial
    2. Datos de las armas
    3. Datos de los integrantes
    >>> ''').strip
                if opcion=='1' :
                    nave_seleccionada=mision_seleccionada.selected_starship()
                    for nave in cargar_datos_csv()['starships'] :
                        if nave['name']==nave_seleccionada :
                            print(f'{nave}: {nave['model']}')
                            print(f'{nave}: {nave['manufacturer']}')
                            print(f'{nave}: {nave['max_atmosphering_speed']}')
                            print(f'{nave}: {nave['length']}')
                            print(f'{nave}: {nave['crew']}')
                            print(f'{nave}: {nave['passengers']}')
                            print(f'{nave}: {nave['cargo_capacity']}')
                            print(f'{nave}: {nave['consumables']}')
                            print(f'{nave}: {nave['hyperdrive_rating']}')
                            print(f'{nave}: {nave['MGLT']}')
                            print(f'{nave}: {nave['starship_class']}')

                elif opcion=='2' :
                    armas_seleccionadas=mision_seleccionada.selected_weapons()
                    for arma_selec in armas_seleccionadas :
                        for arma in cargar_datos_csv()['weapons'] :
                            if arma['name']==arma_selec:
                                print(f'{arma}: {arma['model']}')
                                print(f'{arma}: {arma['manufacturer']}')
                                print(f'{arma}: {arma['length']}')
                                print(f'{arma}: {arma['type']}')
                                print(f'{arma}: {arma['description']}')
                    
                elif opcion=='3' :
                    integrantes_seleccionados=mision_seleccionada.selected_chacarter()
                    for integrante_selec in integrantes_seleccionados :
                        for integrante in cargar_datos_csv()['characters'] :
                            if integrante['name']==integrante_selec:
                                print(f'{integrante}: {integrante['species']}')
                                print(f'{integrante}: {integrante['gender']}')
                                print(f'{integrante}: {integrante['height']}')
                                print(f'{integrante}: {integrante['weight']}')
                                print(f'{integrante}: {integrante['homeworld']}')
                                print(f'{integrante}: {integrante['description']}')

