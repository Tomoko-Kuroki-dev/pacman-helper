import subprocess

def buscar():
    paquete = input("¿Qué paquete buscas? ")

    if not paquete:
        print("No indicaste ningún paquete.")
        return 1

    resultado = subprocess.run(
        ["pacman", "-Ss", paquete]
        )

    return resultado.returncode