.. _installation:

Installation et configuration
==============================

Cette page décrit comment installer et configurer OC Lettings pour le développement local.

Prérequis
---------

- Python 3.13 ou supérieur
- Git
- pip et virtualenv
- Docker (optionnel, pour le déploiement)

Installation locale
-------------------

1. **Cloner le dépôt**

   .. code-block:: bash

      git clone https://github.com/steveraffner/oc-lettings-refactored.git
      cd oc-lettings-refactored

2. **Créer un environnement virtuel**

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Sur Windows: venv\Scripts\activate

3. **Installer les dépendances**

   .. code-block:: bash

      pip install -r requirements.txt

4. **Configuration des variables d'environnement**

   Copier le fichier ``.env.example`` en ``.env`` et configurer :

   .. code-block:: bash

      cp .env.example .env

   Éditer le fichier ``.env`` :

   .. code-block:: text

      SECRET_KEY=votre-clé-secrète
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      SENTRY_DSN=  # Optionnel

5. **Appliquer les migrations**

   .. code-block:: bash

      python manage.py migrate

6. **Créer un superutilisateur (optionnel)**

   .. code-block:: bash

      python manage.py createsuperuser

7. **Lancer le serveur de développement**

   .. code-block:: bash

      python manage.py runserver

   L'application est accessible sur http://localhost:8000

Installation avec Docker
------------------------

Pour un déploiement rapide avec Docker :

.. code-block:: bash

   # Build de l'image
   docker build -t oc-lettings .

   # Lancement avec docker-compose
   docker-compose up

   # L'application est accessible sur http://localhost:8000

Tests
-----

Exécuter les tests :

.. code-block:: bash

   pytest

Avec couverture de code :

.. code-block:: bash

   pytest --cov=. --cov-report=html

Vérification du code
--------------------

Linting avec flake8 :

.. code-block:: bash

   flake8

Variables d'environnement
--------------------------

+------------------+------------------------------------------------+-------------+
| Variable         | Description                                    | Requis      |
+==================+================================================+=============+
| SECRET_KEY       | Clé secrète Django                             | Oui         |
+------------------+------------------------------------------------+-------------+
| DEBUG            | Mode debug (True/False)                        | Oui         |
+------------------+------------------------------------------------+-------------+
| ALLOWED_HOSTS    | Liste des hôtes autorisés (CSV)                | Oui         |
+------------------+------------------------------------------------+-------------+
| SENTRY_DSN       | URL Sentry pour le monitoring                  | Non         |
+------------------+------------------------------------------------+-------------+
| DATABASE_URL     | URL de la base de données                      | Non         |
+------------------+------------------------------------------------+-------------+
