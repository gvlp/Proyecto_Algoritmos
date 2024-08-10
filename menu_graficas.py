import matplotlib.pyplot as plt
import os
from Graficas.grafica_personajes import mostrar_grafica_persona_x_planeta
from Graficas.grafica_naves_longitud import mostrar_grafica_naves_long
from Graficas.grafica_naves_cap_carga import mostrar_grafica_naves_cap_carga
from Graficas.grafica_naves_hiperimpulsores import mostrar_grafica_naves_hiperpropulsores
from Graficas.grafica_naves_mglt import mostrar_grafica_naves_MGLT


def mostrar_menu_graficas():
    print("1. Ver gráfica de personas")
    print("2. Ver gráfica de naves")
    print("3. Regresar al menu principal")
    while True:

        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            mostrar_grafica_persona()

        elif opcion == '2':
            mostrar_menu_naves()
        elif opcion =='3':
            print('Regresando al menu principal...')
            break
            
        else:
            print("Opción inválida. Inténtalo de nuevo.")
            opcion = input("Selecciona una opción: ")


def mostrar_menu_naves():
    print("\nSelecciona una opción:")
    print("1. Longitud de la nave")
    print("2. Capacidad de carga")
    print("3. Clasificación de hiperimpulsor")
    print("4. MGLT (Modern Galactic Light Time)")
    print("5. Regresar al menu principal")

    while True:
        opcion_naves = input("\nSelecciona una opción: ")
        if opcion_naves =="1":
            mostrar_grafica_naves_longitud()
        elif opcion_naves =="2":
            mostrar_grafica_naves_capacidad_carga()
        elif opcion_naves =="3":
            mostrar_grafica_naves_hiperimpulsores_()
        elif opcion_naves =="4":
            mostrar_grafica_naves_MGLT_()
        elif opcion_naves =="5":
            print('Regresar')
            break
            
        else: 
            print("Opción inválida. Inténtalo de nuevo.")
            opcion_naves = input("Selecciona una opción: ")


#metodos para cada grafica
def mostrar_grafica_persona():    
    print("Mostrando gráfica de personas...")
    mostrar_grafica_persona_x_planeta()
    plt.show()

def mostrar_grafica_naves_longitud():    
    print("Mostrando gráfica de longitud de las naves...")
    mostrar_grafica_naves_long()
    plt.show()

def mostrar_grafica_naves_capacidad_carga():    
    print("Mostrando gráfica de capacidad de carga de cada nave...")
    mostrar_grafica_naves_cap_carga()
    plt.show()

def mostrar_grafica_naves_hiperimpulsores_():    
    print("Mostrando gráfica de hiperimpulsores de las naves...")
    mostrar_grafica_naves_hiperpropulsores()
    plt.show()

def mostrar_grafica_naves_MGLT_():    
    print("Mostrando gráfica de MGLT...")
    mostrar_grafica_naves_MGLT()
    plt.show()












