# Linux System Monitor

## Présentation

Linux System Monitor est un projet Python de surveillance système. Il permet d’afficher dans le terminal plusieurs indicateurs de performance :

- L’utilisation du processeur (CPU)
- L’utilisation de la mémoire vive (RAM)
- La mémoire disponible
- L’espace disque utilisé et disponible

Le projet utilise la bibliothèque `psutil` pour récupérer les informations système. Il est actuellement testé sur macOS, avec un objectif de compatibilité Linux.
## Installation

Cloner le dépôt :

```bash
git clone https://github.com/johannafooolchand/linux-system-monitor.git
cd linux-system-monitor
Installer la dependance :
python3 -m pip install psutil

Utilisation :
python3 monitor.py

Technologies :
- Python 3
- psutil
- Git et GitHub
- macOS et Linux
