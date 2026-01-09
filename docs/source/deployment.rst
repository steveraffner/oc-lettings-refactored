.. _deployment:

Déploiement et CI/CD
====================

Cette page décrit le processus de déploiement et la pipeline CI/CD.

Pipeline CI/CD
--------------

Le projet utilise **GitHub Actions** pour l'intégration et le déploiement continus.

Workflow
~~~~~~~~

La pipeline s'exécute sur trois jobs séquentiels :

1. **Test** : Tests unitaires et qualité du code
2. **Build** : Construction et publication de l'image Docker
3. **Deploy** : Déploiement en production (branche main uniquement)

.. code-block:: yaml

   Trigger (push/PR)
        ↓
   ┌────────────┐
   │    Test    │  ← flake8 + pytest + coverage
   └─────┬──────┘
         ↓
   ┌────────────┐
   │   Build    │  ← Docker build + push
   └─────┬──────┘
         ↓
   ┌────────────┐
   │   Deploy   │  ← Render webhook (main only)
   └────────────┘

Job 1 : Tests
~~~~~~~~~~~~~

- Checkout du code
- Setup Python 3.13
- Installation des dépendances
- Exécution de flake8 (linting)
- Exécution de pytest avec couverture
- Upload vers Codecov

Job 2 : Build Docker
~~~~~~~~~~~~~~~~~~~~

- Build multi-architecture (amd64/arm64)
- Tag avec SHA du commit
- Tag avec nom de branche
- Tag ``latest`` pour main
- Push vers Docker Hub
- Cache des layers Docker

Job 3 : Déploiement
~~~~~~~~~~~~~~~~~~~

- Déclenchement uniquement sur ``main``
- Webhook vers Render
- Notification de déploiement

Secrets GitHub
--------------

Configurer dans Settings → Secrets :

+------------------------+------------------------------------------+
| Secret                 | Description                              |
+========================+==========================================+
| DOCKER_USERNAME        | Nom d'utilisateur Docker Hub             |
+------------------------+------------------------------------------+
| DOCKER_PASSWORD        | Token d'accès Docker Hub                 |
+------------------------+------------------------------------------+
| RENDER_DEPLOY_HOOK     | URL du webhook Render                    |
+------------------------+------------------------------------------+

Déploiement Docker
------------------

Build manuel
~~~~~~~~~~~~

.. code-block:: bash

   # Build de l'image
   docker build -t oc-lettings:latest .

   # Lancement local
   docker run -p 8000:8000 \
     -e SECRET_KEY="your-secret-key" \
     -e DEBUG=False \
     -e ALLOWED_HOSTS="yourdomain.com" \
     oc-lettings:latest

Docker Compose
~~~~~~~~~~~~~~

Pour le développement :

.. code-block:: bash

   docker-compose up

Configuration :

.. code-block:: yaml

   services:
     web:
       build: .
       ports:
         - "8000:8000"
       environment:
         - DEBUG=False
         - SECRET_KEY=${SECRET_KEY}
         - SENTRY_DSN=${SENTRY_DSN}

Déploiement sur Render
-----------------------

Configuration
~~~~~~~~~~~~~

1. **Créer un nouveau Web Service**
2. **Connecter le dépôt GitHub**
3. **Configuration** :

   - Environment : Docker
   - Branch : main
   - Health Check Path : /

4. **Variables d'environnement** :

   .. code-block:: text

      SECRET_KEY=<génerer-clé-sécurisée>
      DEBUG=False
      ALLOWED_HOSTS=oc-lettings.onrender.com
      SENTRY_DSN=<votre-dsn-sentry>

5. **Déploiement automatique** :
   
   - Activé sur push vers main
   - Webhook configuré dans GitHub Actions

Monitoring Sentry
-----------------

Configuration
~~~~~~~~~~~~~

1. Créer un projet sur sentry.io
2. Copier le DSN
3. Configurer dans .env ou variables Render

.. code-block:: bash

   SENTRY_DSN=https://xxx@yyy.ingest.sentry.io/zzz

Fonctionnalités
~~~~~~~~~~~~~~~

- Capture automatique des exceptions
- Traces de performance (10% sampling en prod)
- Profiling (10% sampling en prod)
- Tags d'environnement (dev/prod)
- Breadcrumbs pour le contexte

Stratégie de déploiement
-------------------------

Branches
~~~~~~~~

- ``develop`` : Développement continu, tests automatiques
- ``main`` : Production, déploiement automatique

Workflow Git
~~~~~~~~~~~~

.. code-block:: text

   develop ────┬──────┬──────┬──→ (tests)
               │      │      │
               ↓      ↓      ↓
              PR1    PR2    PR3
               │      │      │
               └──────┴──────┴──→ main ──→ deploy

Release
~~~~~~~

1. Développer sur ``develop``
2. Tests validés
3. Merge vers ``main`` via Pull Request
4. Déploiement automatique
5. Tag de version (optionnel)

.. code-block:: bash

   git tag -a v1.0.0 -m "Release 1.0.0"
   git push origin v1.0.0

Rollback
~~~~~~~~

En cas de problème :

.. code-block:: bash

   # Revenir au commit précédent
   git revert HEAD
   git push origin main

   # Ou redéployer une version spécifique
   git checkout v0.9.0
   git push -f origin main

Monitoring post-déploiement
----------------------------

Vérifications
~~~~~~~~~~~~~

1. **Health check** : https://oc-lettings.onrender.com/
2. **Admin** : https://oc-lettings.onrender.com/admin/
3. **Sentry** : Vérifier les erreurs
4. **Logs** : Consulter sur Render

Métriques
~~~~~~~~~

- Temps de réponse
- Taux d'erreur
- Utilisation mémoire
- Requêtes/seconde

Checklist de déploiement
-------------------------

Avant le déploiement
~~~~~~~~~~~~~~~~~~~~

☐ Tests passent localement
☐ Couverture > 80%
☐ Flake8 sans erreurs
☐ Migrations créées et testées
☐ Variables d'environnement configurées
☐ Documentation à jour

Après le déploiement
~~~~~~~~~~~~~~~~~~~~

☐ Application accessible
☐ Admin fonctionnel
☐ Pas d'erreurs Sentry
☐ Logs sans erreurs critiques
☐ Temps de réponse acceptable
☐ Fichiers statiques servis

Dépannage
---------

Problèmes courants
~~~~~~~~~~~~~~~~~~

**Build Docker échoue**

- Vérifier le Dockerfile
- Vérifier requirements.txt
- Nettoyer le cache : ``docker system prune -a``

**Déploiement Render échoue**

- Vérifier les variables d'environnement
- Consulter les logs Render
- Vérifier le Health Check

**Erreurs 500 en production**

- Consulter Sentry
- Vérifier DEBUG=False
- Vérifier ALLOWED_HOSTS
- Vérifier les migrations

Commandes utiles
----------------

.. code-block:: bash

   # Logs Docker
   docker-compose logs -f

   # Shell dans le container
   docker-compose exec web python manage.py shell

   # Migrations
   docker-compose exec web python manage.py migrate

   # Collectstatic
   docker-compose exec web python manage.py collectstatic

   # Créer superuser
   docker-compose exec web python manage.py createsuperuser
