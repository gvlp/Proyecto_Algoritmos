from leer_csv import cargar_datos_csv

class Mision :
     
    planets=[]
    starships=[]
    weapons=[]
    members=[]

    def __init__(self, name=None, selected_planet=None, selected_starship=None, selected_weapons=[], selected_characters=[]) -> None:
        self.name=name
        self.selected_planet=selected_planet
        self.selected_starship=selected_starship
        self.selected_weapons=selected_weapons
        self.selected_chacarter=selected_characters

    def listar_planetas(self) :
        for planeta in cargar_datos_csv()['planets'] :
            self.planets.append(planeta['name'])

    def listar_naves(self) :
        for starship in cargar_datos_csv()['starships'] :
            self.starships.append(starship['name'])

    def listar_armas(self) :
        for arma in cargar_datos_csv()['weapons'] :
            self.weapons.append(arma['name'])

    def listar_integrantes(self) :
        for integrante in cargar_datos_csv()['characters'] :
            self.members.append(integrante['name'])

    def retornar_listas(self) :
        self.weapons.clear()
        self.listar_armas()
        self.members.clear()
        self.listar_integrantes()

    def crear_mision(self) :

        if self.planets==[] :
            self.listar_planetas()
        if self.starships==[] :
            self.listar_naves()
        if self.weapons==[] :
            self.listar_armas()
        if self.members==[] :
            self.listar_integrantes()

        # Nombre de la misión
        print()
        print('-'*20)
        ingreso_nombre=input('Nombre de la mision: ')
        print('-'*20)

        # Elección del planeta
        print()
        print('Elige el planeta donde quieres que se desarrolle la misón: ')
        for i in range(len(self.planets)) : 
            print(f'{i+1}. {self.planets[i]}')
        ingreso_planeta=input('Opción: ').strip()
        while not ingreso_planeta.isnumeric() or int(ingreso_planeta)<1 or int(ingreso_planeta)>len(self.planets) :
            print('\nIngreso Inválido')
            print()
            print('Elige el planeta donde quieres que se desarrolle la misón: ')
            for i in range(len(self.planets)) : 
                print(f'{i+1}. {self.planets[i]}')
            ingreso_planeta=input('Opción: ').strip()
        ingreso_planeta=int(ingreso_planeta)
        planeta_seleccionado=self.planets[ingreso_planeta-1]
        print('-'*20)

        # Elección de la nave
        print()
        print('Elige la nave que usarás en la misón: ')
        for i in range(len(self.starships)) : 
            print(f'{i+1}. {self.starships[i]}')
        ingreso_nave=input('Opción: ').strip()
        while not ingreso_nave.isnumeric() or int(ingreso_nave)<1 or int(ingreso_nave)>len(self.starships) :
            print('\nIngreso Inválido')
            print()
            print('Elige la nave que usarás en la misón: ')
            for i in range(len(self.starships)) : 
                print(f'{i+1}. {self.starships[i]}')
            ingreso_nave=input('Opción: ').strip()
        ingreso_nave=int(ingreso_nave)
        nave_seleccionada=self.starships[ingreso_nave-1]
        print('-'*20)

        # Eleccion de Armas: 
        print()
        print('Elige las armas que usarás en la misón ')
        print('Puedes elegir hasta 7 armas ')
        j=0
        armas_seleccionadas=[]
        while j<7 :
            print('Elige una: ')
            for i in range(len(self.weapons)) : 
                print(f'{i+1}. {self.weapons[i]}')
            ingreso_arma=input('Opción: ').strip()
            while not ingreso_arma.isnumeric() or int(ingreso_arma)<1 or int(ingreso_arma)>len(self.weapons) :
                print('\nIngreso Inválido')
                print()
                print('Elige otra: ')
                for i in range(len(self.weapons)) : 
                    print(f'{i+1}. {self.weapons[i]}')
                ingreso_arma=input('Opción: ').strip()
            ingreso_arma=int(ingreso_arma)
            arma_seleccionada=self.weapons[ingreso_arma-1]
            armas_seleccionadas.append(arma_seleccionada)
            self.weapons.pop(ingreso_arma-1)
            j+=1
            if j==7:
                break
            else :
                seleccion=input('''
¿Deseas agregar otra armas?
Si (1)
No (2)
Opción:  ''').strip()
                while not seleccion.isnumeric() or int(seleccion)<1 or int(seleccion)>2 :
                    print('\nIngreso Inválido')
                    seleccion=input('''
¿Deseas agregar otra armas?
Si (1)
No (2)
Opción: ''').strip()
                if seleccion=='2' :
                    print('-'*20)
                    break
        

        # Eleccion de Integrantes: 
        print()
        print('Elige los integrantes que te acompañaran en la misón')
        print('En total, elegiras a 7')
        j=0
        integrantes_seleccionados=[]
        while j<7 :
            print('Elige a uno: ')
            for i in range(len(self.members)) : 
                print(f'{i+1}. {self.members[i]}')
            ingreso_integrante=input('Opción: ').strip()
            while not ingreso_integrante.isnumeric() or int(ingreso_integrante)<1 or int(ingreso_integrante)>len(self.members) :
                print('\nIngreso Inválido')
                print()
                print('Elige a otro: ')
                for i in range(len(self.members)) : 
                    print(f'{i+1}. {self.members[i]}')
                ingreso_integrante=input('Opción: ').strip()
            ingreso_integrante=int(ingreso_integrante)
            integrante_seleccionado=self.members[ingreso_integrante-1]
            integrantes_seleccionados.append(integrante_seleccionado)
            self.members.pop(ingreso_integrante-1)
            j+=1
            if j==7 :
                break
            else :
                seleccion=input('''
¿Deseas agregar a otro integrante?
Si (1)
No (2)
Opción: ''').strip()
                while not seleccion.isnumeric() or int(seleccion)<1 or int(seleccion)>2 :
                    print('\nIngreso Inválido')
                    seleccion=input('''
¿Deseas agregar a otro integrante?
Si (1)
No (2)
Opción: ''').strip()
                if seleccion=='2' :
                    print('-'*20)
                    break
        print()
        print('Su misión ha sido creada exitosamente')
        self.retornar_listas()

        return Mision(ingreso_nombre,planeta_seleccionado,nave_seleccionada,armas_seleccionadas,integrantes_seleccionados)

    def imprimir_mision(self) :
        print(f'Nombre de la misión: {self.name}')
        print(f'Planeta donde será la misión: {self.selected_planet}')
        print(f'Nave: {self.selected_starship}')
        print(f'Armas: ')
        for arma in self.selected_weapons :
            print(f'    {arma}')
        print(f'Integrantes de la misón: ')
        for integrante in self.selected_chacarter :
            print(f'    {integrante}')

    def cambiar_nombre(self) :
        self.name=input('Ingrese el nuevo nombre de la misión: ')
        print('-'*20)
        print()
        print('El nombre ha sido cambiada exitosamente. ')


    def cambiar_planeta(self) :
        print()
        print('Elige el planeta donde quieres que se desarrolle la misón: ')
        for i in range(len(self.planets)) : 
            print(f'{i+1}. {self.planets[i]}')
        ingreso_planeta=input('Opción: ').strip()
        while not ingreso_planeta.isnumeric() or int(ingreso_planeta)<1 or int(ingreso_planeta)>len(self.planets) :
            print('\nIngreso Inválido')
            print()
            print('Elige el planeta donde quieres que se desarrolle la misón: ')
            for i in range(len(self.planets)) : 
                print(f'{i+1}. {self.planets[i]}')
            ingreso_planeta=input('Opción: ').strip()
        ingreso_planeta=int(ingreso_planeta)
        planeta_seleccionado=self.planets[ingreso_planeta-1]
        self.selected_planet=planeta_seleccionado
        print('-'*20)
        print()
        print('El planeta ha sido cambiado exitosamente. ')


    def cambiar_nave(self) :
        print()
        print('Elige la nueva nave que usarás en la misón: ')
        for i in range(len(self.starships)) : 
            print(f'{i+1}. {self.starships[i]}')
        ingreso_nave=input('Opción: ').strip()
        while not ingreso_nave.isnumeric() or int(ingreso_nave)<1 or int(ingreso_nave)>len(self.starships) :
            print('\nIngreso Inválido')
            print()
            print('Elige la nueva nave que usarás en la misón: ')
            for i in range(len(self.starships)) : 
                print(f'{i+1}. {self.starships[i]}')
            ingreso_nave=input('Opción: ').strip()
        ingreso_nave=int(ingreso_nave)
        nave_seleccionada=self.starships[ingreso_nave-1]
        self.selected_starship=nave_seleccionada
        print('-'*20)
        print()
        print('La nave ha sido cambiada exitosamente. ')

    def cambiar_arma(self) :
        print()
        print('¿Cuál arma desea intercambiar?')
        for i in range(len(self.selected_weapons)):
            print(f'{i+1}. {self.selected_weapons[i]}')
        opcion = input('Opción: ').strip()
        while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > len(self.selected_weapons):
            print('Ingreso Inválido')
            print()
            print('¿Cuál arma desea intercambiar?')
            for i in range(len(self.selected_weapons)):
                print(f'{i+1}. {self.selected_weapons[i]}')
            opcion = input('Opción: ').strip()
        opcion = int(opcion)
        self.selected_weapons.pop(opcion - 1)
        
        print()
        print('Elige otra arma para la misión')
        lista_armas_no_usadas = [arma for arma in self.weapons if arma not in self.selected_weapons]
        
        for i, arma in enumerate(lista_armas_no_usadas):
            print(f'{i+1}. {arma}')
        
        ingreso_arma = input('Opción: ').strip()
        while not ingreso_arma.isnumeric() or int(ingreso_arma) < 1 or int(ingreso_arma) > len(lista_armas_no_usadas):
            print('\nIngreso Inválido')
            print()
            print('Elige otra: ')
            for i, arma in enumerate(lista_armas_no_usadas):
                print(f'{i+1}. {arma}')
            ingreso_arma = input('Opción: ').strip()
        
        ingreso_arma = int(ingreso_arma)
        arma_seleccionada = lista_armas_no_usadas[ingreso_arma - 1]
        self.selected_weapons.append(arma_seleccionada)
        print('-'*20)
        print()
        print('El arma fue exitosamente intercambiada')
       
    def eliminar_arma(self) :
        print()
        print('¿Cuál arma desea eliminar?')
        for i in range(len(self.selected_weapons)) :
            print(f'{i+1}. {self.selected_weapons[i]}')
        opcion=input('Opción: ').strip()
        while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>len(self.selected_weapons) :
            print('Ingreso Inválido')
            print()
            print('¿Cuál arma desea eliminar?')
            for i in range(len(self.selected_weapons)) :
                print(f'{i+1}. {self.selected_weapons[i]}')
            opcion=input('Opción: ').strip()
        opcion=int(opcion)
        self.selected_weapons.pop(opcion-1)
        print('-'*20)
        print()
        print('El arma fue exitosamente eliminada')

    def agregar_arma(self) :
        if len(self.selected_weapons) < 7:
            print('Elige un arma nueva para la misión')
            lista_armas_no_usadas = [arma for arma in self.weapons if arma not in self.selected_weapons]

            for i, arma in enumerate(lista_armas_no_usadas, 1):
                print(f'{i}. {arma}')

            ingreso_arma = input('Opción: ').strip()
            while not ingreso_arma.isnumeric() or int(ingreso_arma) < 1 or int(ingreso_arma) > len(lista_armas_no_usadas):
                print('\nIngreso Inválido')
                for i, arma in enumerate(lista_armas_no_usadas, 1):
                    print(f'{i}. {arma}')
                ingreso_arma = input('Opción: ').strip()

            ingreso_arma = int(ingreso_arma)
            arma_seleccionada = lista_armas_no_usadas[ingreso_arma - 1]
            self.selected_weapons.append(arma_seleccionada)
            print('-' * 20)
            print()
            print('El arma fue exitosamente agregada')
        else:
            print()
            print('Ya tienes el máximo de armas para tu misión, no puedes agregar más.')


    def cambiar_integrante(self) :
        print()
        print('¿A cuál integrante desea intercambiar?')
        for i in range(len(self.selected_chacarter)):
            print(f'{i+1}. {self.selected_chacarter[i]}')
        opcion = input('Opción: ').strip()
        while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > len(self.selected_chacarter):
            print('Ingreso Inválido')
            print()
            print('¿A cuál integrante desea intercambiar?')
            for i in range(len(self.selected_chacarter)):
                print(f'{i+1}. {self.selected_chacarter[i]}')
            opcion = input('Opción: ').strip()
        opcion = int(opcion)
        self.selected_chacarter.pop(opcion - 1)

        print()
        print('Elige a otro integrante para la misión')
        lista_integrantes_no_usados = [integrante for integrante in self.members if integrante not in self.selected_chacarter]
        
        for i, integrante in enumerate(lista_integrantes_no_usados):
            print(f'{i+1}. {integrante}')
        
        ingreso_integrante = input('Opción: ').strip()
        while not ingreso_integrante.isnumeric() or int(ingreso_integrante) < 1 or int(ingreso_integrante) > len(lista_integrantes_no_usados):
            print('\nIngreso Inválido')
            print()
            print('Elige a otro: ')
            for i, integrante in enumerate(lista_integrantes_no_usados):
                print(f'{i+1}. {integrante}')
            ingreso_integrante = input('Opción: ').strip()
        
        ingreso_integrante = int(ingreso_integrante)
        integrante_seleccionado = lista_integrantes_no_usados[ingreso_integrante - 1]
        self.selected_chacarter.append(integrante_seleccionado)
        print('-'*20)
        print()
        print('El integrante fue exitosamente intercambiado')
        
    def eliminar_integrante(self) :
        print()
        print('¿A cuál integrante desea intercambiar?')
        for i in range(len(self.selected_chacarter)) :
            print(f'{i+1}. {self.selected_chacarter[i]}')
        opcion=input('Opción: ').strip()
        while not opcion.isnumeric() or int(opcion)<1 or int(opcion)>len(self.selected_chacarter) :
            print('Ingreso Inválido')
            print()
            print('¿A cuál integrante desea intercambiar?')
            for i in range(len(self.selected_chacarter)) :
                print(f'{i+1}. {self.selected_chacarter[i]}')
            opcion=input('Opción: ').strip()
        opcion=int(opcion)
        self.selected_chacarter.pop(opcion-1)
        print('-'*20)
        print()
        print('El integrante fue exitosamente eliminado')

    def agregar_integrante(self) :
        if len(self.selected_chacarter) < 7:
            print('Elige un nuevo integrante para la misión')
            lista_integrantes_no_usados = [integrante for integrante in self.members if integrante not in self.selected_chacarter]

            for i, integrante in enumerate(lista_integrantes_no_usados, 1):
                print(f'{i}. {integrante}')

            ingreso_integrante = input('Opción: ').strip()
            while not ingreso_integrante.isnumeric() or int(ingreso_integrante) < 1 or int(ingreso_integrante) > len(lista_integrantes_no_usados):
                print('\nIngreso Inválido')
                for i, integrante in enumerate(lista_integrantes_no_usados, 1):
                    print(f'{i}. {integrante}')
                ingreso_integrante = input('Opción: ').strip()

            ingreso_integrante = int(ingreso_integrante)
            integrante_seleccionado = lista_integrantes_no_usados[ingreso_integrante - 1]
            self.selected_chacarter.append(integrante_seleccionado)
            print('-'*20)
            print()
            print('El integrante fue exitosamente agregado')

        else:
            print('Ya tienes el máximo de integrantes en tu misión, no puedes agregar más.') 
            