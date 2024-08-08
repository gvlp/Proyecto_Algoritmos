# MAIN

from Clases.swapi_api import Swapi
import time
from Menus.menu_swapi import menu

def main():
    swapi_api = Swapi()
    print()
    print("¡BIENVENIDO AL MUNDO DE STAR WARS!")
    print()
    print("En breve podrás acceder a la base de datos más completa de la galaxia")
    print()

    movies = None
    people = None
    planets = None
    species = None

    startTime=time.time()
    print("El programa se encuentra buscando los datos de las películas")
    movies = swapi_api.get_data("films")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")

    startTime=time.time()
    print("El programa se encuentra buscando los datos de los personajes")
    people = swapi_api.get_data("people")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")

    startTime=time.time()
    print("El programa se encuentra buscando los datos de los planetas")
    planets = swapi_api.get_data("planets")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos")

    startTime=time.time() 
    print("El programa se encuentra buscando los datos de los seres vivos")
    species = swapi_api.get_data("species")
    end_time = time.time()
    duracion=end_time-startTime
    print(f"Duración: {duracion:.2f} segundos") 

    menu(movies, people, planets, species)

if __name__ == "__main__":
    main()