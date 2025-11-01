# SAE 1 - Python DNB

[SAE 1 - Python DNB | PDF](https://celene.univ-orleans.fr/pluginfile.php/1910057/mod_resource/content/1/sae1.pdf)

## Comment utiliser le projet ?

### Initialisation

Il vous faudra tout d'abord créer un environnement virtuel :

```bash
python3 -m venv .venv
```

et l'activer :

```bash
source .venv/bin/activate  # Linux
.\.venv\Scripts\activate.ps1  # Windows
```

Pour installer les paquets nécessaires au fonctionnement de l'application, utiliser la commande suivante :

```bash
pip install -r requirements.txt
```

### Utilisation

Enfin pour utiliser l'application vous devez faire la commande suivante :

```bash
python3 consultation_dnb.py
```

Puis il vous suffira d'aller dans un navigateur et à l'address `http://127.0.0.1:5000` pour utiliser l'application.

## Task

- [X] Initialiser le repo.
- [X] Implémenter les fonctions du fichier explore_dnb.py et ajouter mes propres fonctions.
- [X] Compléter le fichier tests_explore_dnb.py et ajouter les fonctions de test pour mes propres fonctions.
- [X] Compléter le fichier consultation_dnb.py qui permet de consulter et de manipuler les données chargées à partir d’un fichier CSV.
- [X] Faire un TUI pour consultation_dnb.py.
- [ ] Faire compte rendu
