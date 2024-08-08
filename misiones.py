from leer_csv import cargar_datos_csv

class Mision :
     
    planets=[]
    starships=[]
    weapons=[]
    members=[]

    def __init__(self, name, selected_planet, selected_starship, selected_weapons, selected_characters) -> None:
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

    def crear_mision(self) :

        #Nombre de la misión
        ingreso_nombre=input('Nombre de la mision')
        print('-'*20)

        #Elección del planeta
        print()
        print('Elige el planeta donde quieres que se desarrolle la misón: ')
        self.listar_planetas()
        for i in range(len(self.planets)) : 
            print(f'{i+1}. {self.planets[i]}')
        ingreso_planeta=input('>>> ').strip()
        while not ingreso_planeta.isnumeric() or int(ingreso_planeta)<1 or int(ingreso_planeta)>len(self.planets) :
            print('\nIngreso Inválido')
            print()
            print('Elige el planeta donde quieres que se desarrolle la misón: ')
            for i in range(len(self.planets)) : 
                print(f'{i+1}. {self.planets[i]}')
            ingreso_planeta=input('>>> ').strip()
        planeta_seleccionado=self.planets[ingreso_planeta-1]
        print('-'*20)

        #Elección de la nave
        print()
        print('Elige la nave que usarás en la misón: ')
        self.listar_naves()
        for i in range(len(self.starships)) : 
            print(f'{i+1}. {self.starships[i]}')
        ingreso_nave=input('>>> ').strip()
        while not ingreso_nave.isnumeric() or int(ingreso_nave)<1 or int(ingreso_nave)>len(self.starships) :
            print('\nIngreso Inválido')
            print()
            print('Elige la nave que usarás en la misón: ')
            for i in range(len(self.starships)) : 
                print(f'{i+1}. {self.starships[i]}')
            ingreso_nave=input('>>> ').strip()
        nave_seleccionada=self.starships[ingreso_nave-1]
        print('-'*20)

        #Eleccion de Armas: 
        print()
        self.listar_armas()
        print('Elige las armas que usarás en la misón ')
        print('En total, elegiras 7 armas ')
        for j in range(8) :
            armas_seleccionadas=[]
            print('Elige una: ')
            for i in range(len(self.weapons)) : 
                print(f'{i+1}. {self.weapons[i]}')
            ingreso_arma=input('>>> ').strip()
            while not ingreso_arma.isnumeric() or int(ingreso_arma)<1 or int(ingreso_arma)>len(self.weapons) :
                print('\nIngreso Inválido')
                print()
                print('Elige otra: ')
                for i in range(len(self.weapons)) : 
                    print(f'{i+1}. {self.weapons[i]}')
                ingreso_nave=input('>>> ').strip()
            arma_seleccionada=self.weapons[ingreso_arma-1]
            armas_seleccionadas.append(arma_seleccionada)
            self.weapons.pop(ingreso_arma-1)
        print('-'*20)

        #Eleccion de Integrantes: 
        print()
        self.listar_integrantes()
        print('Elige los integrantes que te acompañaran en la misón')
        print('En total, elegiras a 7')
        for j in range(8) :
            integrantes_seleccionados=[]
            print('Elige a uno: ')
            for i in range(len(self.members)) : 
                print(f'{i+1}. {self.members[i]}')
            ingreso_integrante=input('>>> ').strip()
            while not ingreso_integrante.isnumeric() or int(ingreso_integrante)<1 or int(ingreso_integrante)>len(self.members) :
                print('\nIngreso Inválido')
                print()
                print('Elige a otro: ')
                for i in range(len(self.members)) : 
                    print(f'{i+1}. {self.members[i]}')
                ingreso_integrante=input('>>> ').strip()
            integrante_seleccionado=self.members[ingreso_integrante-1]
            integrantes_seleccionados.append(integrante_seleccionado)
            self.members.pop(integrante_seleccionado-1)
        print('-'*20)

        return Mision(ingreso_nombre, planeta_seleccionado, nave_seleccionada, armas_seleccionadas, integrantes_seleccionados)

    print('Su misión ha sido creada exitosamente')

    def agregar_mision(self) :
        lista_misiones=[] 
        if len(lista_misiones)<5 :
            self.crear_mision()





        








    





