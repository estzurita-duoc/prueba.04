peliculas=[]

def validar_nombre(nombre):
    return nombre.strip()!=""

def validar_duracion(duracion):
    try:
        valor_duracion=int(duracion)
        return valor_duracion > 0
    except:
        return False

def validar_calificacion(calificacion):
    try:
        valor_calificacion=float(calificacion)
        return 0.0 <=valor_calificacion<=10.0
    except:
        return False
    
def mostrar_menu():
    print("\n======MENÚ======")
    print("1. Agregar película")
    print("2. Buscar película")
    print("3. Eliminar  película")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar pelicula")
    print("6. salir")


def leer_opcion():
    while True:
        try:
            opcion=int(input("ingrese una opcion del 1 al 6: "))
            if 1<=opcion<=6:
                return opcion
            else:
                print("ERROR: Debe ingresar una opcion entre 1 y 6.")
        except:
            print("ERROR: ingrese un numero valido.")

def agregar_pelicula(lista):
    while True:
        nombre = input("ingrese nombre de la pelicula: ")
        if validar_nombre(nombre):
            break
        else:
            print("ERROR: el nombre no puede estar vacio ni contener solo espacios.") 
    while True:
        duracion=int(input("ingrese la duracion de la pelicula: "))
        if validar_duracion(duracion):
            break
        else:
            print("la duracion debe ser un numero entero mayor a 0")
    while True:
        calificacion=float(input("ingrese la calificacion de la pelicula: "))
        if validar_calificacion(calificacion):
            break
        else:
            print("la calificacion debe ser un numero decimal entre 0.0 y 10.0")
    
    
    pelicula= {"nombre": nombre.strip(),
               "duracion": int(duracion),
               "calificacion": float(calificacion),
               "disponible":False
               }
    lista.append(pelicula)
    print("\nPelicula registrada exitosamnete")


def buscar_pelicula(lista, nombre_buscar):
    for pelicula in range(len(lista)):
        if lista[pelicula]["nombre"]== nombre_buscar:
            return pelicula
    return -1

def actualizar_disponiblidad(lista):
    for pelicula in lista:
        if pelicula["calificacion"]>=7.0:
            pelicula["disponible"]= True
        else:
            pelicula["disponible"]= False
def mostrar_pelicula(lista):
    actualizar_disponiblidad(lista)
    if len(lista)==0:
        print("No existen peliculas registradas")
        return
    
    print("\n===LISTA DE PELICULAS===")
    print(f"Nombre:{peliculas['nombre']}")
    print(f"Duracion:{peliculas['duracion']}")
    print(f"Calificacion:{peliculas['calificacion']}")

    if peliculas["disponible"]:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: NO RECOMENDADA")
    
while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion== 1:
        agregar_pelicula(peliculas)
    elif opcion== 2:
        nombre_buscar=input("ingrese el nombre de la pelicula que quiere buscar: ")
        posicion = buscar_pelicula(peliculas,nombre_buscar)

        if posicion!=-1:
            print("estudiante encontrado")
            print(f"Posicion en la lista: {posicion}")
            print(f"nombre : {peliculas[posicion]['nombre']}")
            print(f"duracion : {peliculas[posicion]['duracion']}")
            print(f"calificacion : {peliculas[posicion]['calificacion']}")

            if peliculas[posicion]['disponible']:
                print("estado actual: DISPONIBLE")
            else:
                print("estado actual: NO RECOMENDADO")
        else:
            print(f"la pelicula'{nombre_buscar}' no se encuentra registrada")
    elif opcion== 3:
        nombre_eliminar=input("ingrese nombre de pelicula a eliminar: ")
        posicion= buscar_pelicula(peliculas, nombre_eliminar)
        if posicion !=-1:
            peliculas.pop(posicion)
            print("pelicula eliminada")
        else:
            print(f"la pelicula '{nombre_eliminar}' no se encuentra registrada")
    elif opcion==4:
        actualizar_disponiblidad(peliculas)
        print("disponibilidad actualizada")
    elif opcion ==5:
        mostrar_pelicula(peliculas)
    elif opcion== 6:
        print("\n gracias por usar el sistema. vuelva pronto")
            