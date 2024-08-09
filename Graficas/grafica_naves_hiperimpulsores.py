import pandas as pd
from matplotlib import pyplot as plt
import csv
import random

def mostrar_grafica_naves_hiperpropulsores():
    data = pd.read_csv('starwars/csv/starships.csv')

    starships = data['name']
    lenghs = data['hyperdrive_rating']
    labels_num = len(starships)
    def gen_random_colors():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02X}{g:02X}{b:02X}"
    elements_number = len(starships)
    colors = [gen_random_colors() for _ in range(elements_number)]
    plt.bar(starships,lenghs,color=colors)
    plt.xlabel('Naves')
    plt.ylabel('Capacidad de carga')
    plt.title('Comparacion de capacidad de carga de naves')
    plt.xticks(rotation=90)
    plt.tick_params(axis='x',which='major',labelsize=7)
