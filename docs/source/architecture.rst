.. _architecture:

Architecture du projet
======================

Cette page décrit l'architecture technique d'OC Lettings.

Vue d'ensemble
--------------

OC Lettings suit une architecture modulaire Django basée sur le pattern MVT (Model-View-Template). Le projet est divisé en trois applications principales :

- ``oc_lettings_site`` : Application principale et point d'entrée
- ``lettings`` : Gestion des locations immobilières
- ``profiles`` : Gestion des profils utilisateurs

Structure du projet
-------------------

.. code-block:: text

   oc-lettings/
   ├── oc_lettings_site/      # Application principale
   │   ├── settings.py         # Configuration Django
   │   ├── urls.py             # Routage principal
   │   └── wsgi.py             # Point d'entrée WSGI
   ├── lettings/               # App locations
   │   ├── models.py           # Modèles Address, Letting
   │   ├── views.py            # Vues lettings
   │   ├── urls.py             # URLs lettings
   │   ├── admin.py            # Configuration admin
   │   └── tests.py            # Tests unitaires
   ├── profiles/               # App profils
   │   ├── models.py           # Modèle Profile
   │   ├── views.py            # Vues profils
   │   ├── urls.py             # URLs profils
   │   ├── admin.py            # Configuration admin
   │   └── tests.py            # Tests unitaires
   ├── templates/              # Templates HTML
   │   ├── base.html
   │   ├── index.html
   │   ├── 404.html
   │   ├── 500.html
   │   ├── lettings/
   │   └── profiles/
   ├── static/                 # Fichiers statiques
   ├── docs/                   # Documentation Sphinx
   ├── Dockerfile              # Configuration Docker
   ├── docker-compose.yml      # Orchestration Docker
   ├── requirements.txt        # Dépendances Python
   └── pytest.ini              # Configuration tests

Modèles de données
------------------

Application Lettings
~~~~~~~~~~~~~~~~~~~~

**Address**

.. code-block:: python

   class Address(models.Model):
       number = models.PositiveIntegerField()
       street = models.CharField(max_length=64)
       city = models.CharField(max_length=64)
       state = models.CharField(max_length=2)
       zip_code = models.PositiveIntegerField()
       country_iso_code = models.CharField(max_length=3)

**Letting**

.. code-block:: python

   class Letting(models.Model):
       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)

Application Profiles
~~~~~~~~~~~~~~~~~~~~

**Profile**

.. code-block:: python

   class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

Diagramme de relations
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   ┌─────────────┐
   │    User     │
   │  (Django)   │
   └─────┬───────┘
         │ 1:1
         │
   ┌─────▼───────┐
   │   Profile   │
   │             │
   └─────────────┘

   ┌─────────────┐       ┌─────────────┐
   │   Address   │ 1:1   │   Letting   │
   │             │◄──────┤             │
   └─────────────┘       └─────────────┘

Vues et URLs
------------

Namespaces
~~~~~~~~~~

- ``/`` : Page d'accueil (index)
- ``/lettings/`` : Application lettings (namespace: ``lettings``)
- ``/profiles/`` : Application profiles (namespace: ``profiles``)
- ``/admin/`` : Interface d'administration Django

Routes lettings
~~~~~~~~~~~~~~~

- ``lettings:index`` : Liste des locations
- ``lettings:letting`` : Détail d'une location

Routes profiles
~~~~~~~~~~~~~~~

- ``profiles:index`` : Liste des profils
- ``profiles:profile`` : Détail d'un profil

Configuration
-------------

Settings Django
~~~~~~~~~~~~~~~

Le fichier ``settings.py`` utilise ``python-decouple`` pour la gestion des variables d'environnement :

- ``SECRET_KEY`` : Clé secrète (depuis .env)
- ``DEBUG`` : Mode debug (depuis .env)
- ``ALLOWED_HOSTS`` : Hôtes autorisés (depuis .env)

Middleware
~~~~~~~~~~

1. SecurityMiddleware (Django)
2. **WhiteNoiseMiddleware** (fichiers statiques)
3. SessionMiddleware (Django)
4. CommonMiddleware (Django)
5. CsrfViewMiddleware (Django)
6. AuthenticationMiddleware (Django)
7. MessageMiddleware (Django)
8. ClickjackingMiddleware (Django)

Intégrations
------------

Sentry
~~~~~~

Monitoring des erreurs configuré via ``SENTRY_DSN`` :

- Traces : 10% en production
- Profiling : 10% en production
- Environment tags : development/production

WhiteNoise
~~~~~~~~~~

Serveur de fichiers statiques pour production :

- Compression automatique
- Cache optimisé
- Manifest pour versioning

Tests
-----

Structure des tests
~~~~~~~~~~~~~~~~~~~

Chaque application contient un fichier ``tests.py`` avec :

- Tests des modèles (création, ``__str__``, validations)
- Tests des vues (status codes, contenu, templates)
- Utilisation de pytest et pytest-django
- Fixtures Django pour l'isolation

Couverture
~~~~~~~~~~

Objectif : **> 80% de couverture**

Configuration dans ``.coveragerc`` :

- Exclusion des migrations
- Exclusion des fichiers de configuration
- Exclusion de l'environnement virtuel

Sécurité
--------

Mesures de sécurité implémentées :

- SECRET_KEY stockée en variable d'environnement
- DEBUG=False en production
- ALLOWED_HOSTS configuré
- CSRF protection activé
- Clickjacking protection
- WhiteNoise pour les fichiers statiques
- Utilisateur non-root dans Docker
