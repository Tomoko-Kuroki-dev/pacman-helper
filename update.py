import subprocess
def actualizar():
    resultado = subprocess.run(["sudo", "pacman", "-Sy", "--noconfirm"])
    return resultado.returncode