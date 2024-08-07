# MAIN

from swapi_api import Swapi 
import time

def main():

    swapi_api = Swapi()

    print("Cargando data de Star Wars")
    
    startTime=time.time()
    print("El programa se encuentra buscando los datos de las películas")
    movies = swapi_api.get_data("films")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")

    print("El programa se encuentra buscando los datos de los personajes")
    startTime=time.time()
    people = swapi_api.get_data("people")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")

    print("El programa se encuentra buscando los datos de los planetas")
    startTime=time.time()
    planets = swapi_api.get_data("planets")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")

    print("El programa se encuentra buscando los datos de los seres vivos")
    startTime=time.time() 
    species = swapi_api.get_data("species")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")
   
    while True:
        print("Bienvenido al mundo de Star Wars, por favor seleccione una opción:")
        print("1. Información de películas")
        print("2. Información de personajes")
        print("3. Información de planetas")
        print("4. Información de seres vivos")
        print("5. Personas por planeta")
        print("6. Información de naves")
        print("7. Estadistica sobre las naves")
        print("8. Misiones")
        print("9. Salir del programa")

        option = input("Opción: ")

        if option == "1":
            print("Lista de películas:")

            for i, movie in enumerate(movies, 1):
                print(f"{i}. {movie.title}")
            while True:
                try:
                    movie_option = int(input("Seleccione una película (ingrese el número) para ver más información sobre ella: "))
                    if movie_option > 0 and movie_option <= len(movies):
                        elected_movie = movies[movie_option - 1]
                        print(elected_movie)
                        print("---")
                        break
                    else:
                        print("Número inválido. Por favor, ingrese un número válido.")
                except ValueError:
                    print("Ingrese un número, por favor.")

        elif option == "2":
            print("Lista de personajes:")
            
            for i, person in enumerate(people, 1):
                print(f"{i}. {person.name}")

            while True:
                seleccion = int(input("Ingrese el número del personaje que desea ver: "))
                try:
                    seleccion = int(seleccion)
                    if seleccion > 0 and seleccion <= len(people):
                        print(people[seleccion - 1])
                        break
                    else:
                        print("Número inválido. Por favor, ingrese un número válido.")
                except ValueError:
                    print("Ingrese un número, por favor.")

        elif option == "3":
        #    planets = swapi_api.get_data("planets")
            print("Lista de planetas:")
            for i, planet in enumerate(planets, 1):
                print(f"{i}. {planet.name}")
            while True:
                try:
                    planet_option = int(input("Seleccione un planeta (ingrese el número) para ver más información sobre él: "))
                    if planet_option > 0 and planet_option <= len(planets):
                        selected_planet = planets[planet_option - 1]
                        print(selected_planet)
                        print("---")
                        break
                    else:
                        print("Número inválido. Por favor, ingrese un número válido.")
                except ValueError:
                    print("Ingrese un número, por favor.")

        elif option == "4":
            print("Lista de especies:")
            for i, specie in enumerate(species):
                print(f"{i+1}. {specie.name}")  

            while True:
                try:
                    specie_index = int(input("Ingrese el número de la especie que desea ver: "))
                    if specie_index < 1 or specie_index > len(species):
                        print("Número inválido. Por favor, ingrese un número entre 1 y", len(species))
                    else:
                        selected_specie = species[specie_index - 1]
                        print("\nInformación de la especie:")
                        print(selected_specie)  
                        break
                except ValueError:
                    print("Ingrese un número válido.")

        elif option == "9":
            print("Ha salido del programa")
            break

        else:
            print("Esta opción no es válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()