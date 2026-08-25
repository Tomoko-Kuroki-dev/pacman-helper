import subprocess
def actualizar_sistema():
    resultado = subprocess.run(["sudo", "pacman", "-Syu"])
    return resultado.returncode