import datetime

# Variables globales
asientos = [["O" for _ in range(10)] for _ in range(10)]
precios = {
    "Platinum": 120000,
    "Gold": 80000,
    "Silver": 50000
}
asistentes = []

# Función para validar la opción del menú
def validar_opcion(opciones):
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion in opciones:
            return opcion
        print("Opción inválida. Intente nuevamente.")

# Función para comprar entradas
def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    while cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Intente nuevamente.")
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))

    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()

    for _ in range(cantidad):
        fila = int(input("Seleccione la fila del asiento disponible: ")) - 1
        while fila < 0 or fila >= 10:
            print("Fila inválida. Intente nuevamente.")
            fila = int(input("Seleccione la fila del asiento disponible: ")) - 1

        columna = int(input("Seleccione la columna del asiento disponible: ")) - 1
        while columna < 0 or columna >= 10:
            print("Columna inválida. Intente nuevamente.")
            columna = int(input("Seleccione la columna del asiento disponible: ")) - 1

        if asientos[fila][columna] == "X":
            print("Ubicación no disponible. Intente nuevamente.")
            continue

        run = input("Ingrese el RUN del asistente (sin guiones ni dígito verificador): ")
        while not run.isdigit():
            print("RUN inválido. Intente nuevamente.")
            run = input("Ingrese el RUN del asistente (sin guiones ni dígito verificador): ")

        asientos[fila][columna] = "X"

        asistente = {
            "asiento": (fila, columna),
            "run": run
        }
        asistentes.append(asistente)

    print("Operación realizada correctamente.")

# Función para mostrar ubicaciones disponibles
def mostrar_ubicaciones_disponibles():
    print("Estado actual de la venta de entradas:")
    print("Escenario:")
    print("    1  2  3  4  5  6  7  8  9 10")
    for i in range(10):
        fila = i + 1
        print(f"{fila:2d} ", end="")
        for j in range(10):
            if asientos[i][j] == "O":
                print("O", end="  ")
            else:
                print("X", end="  ")
        print()

# Función para mostrar el listado de asistentes
def mostrar_listado_asistentes():
    if not asistentes:
        print("No hay asistentes registrados.")
    else:
        print("Listado de asistentes:")
        for asistente in sorted(asistentes, key=lambda x: x["run"]):
            fila, columna = asistente["asiento"]
            asiento = fila * 10 + columna + 1
            print(f"Asiento {asiento}: RUN {asistente['run']}")

# Función para mostrar las ganancias totales
def mostrar_ganancias_totales():
    ganancias = {
        "Platinum": 0,
        "Gold": 0,
        "Silver": 0
    }
    for asistente in asistentes:
        fila, columna = asistente["asiento"]
        if fila < 2:
            ganancias["Platinum"] += precios["Platinum"]
        elif fila < 5:
            ganancias["Gold"] += precios["Gold"]
        else:
            ganancias["Silver"] += precios["Silver"]

    print("Ganancias totales por categoría:")
    for categoria, total in ganancias.items():
        print(f"{categoria}: ${total}")

# Función principal
def main():
    opciones = ["1", "2", "3", "4", "5"]
    while True:
        print("\n--- Menú ---")
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        opcion = validar_opcion(opciones)

        if opcion == "1":
            comprar_entradas()
        elif opcion == "2":
            mostrar_ubicaciones_disponibles()
        elif opcion == "3":
            mostrar_listado_asistentes()
        elif opcion == "4":
            mostrar_ganancias_totales()
        elif opcion == "5":
            fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"\nSaliendo del sistema - {fecha_actual}")
            break

if __name__ == "__main__":
    main()
    # https://github.com/mati12b/evalucion_transversal