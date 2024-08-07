# MAIN

from Clases.swapi_api import Swapi 
import time

def main():

    swapi_api = Swapi()

    print()
    print("¡BIENVENIDO AL MUNDO DE STAR WARS!")
    print()
    print("En breve podrás acceder a la base de datos más completa de la galaxia")
    print()

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
        print()
        print("A continuación se presenta el menú, por favor seleccione una opción:")
        print("1. Información de películas")
        print("2. Información de personajes")
        print("3. Información de planetas")
        print("4. Información de seres vivos")
        print("5. Personas por planeta")
        print("6. Información de naves")
        print("7. Estadistica sobre las naves")
        print("8. Misiones")
        print("9. Salir del programa")
        print()

        option = input("Opción: ")
        print()

        if option == "1":
            print("Lista de películas:")

            for i, movie in enumerate(movies, 1):
                print(f"{i}. {movie.title}")
            while True:
                try:
                    movie_option = int(input("Seleccione una película (ingrese el número) para ver información sobre ella: "))
                    if movie_option > 0 and movie_option <= len(movies):
                        elected_movie = movies[movie_option - 1]
                        print(elected_movie)
                        break
                    else:
                        print("Número inválido. Por favor, ingrese un número válido.")
                except ValueError:
                    print("Ingrese un número, por favor.")

        elif option == "2":
            print("Opciones para buscar personajes:")
            print("1. Buscar personajes manualmente")
            print("2. Ver lista de personajes")

            person_option = input("Por favor ingrese una opción: ")

            if person_option == "1":
                print("Búsqueda de personajes:")
                search_string = input("Ingrese una cadena de caracteres para buscar a los personajes que la contengan: ")
                search_string = search_string.lower()

                matching_characters = [person for person in people if search_string in person.name.lower()]

                if matching_characters:
                    print("Personajes encontrados:")
                    for i, person in enumerate(matching_characters, 1):
                        print(f"{i}. {person.name}")

                    while True:
                        seleccion = input("Seleccione un personaje (ingrese el número) para ver información sobre él: ")
                        try:
                            seleccion = int(seleccion)
                            if seleccion > 0 and seleccion <= len(matching_characters):
                                selected_person = matching_characters[seleccion - 1]
                                print(selected_person)
                                break
                            else:
                                print("Número inválido. Por favor, ingrese un número válido.")
                        except ValueError:
                            print("Ingrese un número, por favor.")

                else:
                    print("No se encontraron personajes que coincidan con la búsqueda.")

            elif person_option == "2":
                print("Lista de personajes:")
                for i, person in enumerate(people, 1):
                    print(f"{i}. {person.name}")

                while True:
                    seleccion = input("Seleccione un personaje (ingrese el número) para ver información sobre él: ")
                    try:
                        seleccion = int(seleccion)
                        if seleccion > 0 and seleccion <= len(people):
                            selected_person = people[seleccion - 1]
                            print(selected_person)
                            break
                        else:
                            print("Número inválido. Por favor, ingrese un número válido.")
                    except ValueError:
                        print("Ingrese un número, por favor.")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

        elif option == "3":

            print("Lista de planetas:")
            for i, planet in enumerate(planets, 1):
                print(f"{i}. {planet.name}")
            while True:
                try:
                    planet_option = int(input("Seleccione un planeta (ingrese el número) para ver más información sobre él: "))
                    if planet_option > 0 and planet_option <= len(planets):
                        selected_planet = planets[planet_option - 1]
                        print(selected_planet)
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
                    specie_index = int(input("Seleccione una especie (ingrese el número) para ver información sobre ella: "))
                    if specie_index < 1 or specie_index > len(species):
                        print("Número inválido. Por favor, ingrese un número válido.")
                    else:
                        selected_specie = species[specie_index - 1]
                        print("\nInformación de la especie:")
                        print(selected_specie)  
                        break
                except ValueError:
                    print("Ingrese un número, por favor.")

        elif option == "9":
            print("El programa ha cerrado")
            print()
            print("¡QUE LA FUERZA TE ACOMPAÑE!")
            print()
            break

        else:
            print("Esta opción no es válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()