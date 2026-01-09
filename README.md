# OC Lettings - Refactoring et Déploiement

[![CI/CD Pipeline](https://github.com/steveraffner/oc-lettings-refactored/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/steveraffner/oc-lettings-refactored/actions)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Django 4.2](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)

Application Django modernisée pour la gestion de locations immobilières et de profils utilisateurs.

## 🚀 Installation rapide

\`\`\`bash
git clone https://github.com/steveraffner/oc-lettings-refactored.git
cd oc-lettings-refactored
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
\`\`\`

## 📚 Documentation complète

La documentation détaillée est disponible dans le dossier \`docs/\`.

Pour construire la documentation :

\`\`\`bash
cd docs && make html
\`\`\`

## 🧪 Tests

\`\`\`bash
pytest --cov=. --cov-report=html
flake8
\`\`\`

## 🐳 Docker

\`\`\`bash
docker-compose up
\`\`\`

---

**Projet OpenClassrooms** - Parcours Développeur Python
