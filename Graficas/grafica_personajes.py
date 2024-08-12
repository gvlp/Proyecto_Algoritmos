import pandas as pd
from matplotlib import pyplot as plt
import csv
import random

def mostrar_grafica_persona_x_planeta():
    
    homeworld_counter= {}

    with open('starwars/csv/characters.csv','r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            homeworld = row['homeworld']
            if homeworld in homeworld_counter:
                homeworld_counter[homeworld]+=1

            else:
                homeworld_counter[homeworld]=1


    homeworld_label = list(homeworld_counter.keys())
    homeworld_values = list(homeworld_counter.values())

    labels_num = len(homeworld_label)
    #Para definir los colores de cada barra
    def gen_random_colors():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02X}{g:02X}{b:02X}"
    elements_number = len(homeworld_values)
    colors = [gen_random_colors() for _ in range(elements_number)]
    plt.bar(homeworld_label,homeworld_values,color=colors)
    plt.xlabel('Planetas')
    plt.ylabel('Némero de personajes')
    plt.title('Número de personajes nacidos en cada planeta')
    plt.xticks(rotation=90)
    plt.xlim(-0.5, len(homeworld_label)-0.5)
    plt.tick_params(axis='x',which='major',labelsize=7)

    