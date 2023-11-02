import json

def cargar_datos():
    try:
        with open('registros.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(registros):
    with open('registros.json', 'w') as archivo:
        json.dump(registros, archivo, indent=4)

def agregar_registro(registros, nombre, telefono):
    registros.append({'nombre': nombre, 'telefono': telefono})
    guardar_datos(registros)
    print('Registro agregado exitosamente.')

def mostrar_registros(registros):
    if not registros:
        print('No hay registros disponibles.')
    else:
        for i, registro in enumerate(registros, start=1):
            print(f"{i}. Nombre: {registro['nombre']}, Teléfono: {registro['telefono']}")

def modificar_registro(registros, numero, nombre, telefono):
    if 1 <= numero <= len(registros):
        registros[numero - 1] = {'nombre': nombre, 'telefono': telefono}
        guardar_datos(registros)
        print('Registro modificado exitosamente.')
    else:
        print('Número de registro inválido.')

def eliminar_registro(registros, numero):
    if 1 <= numero <= len(registros):
        del registros[numero - 1]
        guardar_datos(registros)
        print('Registro eliminado exitosamente.')
    else:
        print('Número de registro inválido.')

def main():
    registros = cargar_datos()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar registro")
        print("2. Mostrar registros")
        print("3. Modificar registro")
        print("4. Eliminar registro")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            agregar_registro(registros, nombre, telefono)
        elif opcion == '2':
            mostrar_registros(registros)
        elif opcion == '3':
            mostrar_registros(registros)
            numero = int(input("Ingrese el número de registro que desea modificar: "))
            nombre = input("Ingrese el nuevo nombre: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            modificar_registro(registros, numero, nombre, telefono)
        elif opcion == '4':
            mostrar_registros(registros)
            numero = int(input("Ingrese el número de registro que desea eliminar: "))
            eliminar_registro(registros, numero)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()



