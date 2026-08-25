import subprocess

def instalar():
    programas = input("¿Qué programas deseas instalar? ").split()
    if not programas:
        print("No indicaste ningún programa")
        return 1
    resultado = subprocess.run(
        ["sudo", "pacman", "-S", "--noconfirm"] + programas
    )
    return resultado.returncode