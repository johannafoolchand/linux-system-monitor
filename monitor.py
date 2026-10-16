
import platform
import shutil
import os
import time
import psutil

def afficher_systeme():
    print("=" * 40)
    print("         SYSTEM MONITOR")
    print("=" * 40)

    print(f"Système : {platform.system()}")
    print(f"Version : {platform.release()}")
    # Surveillance du processeur et de la mémoire
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()

    print(f"CPU utilisé : {cpu}%")
    print(f"RAM utilisée : {ram.percent}%")
    print(f"RAM disponible : {ram.available / (1024 ** 3):.2f} Go")

    # Espace disque
    total, utilise, libre = shutil.disk_usage("/")

    pourcentage_disque = (utilise / total) * 100

    print(f"Disque utilisé : {pourcentage_disque:.1f}%")
    print(f"Espace libre : {libre / (1024 ** 3):.2f} Go")

    # Mémoire vive
    if os.path.exists("/proc/meminfo"):
        with open("/proc/meminfo", "r") as fichier:
            lignes = fichier.readlines()

        memoire = {}
        for ligne in lignes:
            cle, valeur = ligne.split(":", 1)
            memoire[cle] = int(valeur.strip().split()[0])

        total_ram = memoire["MemTotal"]
        disponible_ram = memoire["MemAvailable"]
        ram_utilisee = total_ram - disponible_ram
        pourcentage_ram = (ram_utilisee / total_ram) * 100

        print(f"RAM utilisée : {pourcentage_ram:.1f}%")
    else:
        print("RAM détaillée : affichée si disponible sur le système")

if __name__ == "__main__":
    afficher_systeme()


