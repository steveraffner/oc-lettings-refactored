# 🏠 OC Lettings - Refonte Architecture Modulaire

[![CI/CD Pipeline](https://github.com/[VOTRE-USERNAME]/oc-lettings/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/[VOTRE-USERNAME]/oc-lettings/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Django 4.2](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/r/[VOTRE-USERNAME]/oc-lettings)
[![Coverage](https://img.shields.io/badge/coverage-80%25+-success.svg)](https://pytest.org/)

Application web Django de gestion de locations immobilières avec architecture modulaire, pipeline CI/CD, monitoring Sentry et documentation complète.

## 📋 Table des matières

- [Aperçu du projet](#-aperçu-du-projet)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture](#-architecture)
- [Installation locale](#-installation-locale)
- [Tests](#-tests)
- [Déploiement](#-déploiement)
- [Technologies utilisées](#-technologies-utilisées)
- [Documentation](#-documentation)

## 🎯 Aperçu du projet

OC Lettings est une application Django refactorisée pour améliorer sa maintenabilité, sa performance et sa scalabilité. Le projet a été restructuré avec une architecture modulaire en 3 applications distinctes.

### Améliorations apportées

- ✅ **Architecture modulaire** : Séparation en 3 apps (lettings, profiles, oc_lettings_site)
- ✅ **Dette technique réduite** : Code propre, documenté, tests >80%
- ✅ **CI/CD automatisé** : GitHub Actions avec tests, build et déploiement
- ✅ **Conteneurisation** : Image Docker optimisée
- ✅ **Monitoring** : Intégration Sentry pour le suivi des erreurs
- ✅ **Documentation** : Read The Docs avec Sphinx

## ✨ Fonctionnalités

- 🏡 **Gestion des locations** : Consultation des propriétés disponibles
- 👥 **Gestion des profils** : Profils utilisateurs avec villes favorites
- 🔐 **Interface admin** : Administration complète via Django Admin
- 📱 **Responsive** : Interface adaptative pour mobile et desktop
- 🐛 **Pages d'erreur personnalisées** : 404 et 500 avec design cohérent

## 🏗️ Architecture

### Structure du projet

```
oc-lettings/
├── oc_lettings_site/          # Application principale
│   ├── settings.py            # Configuration Django
│   ├── urls.py                # Routing principal
│   ├── views.py               # Vue page d'accueil
│   └── wsgi.py                # Point d'entrée WSGI
│
├── lettings/                  # App Locations
│   ├── models.py              # Address, Letting
│   ├── views.py               # index, letting
│   ├── urls.py                # Routes /lettings/
│   ├── admin.py               # Configuration admin
│   ├── tests.py               # Tests unitaires
│   └── migrations/            # Migrations DB
│
├── profiles/                  # App Profils
│   ├── models.py              # Profile
│   ├── views.py               # index, profile
│   ├── urls.py                # Routes /profiles/
│   ├── admin.py               # Configuration admin
│   ├── tests.py               # Tests unitaires
│   └── migrations/            # Migrations DB
│
├── templates/                 # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── 404.html
│   ├── 500.html
│   ├── lettings/
│   └── profiles/
│
├── static/                    # Fichiers statiques
│   └── css/
│
├── .github/workflows/         # CI/CD
│   └── ci-cd.yml
│
├── docs/                      # Documentation Sphinx
│   ├── conf.py
│   ├── index.rst
│   └── ...
│
├── Dockerfile                 # Image Docker
├── docker-compose.yml         # Configuration Docker Compose
├── requirements.txt           # Dépendances Python
├── pytest.ini                 # Configuration pytest
└── setup.cfg                  # Configuration flake8
```

### Modèles de données

```python
# lettings/models.py
class Address:
    - number: IntegerField
    - street: CharField(64)
    - city: CharField(64)
    - state: CharField(2)
    - zip_code: IntegerField
    - country_iso_code: CharField(3)

class Letting:
    - title: CharField(256)
    - address: OneToOneField(Address)

# profiles/models.py
class Profile:
    - user: OneToOneField(User)
    - favorite_city: CharField(64)
```

## 💻 Installation locale

### Prérequis

- Python 3.11+
- Git
- SQLite3 (inclus avec Python)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/[VOTRE-USERNAME]/oc-lettings.git
cd oc-lettings
```

2. **Créer et activer l'environnement virtuel**
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Appliquer les migrations**
```bash
python manage.py migrate
```

5. **Créer un superutilisateur (optionnel)**
```bash
python manage.py createsuperuser
```

6. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

7. **Accéder à l'application**
- Site : http://localhost:8000
- Admin : http://localhost:8000/admin
- Lettings : http://localhost:8000/lettings/
- Profiles : http://localhost:8000/profiles/

### Variables d'environnement (optionnel en local)

Créer un fichier `.env` à la racine :
```env
SECRET_KEY=votre-cle-secrete-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SENTRY_DSN=votre-dsn-sentry (optionnel)
```

## 🧪 Tests

### Lancer tous les tests
```bash
pytest
```

### Tests avec couverture
```bash
pytest --cov=. --cov-report=html
```

### Vérifier le linting
```bash
flake8
```

### Rapport de couverture
Après avoir lancé les tests avec couverture, ouvrir `htmlcov/index.html` dans le navigateur.

## 🐳 Docker

### Build de l'image Docker
```bash
docker build -t oc-lettings .
```

### Lancer le conteneur
```bash
docker run -p 8000:8000 \
  -e SECRET_KEY="votre-cle-secrete" \
  -e DEBUG=False \
  -e ALLOWED_HOSTS="localhost,127.0.0.1" \
  oc-lettings
```

### Avec Docker Compose
```bash
# Développement
docker-compose up

# Production
docker-compose -f docker-compose.prod.yml up
```

### Pull depuis Docker Hub
```bash
docker pull [VOTRE-USERNAME]/oc-lettings:latest
docker run -p 8000:8000 [VOTRE-USERNAME]/oc-lettings:latest
```

## 🚀 Déploiement

### Pipeline CI/CD

Le projet utilise GitHub Actions pour automatiser :
1. ✅ **Tests** : Exécution de la suite de tests
2. ✅ **Linting** : Vérification flake8
3. ✅ **Build Docker** : Construction de l'image
4. ✅ **Push Docker Hub** : Envoi sur Docker Hub (branche main uniquement)
5. ✅ **Déploiement** : Déploiement automatique sur [Render/Railway/Heroku]

### Workflow
```
git push origin main
    ↓
GitHub Actions
    ↓
Tests + Linting
    ↓
Build Docker Image
    ↓
Push to Docker Hub
    ↓
Deploy to Production
```

### Configuration requise

**Secrets GitHub Actions** (Settings > Secrets and variables > Actions) :
- `SECRET_KEY` : Clé secrète Django
- `DOCKER_USERNAME` : Username Docker Hub
- `DOCKER_PASSWORD` : Token Docker Hub
- `SENTRY_DSN` : DSN Sentry
- `RENDER_DEPLOY_HOOK` : URL de déploiement (si Render)

### Déploiement manuel

```bash
# Build et push
docker build -t [USERNAME]/oc-lettings:latest .
docker push [USERNAME]/oc-lettings:latest

# Déployer sur la plateforme
# Render/Railway/Heroku spécifique
```

## 🛠️ Technologies utilisées

### Backend
- **Python 3.11** : Langage de programmation
- **Django 4.2** : Framework web
- **Gunicorn** : Serveur WSGI pour production
- **WhiteNoise** : Gestion des fichiers statiques

### Base de données
- **SQLite3** : Développement
- **PostgreSQL** : Production

### Tests & Qualité
- **pytest** : Framework de tests
- **pytest-django** : Intégration Django
- **pytest-cov** : Couverture de tests
- **flake8** : Linting PEP 8

### DevOps
- **Docker** : Conteneurisation
- **GitHub Actions** : CI/CD
- **Docker Hub** : Registry d'images

### Monitoring & Documentation
- **Sentry** : Surveillance des erreurs
- **Sphinx** : Génération de documentation
- **Read The Docs** : Hébergement documentation

### Plateforme de déploiement
- **[Render/Railway/Heroku]** : Hébergement cloud

## 📚 Documentation

- **Documentation technique** : [https://[VOTRE-PROJET].readthedocs.io](https://[VOTRE-PROJET].readthedocs.io)
- **Repository GitHub** : [https://github.com/[VOTRE-USERNAME]/oc-lettings](https://github.com/[VOTRE-USERNAME]/oc-lettings)
- **Docker Hub** : [https://hub.docker.com/r/[VOTRE-USERNAME]/oc-lettings](https://hub.docker.com/r/[VOTRE-USERNAME]/oc-lettings)
- **Site en production** : [https://[VOTRE-APP].[plateforme].com](https://[VOTRE-APP].[plateforme].com)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

### Standards de code

- Respecter PEP 8 (vérifier avec `flake8`)
- Ajouter des docstrings à toutes les fonctions
- Maintenir une couverture de tests >80%
- Tester localement avant de push

## 📝 Licence

Ce projet est développé dans le cadre de la formation OpenClassrooms - Développeur d'application Python.

## 👤 Auteur

**Steve Raffner**
- GitHub : [@[VOTRE-USERNAME]](https://github.com/[VOTRE-USERNAME])

## 🙏 Remerciements

- OpenClassrooms pour le projet initial
- La communauté Django
- Tous les contributeurs

---

**Version** : 2.0  
**Dernière mise à jour** : Janvier 2026
