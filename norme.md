# Norme de codage Python - PEP 8

## Introduction

Ce document décrit les conventions de codage Python basées sur **PEP 8** (Python Enhancement Proposal 8), le guide de style officiel pour le code Python.

**Philosophie :** Le code est lu beaucoup plus souvent qu'il n'est écrit. La lisibilité compte.

---

## Table des matières

1. [Indentation et mise en forme](#1-indentation-et-mise-en-forme)
2. [Longueur des lignes](#2-longueur-des-lignes)
3. [Imports](#3-imports)
4. [Espaces](#4-espaces)
5. [Commentaires et docstrings](#5-commentaires-et-docstrings)
6. [Conventions de nommage](#6-conventions-de-nommage)
7. [Structure d'un fichier](#7-structure-dun-fichier)
8. [Type hints](#8-type-hints)
9. [Bonnes pratiques](#9-bonnes-pratiques)
10. [Outils](#10-outils)

---

## 1. Indentation et mise en forme

### Règle de base
- **4 espaces** par niveau d'indentation
- **Jamais de tabs**
- Pas de mélange espaces/tabs

```python
# ✅ BON
def function(arg):
    if arg:
        return True
    return False

# ❌ MAUVAIS : 2 espaces
def function(arg):
  if arg:
    return True
  return False

# ❌ MAUVAIS : tabs
def function(arg):
    if arg:
        return True
    return False
```

### Continuation de ligne

```python
# ✅ BON : Alignement avec le délimiteur
result = some_function(
    argument1, argument2,
    argument3, argument4
)

# ✅ BON : Indentation suspendue (hanging indent)
result = some_function(
    argument1,
    argument2,
    argument3,
)

# ✅ BON : Avec des dictionnaires
config = {
    "token": "xxx",
    "prefix": "!",
    "database": "postgresql://...",
}

# ❌ MAUVAIS : Pas d'alignement
result = some_function(argument1, argument2,
    argument3, argument4)
```

---

## 2. Longueur des lignes

### Règles
- **79 caractères** maximum (PEP 8 strict)
- **88 caractères** avec Black (recommandé pour ce projet)
- **72 caractères** pour les docstrings et commentaires

```python
# ✅ BON : Ligne courte
user_id = get_user_id_from_database(username)

# ✅ BON : Découpage si trop long
user_id = get_user_id_from_database(
    username=username,
    guild_id=guild_id,
    cache_enabled=True,
)

# ❌ MAUVAIS : Trop long
user_id = get_user_id_from_database(username, guild_id, cache_enabled=True, retry_count=3, timeout=30)
```

---

## 3. Imports

### Organisation
1. Standard library imports
2. Related third party imports
3. Local application/library imports
4. Une ligne blanche entre chaque groupe

```python
# ✅ BON
# Standard library
import os
import sys
from typing import Dict, List, Optional

# Third-party
import aiohttp
import websockets
from dotenv import load_dotenv

# Local
from core.gateway import Gateway
from core.http_client import HTTPClient
from shared.config import Config
from shared.logger import logger
```

### Règles d'imports

```python
# ✅ BON : Un import par ligne
import os
import sys

# ✅ BON : Imports multiples d'un même module
from typing import Dict, List, Optional

# ❌ MAUVAIS : Imports multiples sur une ligne
import os, sys

# ✅ BON : Import absolu
from core.gateway import Gateway

# ❌ ÉVITER : Import relatif (sauf dans un package)
from ..core.gateway import Gateway

# ✅ BON : Imports triés alphabétiquement
import aiohttp
import asyncio
import json
import websockets
```

### Imports conditionnels

```python
# ✅ BON : À la fin des imports
import os
import sys

if sys.platform == 'win32':
    import winreg
else:
    import pwd
```

---

## 4. Espaces

### Autour des opérateurs

```python
# ✅ BON
x = 1
y = 2
result = x + y
flag = x == 1 and y == 2

# ❌ MAUVAIS
x=1
y=2
result=x+y
flag=x==1and y==2
```

### Dans les fonctions

```python
# ✅ BON
def function(arg1, arg2, arg3=None):
    pass

result = function(1, 2, arg3=3)

# ❌ MAUVAIS
def function( arg1, arg2, arg3 = None ):
    pass

result = function (1, 2, arg3 = 3)
```

### Dans les structures

```python
# ✅ BON
my_list = [1, 2, 3, 4, 5]
my_dict = {"key": "value"}
my_tuple = (1, 2)

# ❌ MAUVAIS
my_list = [ 1,2,3,4,5 ]
my_dict = { "key" : "value" }
my_tuple = (1,2)
```

### Lignes blanches

```python
# 2 lignes blanches avant les classes et fonctions de niveau supérieur
import os


class MyClass:
    pass


def my_function():
    pass


# 1 ligne blanche entre les méthodes d'une classe
class MyClass:
    def method1(self):
        pass

    def method2(self):
        pass


# Pas de ligne blanche inutile
def function():
    x = 1
    
    y = 2  # ❌ Ligne blanche inutile
    
    return x + y
```

---

## 5. Commentaires et docstrings

### Commentaires en ligne

```python
# ✅ BON : Commentaire descriptif
x = x + 1  # Incrémente le compteur

# ✅ BON : Commentaire au-dessus
# Calcule la moyenne des scores
average = sum(scores) / len(scores)

# ❌ MAUVAIS : Évident
x = x + 1  # Ajoute 1 à x

# ❌ MAUVAIS : Commentaire obsolète
x = x + 2  # Incrémente le compteur
```

### Docstrings (fonctions)

```python
# ✅ BON : Docstring complète (style Google)
def add_task(name: str, priority: int = 0, tags: List[str] = None) -> dict:
    """
    Ajoute une tâche à la liste.

    Cette fonction crée une nouvelle tâche avec le nom et la priorité
    spécifiés, puis l'ajoute à la base de données.

    Args:
        name: Le nom de la tâche (obligatoire)
        priority: La priorité de la tâche (0 = basse, 1 = haute)
        tags: Liste optionnelle de tags

    Returns:
        Un dictionnaire contenant la tâche créée avec les clés:
        - id: Identifiant unique
        - name: Nom de la tâche
        - priority: Priorité
        - created_at: Date de création

    Raises:
        ValueError: Si le nom est vide ou None
        DatabaseError: Si l'insertion échoue

    Example:
        >>> task = add_task("Réunion BDE", priority=1)
        >>> print(task["name"])
        Réunion BDE
    """
    if not name:
        raise ValueError("Le nom ne peut pas être vide")
    
    # Implementation...
    return {"id": 1, "name": name, "priority": priority}


# ✅ BON : Docstring courte (une ligne)
def get_user_name(user_id: int) -> str:
    """Retourne le nom d'utilisateur à partir de son ID."""
    return users.get(user_id, "Unknown")


# ❌ MAUVAIS : Pas de docstring
def important_function(arg1, arg2):
    return arg1 + arg2
```

### Docstrings (classes)

```python
# ✅ BON
class TaskManager:
    """
    Gestionnaire de tâches pour le bot Discord.

    Cette classe gère toutes les opérations CRUD sur les tâches,
    incluant la création, la lecture, la mise à jour et la suppression.

    Attributes:
        tasks: Liste des tâches en mémoire
        db_connection: Connexion à la base de données
        logger: Instance du logger

    Example:
        >>> manager = TaskManager(db_connection)
        >>> task = manager.add_task("Nouvelle tâche")
    """

    def __init__(self, db_connection):
        """
        Initialise le gestionnaire de tâches.

        Args:
            db_connection: Connexion à la base de données
        """
        self.tasks = []
        self.db_connection = db_connection
        self.logger = get_logger(__name__)
```

### Docstrings (modules)

```python
# ✅ BON : En haut du fichier
"""
Module de gestion des tâches.

Ce module fournit les fonctionnalités pour créer, lister, modifier
et supprimer des tâches pour le bot Discord du BDE.

Classes:
    TaskManager: Gestionnaire principal des tâches
    TaskDatabase: Interface avec la base de données

Functions:
    format_task: Formate une tâche pour l'affichage Discord
    validate_task: Valide les données d'une tâche

Constants:
    MAX_TASKS: Nombre maximum de tâches par utilisateur
    DEFAULT_PRIORITY: Priorité par défaut
"""

import os
from typing import List, Dict

MAX_TASKS = 100
DEFAULT_PRIORITY = 0
```

---

## 6. Conventions de nommage

### Résumé

| Type | Convention | Exemple |
|------|------------|---------|
| Variables/Fonctions | `snake_case` | `user_name`, `get_user()` |
| Constantes | `UPPER_CASE` | `MAX_TASKS`, `API_KEY` |
| Classes | `PascalCase` | `TaskManager`, `HTTPClient` |
| Méthodes | `snake_case` | `add_task()`, `get_user_id()` |
| Privé | `_leading_underscore` | `_internal_method()` |
| Très privé | `__double_leading` | `__private_attr` |
| Modules | `snake_case` | `http_client.py`, `task_manager.py` |

### Variables et fonctions

```python
# ✅ BON
user_name = "Alice"
task_count = 0

def get_user_by_id(user_id):
    pass

def calculate_average_score(scores):
    pass

# ❌ MAUVAIS
userName = "Alice"  # camelCase
TaskCount = 0       # PascalCase

def GetUserById(user_id):  # PascalCase
    pass

def CalculateAverageScore(scores):  # PascalCase
    pass
```

### Classes

```python
# ✅ BON
class TaskManager:
    pass

class HTTPClient:
    pass

class DatabaseConnection:
    pass

# ❌ MAUVAIS
class taskManager:  # snake_case
    pass

class Http_Client:  # snake_case
    pass
```

### Constantes

```python
# ✅ BON
MAX_TASKS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://discord.com/api/v10"

# ❌ MAUVAIS
max_tasks = 100  # snake_case
MaxTasks = 100   # PascalCase
```

### Méthodes privées et publiques

```python
class TaskManager:
    def __init__(self):
        self.tasks = []           # Public
        self._cache = {}          # Privé (convention)
        self.__secret = "xxx"     # Très privé (name mangling)
    
    def add_task(self, name):     # Public
        """Méthode publique."""
        self._validate(name)
        # ...
    
    def _validate(self, name):    # Privé (convention)
        """Méthode interne, ne pas appeler directement."""
        if not name:
            raise ValueError("Invalid name")
    
    def __internal_method(self):  # Très privé
        """Méthode vraiment interne."""
        pass
```

### Noms à éviter

```python
# ❌ MAUVAIS : Noms d'une seule lettre (sauf dans les boucles)
def calculate(a, b, c):
    pass

# ✅ BON
def calculate(width, height, depth):
    pass

# ✅ EXCEPTION : Boucles courtes
for i in range(10):
    print(i)

for x, y in coordinates:
    print(x, y)

# ❌ MAUVAIS : Noms réservés Python
list = [1, 2, 3]  # Écrase le type built-in
dict = {}         # Écrase le type built-in

# ✅ BON
task_list = [1, 2, 3]
config_dict = {}
```

---

## 7. Structure d'un fichier

### Template standard

```python
"""
Docstring du module.

Description détaillée du module et de son rôle.
"""

# Standard library imports
import os
import sys
from typing import Dict, List, Optional

# Third-party imports
import aiohttp
import websockets

# Local imports
from core.gateway import Gateway
from shared.config import Config

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Module-level variables (éviter si possible)
_cache: Dict[str, str] = {}


# Classes
class MyClass:
    """Docstring de la classe."""
    
    def __init__(self):
        """Docstring du constructeur."""
        pass
    
    def public_method(self):
        """Docstring de la méthode publique."""
        pass
    
    def _private_method(self):
        """Docstring de la méthode privée."""
        pass


# Functions
def public_function(arg1: str, arg2: int = 0) -> str:
    """Docstring de la fonction publique."""
    pass


def _helper_function(data: dict) -> list:
    """Docstring de la fonction helper."""
    pass


# Main execution
if __name__ == "__main__":
    # Code qui s'exécute uniquement si le fichier est lancé directement
    main()
```

### Ordre des éléments dans une classe

```python
class TaskManager:
    """Gestionnaire de tâches."""
    
    # 1. Attributs de classe (constantes)
    MAX_TASKS = 100
    
    # 2. Constructeur
    def __init__(self, db_connection):
        """Initialise le gestionnaire."""
        self.db = db_connection
        self.tasks = []
    
    # 3. Propriétés
    @property
    def task_count(self) -> int:
        """Retourne le nombre de tâches."""
        return len(self.tasks)
    
    # 4. Méthodes publiques
    def add_task(self, name: str) -> dict:
        """Ajoute une tâche."""
        pass
    
    def get_task(self, task_id: int) -> dict:
        """Récupère une tâche."""
        pass
    
    # 5. Méthodes privées
    def _validate_task(self, task: dict) -> bool:
        """Valide une tâche."""
        pass
    
    # 6. Méthodes magiques (sauf __init__)
    def __repr__(self) -> str:
        """Représentation de l'objet."""
        return f"TaskManager(tasks={self.task_count})"
    
    def __str__(self) -> str:
        """String de l'objet."""
        return f"TaskManager with {self.task_count} tasks"
```

---

## 8. Type hints

### Utilisation des type hints

```python
from typing import Dict, List, Optional, Union, Any, Tuple

# ✅ BON : Type hints clairs
def get_user(user_id: int) -> dict:
    """Récupère un utilisateur."""
    return {"id": user_id, "name": "Alice"}

def calculate_average(scores: List[int]) -> float:
    """Calcule la moyenne."""
    return sum(scores) / len(scores)

def find_user(name: str) -> Optional[dict]:
    """Trouve un utilisateur (peut retourner None)."""
    return users.get(name)

def process_data(data: Union[str, int]) -> str:
    """Traite des données de type str ou int."""
    return str(data)

# ✅ BON : Type hints complexes
def create_mapping(
    items: List[Tuple[str, int]]
) -> Dict[str, List[int]]:
    """Crée un mapping."""
    result: Dict[str, List[int]] = {}
    for key, value in items:
        if key not in result:
            result[key] = []
        result[key].append(value)
    return result

# ✅ BON : Type hints pour les méthodes async
async def fetch_data(url: str) -> dict:
    """Récupère des données async."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

### Type hints pour les classes

```python
from typing import List, Optional

class TaskManager:
    """Gestionnaire de tâches."""
    
    def __init__(self, db_connection: DatabaseConnection) -> None:
        """Initialise le gestionnaire."""
        self.db: DatabaseConnection = db_connection
        self.tasks: List[dict] = []
        self._cache: Dict[int, dict] = {}
    
    def add_task(self, name: str, priority: int = 0) -> dict:
        """Ajoute une tâche."""
        task: dict = {"name": name, "priority": priority}
        self.tasks.append(task)
        return task
    
    def get_task(self, task_id: int) -> Optional[dict]:
        """Récupère une tâche."""
        return self._cache.get(task_id)
```

---

## 9. Bonnes pratiques

### Comparaisons

```python
# ✅ BON : Comparaison avec None
if value is None:
    pass

if value is not None:
    pass

# ❌ MAUVAIS
if value == None:
    pass

# ✅ BON : Vérification booléenne
if items:  # Liste non vide
    pass

if not items:  # Liste vide
    pass

# ❌ MAUVAIS
if len(items) > 0:
    pass

if len(items) == 0:
    pass

# ✅ BON : Comparaison de types
if isinstance(value, str):
    pass

# ❌ MAUVAIS
if type(value) == str:
    pass
```

### Gestion d'exceptions

```python
# ✅ BON : Spécifique
try:
    value = int(user_input)
except ValueError as e:
    logger.error(f"Invalid input: {e}")
    value = 0

# ❌ MAUVAIS : Trop général
try:
    value = int(user_input)
except:  # Attrape tout, même KeyboardInterrupt
    value = 0

# ✅ BON : Exceptions multiples
try:
    data = json.loads(response)
except (json.JSONDecodeError, ValueError) as e:
    logger.error(f"Failed to parse JSON: {e}")
    data = {}
```

### Compréhensions

```python
# ✅ BON : Compréhension de liste simple
squares = [x**2 for x in range(10)]

# ✅ BON : Avec condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# ❌ MAUVAIS : Trop complexe (utiliser une boucle normale)
result = [
    process_item(item) for item in items
    if validate(item) and check_permission(item)
    and item.status == "active"
]

# ✅ BON : Boucle normale pour la clarté
result = []
for item in items:
    if not validate(item):
        continue
    if not check_permission(item):
        continue
    if item.status != "active":
        continue
    result.append(process_item(item))
```

### Context managers

```python
# ✅ BON : Utilisation de 'with'
with open("file.txt", "r") as f:
    content = f.read()

# ❌ MAUVAIS : Sans context manager
f = open("file.txt", "r")
content = f.read()
f.close()  # Peut être oublié

# ✅ BON : Context managers multiples
with open("input.txt", "r") as f_in, open("output.txt", "w") as f_out:
    f_out.write(f_in.read())
```

### F-strings

```python
# ✅ BON : F-strings (Python 3.6+)
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."

# ✅ BON : Expressions dans f-strings
total = f"Total: {sum(values):.2f}€"

# ❌ ÉVITER : Format ancien
message = "Hello, %s! You are %d years old." % (name, age)

# ❌ ÉVITER : .format() (sauf cas spéciaux)
message = "Hello, {}! You are {} years old.".format(name, age)
```

---

## 10. Outils

### Configuration Black

```toml
[tool.black]
line-length = 88
target-version = ['py313']
include = '\.pyi?$'
extend-exclude = '''
/(
    \.git
  | \.venv
  | build
  | dist
)/
'''
```

### Configuration Ruff

```toml
[tool.ruff]
line-length = 88
target-version = "py313"

select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "C",   # flake8-comprehensions
    "B",   # flake8-bugbear
    "UP",  # pyupgrade
]

ignore = [
    "E501",  # line too long (géré par Black)
]

[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]  # Unused imports OK
```

### Configuration isort

```toml
[tool.isort]
profile = "black"
line_length = 88
skip_gitignore = true
```

### Commandes utiles

```bash
# Formater le code
poetry run black src/

# Vérifier sans modifier
poetry run black --check src/

# Linter
poetry run ruff check src/

# Auto-fix
poetry run ruff check --fix src/

# Trier les imports
poetry run isort src/

# Tout en une fois
poetry run black src/ && poetry run isort src/ && poetry run ruff check src/
```

---

## Références

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

---

## Checklist avant commit

- [ ] Code formaté avec Black
- [ ] Imports triés avec isort
- [ ] Pas d'erreurs Ruff
- [ ] Docstrings présentes pour toutes les fonctions publiques
- [ ] Type hints ajoutés
- [ ] Tests passent
- [ ] Pas de variables `TODO` ou `FIXME` oubliées

---

*Document mis à jour : Novembre 2024*
*Version Python : 3.13+*