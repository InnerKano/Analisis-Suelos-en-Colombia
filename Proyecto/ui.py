from api import*

def Bienvenida():
    print("\nBienvenido Usuario\n")

def departamento():
    nombre_departamento=input("Inserte el departamento: ")
    return nombre_departamento

def municipio():
    nombre_municipio=input("Inserte el municipio: ")
    return nombre_municipio

def cultivo():
    nombre_cultivo=input("Inserte el cultivo: ")
    return nombre_cultivo

def limite():
    limit=int(input("Inserte el limite de regitros: "))
    print("\n")
    if (limit > 200):
        print("Error inserte un limite de menor tamaño")
        limite()
    return limit
