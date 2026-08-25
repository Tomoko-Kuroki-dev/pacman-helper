import subprocess

def eliminar():
    paquetes = input(
        "¿Qué paquetes deseas eliminar? "
        "(Se eliminarán los paquetes, dependencias innecesarias "
        "y configuraciones gestionadas por pacman) "
    ).split()
    if not paquetes:
        print("No indicaste ningún paquete.")
        return 1
    resultado = subprocess.run(
        ["sudo", "pacman", "-Rns"] + paquetes
    )
    return resultado.returncode