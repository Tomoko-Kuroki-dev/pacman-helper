import install
import update
import upgrade
import search
import info
import remove

def comprobar(resultado, mensaje_error, mensaje_exito):
    if resultado != 0:
        print(mensaje_error)
    else:
        print(mensaje_exito)


opciones = {
    "1": ("Instalación de paquetes", install.instalar),
    "2": ("Actualización de la base de datos", update.actualizar),
    "3": ("Actualización del sistema", upgrade.actualizar_sistema),
    "4": ("Búsqueda de paquetes", search.buscar),
    "5": ("Consulta del paquete", info.informacion),
    "6": ("Eliminación de paquetes", remove.eliminar),
}


while True:
    print("""
¿Qué quieres hacer?

1. Instalar paquetes
2. Actualizar bases de datos
3. Actualizar sistema
4. Buscar paquetes
5. Información del paquete
6. Eliminar paquetes
9. Salir
""")

    opcion = input("Opción: ")

    if opcion == "9":
        break

    if opcion in opciones:
        nombre, funcion = opciones[opcion]

        resultado = funcion()

        comprobar(
            resultado,
            f"{nombre} falló.",
            f"{nombre} terminado con éxito."
        )

    else:
        print("Opción no válida.")