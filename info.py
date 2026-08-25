import subprocess

def informacion():
    consulta = input("¿Qué paquete quieres consultar? ").split()
    if not consulta:
        print("No indicaste ningún paquete")
        return 1
    resultado = subprocess.run(
        ["pacman", "-Si"] + consulta
    )
    return resultado.returncode