#  Téléprompteur de Soutenance - OC Lettings

**Durée : 15 minutes (±5 minutes)**  
**Date de soutenance : _________**

---

##  INTRODUCTION (1 minute)

> *"Bonjour , je vais vous présenter les améliorations apportées au site OC Lettings. J'ai travaillé sur 5 axes majeurs conformément à vos demandes :*
> 
> 1. *La refactorisation en architecture modulaire*
> 2. *La réduction de la dette technique*
> 3. *La mise en place d'un pipeline CI/CD avec Docker*
> 4. *L'intégration du monitoring avec Sentry*
> 5. *La documentation technique sur Read The Docs*
>
> *Je vais maintenant vous faire une démonstration complète du site et du processus de déploiement."*

---

##  PARTIE 1 : DÉMONSTRATION LOCALE (3 minutes)

###  Lancement du site en local

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Lancer le serveur de développement
python manage.py runserver
```

** À dire :**
> *"Voici le site fonctionnel sur http://localhost:8000. Lors de la mise en place de l'environnement de développement, j'ai rencontré quelques défis :*
> 
> - **[Mentionner vos problèmes réels]** : 
>   - *Problèmes de migrations de données*
>   - *Configuration de la base de données SQLite*
>   - *Gestion des dépendances Python*
>   - *Configuration des fichiers statiques*
> 
> *Je les ai résolus en [expliquer brièvement vos solutions]."*

###  Parcourir le site

**Montrer dans l'ordre :**

1. **Page d'accueil** (`http://localhost:8000/`)
   - *"Voici la page d'accueil avec le titre qui sera modifié pendant la démo"*

2. **Section Lettings** (`http://localhost:8000/lettings/`)
   - *"Liste des locations disponibles"*
   - Cliquer sur une location pour voir le détail

3. **Section Profiles** (`http://localhost:8000/profiles/`)
   - *"Liste des profils utilisateurs"*
   - Cliquer sur un profil pour voir le détail

4. **Interface Admin** (`http://localhost:8000/admin/`)
   - Se connecter avec les identifiants admin :
     - **Login :** `admin`
     - **Mot de passe :** `Abc1234!`
   - *"Notez la pluralisation correcte des modèles"*
   - Montrer : Lettings, Addresses, Profiles

---

## ️ PARTIE 2 : ARCHITECTURE MODULAIRE (2 minutes)

** À dire :**
> *"J'ai restructuré l'application monolithique initiale en 3 applications Django distinctes pour améliorer la maintenabilité et la scalabilité :*

###  Structure des applications

```
oc-lettings/
├── oc_lettings_site/     # Application principale
│   ├── __init__.py
│   ├── settings.py       # Configuration centrale
│   ├── urls.py           # Routing principal
│   └── views.py          # Page d'accueil
│
├── lettings/             # Application Locations
│   ├── models.py         # Address, Letting
│   ├── views.py          # Vues liste/détail
│   ├── urls.py           # Routes /lettings/
│   ├── admin.py          # Config admin
│   ├── tests.py          # Tests unitaires
│   └── migrations/       # Migrations données
│
└── profiles/             # Application Profils
    ├── models.py         # Profile
    ├── views.py          # Vues liste/détail
    ├── urls.py           # Routes /profiles/
    ├── admin.py          # Config admin
    ├── tests.py          # Tests unitaires
    └── migrations/       # Migrations données
```

** Continuer :**
> *"Les migrations personnalisées ont permis de copier les données des anciens modèles vers les nouveaux sans perte :*
> 
> - *Utilisation de `apps.get_model()` pour accéder aux modèles*
> - *Fonction `RunPython` pour copier les données*
> - *Suppression des anciens modèles après vérification*
> - *Aucune utilisation de SQL direct (RunSQL)*
>
> *Cette approche garantit une migration sûre et traçable."*

---

##  PARTIE 3 : RÉDUCTION DE LA DETTE TECHNIQUE (1,5 minute)

** À dire :**
> *"J'ai travaillé sur 5 points pour réduire la dette technique :*

###  1. Linting avec Flake8

> 🟢 **POUR TOI :** Flake8 = outil qui vérifie automatiquement la qualité du code Python (respect des conventions PEP 8, détection d'erreurs de syntaxe, lignes trop longues, etc.)
> 
> 🟢 **CE QUE TU FAIS :** Ouvre un terminal et tape `flake8` puis Entrée. Si aucun message n'apparaît = code propre ✅
> 
> 🟢 **FICHIER À MONTRER :** Le fichier `setup.cfg` qui contient la configuration flake8 (exclusions, longueur max des lignes)

```bash
flake8
```

> *"Aucune erreur de linting détectée. Le code respecte les conventions PEP 8."*

###  2. Docstrings

> 🟢 **POUR TOI :** Les docstrings = commentaires structurés au début des fonctions qui expliquent ce qu'elles font
> 
> 🟢 **CE QUE TU FAIS :** Ouvre un fichier de code (par exemple `lettings/views.py` ou `profiles/views.py`) et montre les docstrings avec les """ """
> 
> 🟢 **FICHIERS À MONTRER :** `lettings/views.py`, `profiles/views.py`, ou `oc_lettings_site/views.py`

> *"Tous les modules, classes et fonctions sont documentés avec des docstrings explicatives :*
> - *Description de la fonctionnalité*
> - *Paramètres d'entrée*
> - *Valeurs de retour*
> - *Exemples d'utilisation si nécessaire"*

**Exemple à montrer dans le code :**
```python
def index(request):
    """
    Affiche la page d'accueil du site OC Lettings.
    
    Args:
        request (HttpRequest): Requête HTTP Django
        
    Returns:
        HttpResponse: Page d'accueil rendue
    """
    return render(request, 'index.html')
```

###  3. Tests et couverture >80%

> 🟢 **POUR TOI :** Pytest = outil qui lance les tests automatiques. Coverage = pourcentage de code testé
> 
> 🟢 **CE QUE TU FAIS :** 
> 1. **IMPORTANT : Active d'abord l'environnement virtuel :** `source venv/bin/activate`
> 2. **Puis lance les tests :** `pytest --cov=. --cov-report=term-missing`
> 
> 🟢 **CE QUE TU VERRAS :** Une liste de tests qui passent (en vert) + un tableau avec le % de couverture par fichier
> - "15 passed" = 15 tests réussis ✅
> - "80% coverage" = couverture de code à 80%
> 
> 🟢 **FICHIERS DE TESTS :** `lettings/tests.py`, `profiles/tests.py`, `oc_lettings_site/tests.py`

```bash
# D'abord activer l'environnement virtuel
source venv/bin/activate

# Puis lancer les tests avec couverture
pytest --cov=. --cov-report=term-missing
```

> *"J'ai obtenu une couverture de 80% avec 15 tests passés :*
> - *7 tests pour l'application lettings (modèles + vues)*
> - *6 tests pour l'application profiles (modèles + vues)*
> - *2 tests pour la page d'accueil*
>
> *La couverture atteint exactement l'objectif de 80% fixé."*

> *"Couverture de test supérieure à 80% avec pytest-django et pytest-cov. Les tests couvrent :*
> - *Les modèles (création, validation)*
> - *Les vues (GET requests, contexte)*
> - *Les URLs (résolution des routes)*
> - *L'intégration admin"*

###  4. Pluralisation correcte dans l'admin

> 🟢 **POUR TOI :** Par défaut Django ajoute juste un "s" au pluriel, ce qui donnait "Addresss" au lieu de "Addresses"
> 
> 🟢 **CE QUE TU FAIS :** Va dans l'interface admin (http://localhost:8000/admin/) et montre que c'est écrit "Addresses" (pas "Addresss")
> 
> 🟢 **FICHIER À MONTRER :** `lettings/models.py` ligne avec `verbose_name_plural = "Addresses"` dans le modèle Address

> *"Configuration de `verbose_name_plural` dans les modèles pour corriger :*
> - *'Profiles' → 'Profiles' (correct)*
> - *'Addresss' → 'Addresses' (corrigé)"*

###  5. Pages d'erreur personnalisées

> 🟢 **POUR TOI :** Au lieu d'avoir des pages d'erreur moches par défaut, j'ai créé des pages stylisées
> 
> 🟢 **CE QUE TU FAIS - OPTION 1 (Montrer le code) :**
> - Ouvre les fichiers [templates/404.html](templates/404.html) et [templates/500.html](templates/500.html) dans VS Code
> - Montre le HTML avec le style personnalisé qui respecte le design du site
> 
> 🟢 **CE QUE TU FAIS - OPTION 2 (Tester en live) :**
> - ⚠️ **IMPORTANT :** Les pages personnalisées ne s'affichent qu'en mode production !
> - Dans le fichier **`.env`** à la racine du projet, change temporairement :
>   - `DEBUG=True` en `DEBUG=False`
> - **Note :** `LANGUAGE_CODE` est déjà configuré à `'fr-fr'` dans [oc_lettings_site/settings.py](oc_lettings_site/settings.py) ligne 102 pour corriger l'affichage des caractères français
> - Redémarre le serveur :
> 
> ```bash
> source venv/bin/activate
> python manage.py runserver
> ```
> 
> - Va sur http://localhost:8000/page-qui-existe-pas → page 404 personnalisée avec caractères français corrects
> - **⚠️ N'OUBLIE PAS de remettre `DEBUG=True` dans le fichier `.env` après la démo !**
> 
> 🟢 **FICHIERS :** [templates/404.html](templates/404.html) et [templates/500.html](templates/500.html)
> 
> 🟢 **PLUS SIMPLE :** Montre juste les fichiers HTML dans l'éditeur, pas besoin de changer DEBUG

> *"Création de templates personnalisés :*
> - *`404.html` : Page non trouvée*
> - *`500.html` : Erreur serveur*
>
> *Ces pages offrent une meilleure expérience utilisateur."*

---

##  PARTIE 4 : PIPELINE CI/CD ET DÉPLOIEMENT (5 minutes) 

###  Architecture du pipeline

** À dire :**
> *"Le pipeline CI/CD est configuré avec GitHub Actions et comprend 4 étapes automatisées :*

```yaml
Pipeline CI/CD :
1️⃣ Tests & Linting (pytest + flake8)
2️⃣ Build Docker (si tests OK)
3️⃣ Push Docker Hub (si branche main)
4️⃣ Déploiement automatique (si branche main)
```

**Montrer le fichier de configuration CI/CD** : [.github/workflows/ci-cd.yml](https://github.com/steveraffner/oc-lettings-refactored/blob/main/.github/workflows/ci-cd.yml)

---

###  DÉMONSTRATION : Pipeline CI/CD (OPTION SÛRE)

> ⚠️ **RECOMMANDATION** : Ne faites PAS de modification en direct pendant la démo pour éviter tout risque d'échec. Montrez plutôt l'historique des workflows qui ont réussi !

#### **Étape 1 : Montrer l'historique GitHub Actions** ⏱️ 2-3 min

**Aller sur GitHub Actions :**
```
https://github.com/steveraffner/oc-lettings-refactored/actions
```

1. Ouvrir l'onglet **Actions**
2. Montrer les **workflows récents qui ont réussi** ✅
3. Cliquer sur un workflow réussi (par exemple : "docs: add clickable link to CI/CD workflow fil...")
4. Expliquer chaque étape **déjà terminée**

** À dire en montrant un workflow réussi :**

> *"Voici un exemple de pipeline CI/CD qui s'est exécuté avec succès lors de mon dernier commit :*
> 
> - **✅ Tests et linting** : Vérification flake8 et exécution des tests pytest - 15 tests passés avec 80% de couverture
> - **✅ Build Docker image** : Construction de l'image Docker optimisée avec build multi-stage
> - **✅ Push Docker Hub** : Image poussée sur Docker Hub avec tag latest et SHA du commit
> - **✅ Deploy to production** : Déploiement automatique sur Render terminé avec succès
>
> *Le processus complet prend environ 5-7 minutes. Si une étape échoue, le pipeline s'arrête immédiatement et aucun déploiement n'est effectué, ce qui garantit qu'aucun code défectueux n'atteint la production."*

---
---

#### **Étape 5 : Vérifier le site déployé** ⏱️ 1 min

**Ouvrir l'URL de production :**
```
https://oc-lettings-av9a.onrender.com
```

** À dire :**
> *"Le déploiement est maintenant terminé. Vous pouvez constater que :*
> -  *Le nouveau titre apparaît bien : 'OC Lettings - Welcome 2026'*
> -  *Le site est entièrement fonctionnel en production*
> -  *Les fichiers statiques se chargent correctement*
> -  *La base de données PostgreSQL est opérationnelle"*

---

#### **Étape 2 : Vérifier Docker Hub** ⏱️ 30 sec

**Ouvrir Docker Hub dans le navigateur :**
```
https://hub.docker.com/r/immeuble11/oc-lettings
```

** À dire :**
> *"Voyons maintenant Docker Hub où les images sont stockées :*
> - *Voici le repository avec l'image Docker de l'application*
> - *Système de tags : `latest` pour la dernière version et `[SHA-commit]` pour chaque commit*
> - *L'image fait environ [XXX MB] grâce au build multi-stage optimisé*
> - *Elle contient l'application Django, toutes les dépendances et les fichiers statiques"*

---

#### **Étape 3 : Vérifier le site déployé** ⏱️ 1 min

**Ouvrir l'URL de production :**
```
https://oc-lettings-av9a.onrender.com
```

** À dire :**
> *"L'application est maintenant en production et entièrement fonctionnelle :*
> -  *Le site répond correctement*
> -  *Les fichiers statiques se chargent (CSS, images, JavaScript)*
> -  *La base de données PostgreSQL est opérationnelle*
> -  *Tout est configuré en mode production avec DEBUG=False"*

**Naviguer rapidement dans le site :**
- Page d'accueil
- Lettings
- Profiles

---

#### **Étape 4 : Pull et Run Docker en local** ⏱️ 1 min

```bash
# Pull de l'image depuis Docker Hub
docker pull immeuble11/oc-lettings:latest

# Lancement du conteneur
docker run -p 8000:8000 \
  -e SECRET_KEY="demo-secret-key-for-presentation" \
  -e DEBUG=False \
  -e ALLOWED_HOSTS="localhost,127.0.0.1" \
  immeuble11/oc-lettings:latest
```

** À dire :**
> *"Pour démontrer la portabilité, je lance maintenant l'image Docker localement :*
> - *Pull de l'image depuis Docker Hub*
> - *Port 8000 exposé*
> - *Variables d'environnement injectées*
> - *Application prête en quelques secondes*
> - *Build multi-stage optimisé pour réduire la taille*
> - *Utilisateur non-root pour la sécurité*
>
> *Cela garantit que l'application fonctionne exactement de la même manière en développement, en staging et en production."*

**Ouvrir `http://localhost:8000` pour vérifier**

---

> 💡 **OPTION ALTERNATIVE (Si vous voulez prendre un risque)** :
> 
> Vous pouvez tenter une modification en direct sur GitHub :
> 1. Sur GitHub, éditez `templates/index.html`
> 2. Changez simplement `Holiday Homes` → `Holiday Homes 2026`
> 3. Commit et observez le pipeline
> 
> ⚠️ **Risque** : Si ça échoue, ça peut stresser pendant la démo. **L'option sûre ci-dessus est recommandée !**

---

##  PARTIE 5 : MONITORING AVEC SENTRY (1,5 minute)

**Ouvrir Sentry dans le navigateur :**
```
https://steve-raffner.sentry.io/projects/oc-lettings/
```

** À dire :**
> *"J'ai intégré Sentry pour la surveillance en temps réel des erreurs en production :*

### Configuration

```python
# Dans settings.py
import sentry_sdk

SENTRY_DSN = config('SENTRY_DSN', default='')

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0 if DEBUG else 0.1,
        profiles_sample_rate=1.0 if DEBUG else 0.1,
        environment='development' if DEBUG else 'production',
        send_default_pii=False,
    )
```

** Continuer :**
> *"Les points clés de l'intégration Sentry :*
> - *DSN stocké en variable d'environnement (sécurisé)*
> - *Capture automatique des exceptions non gérées*
> - *Traces de performance (10% en production)*
> - *Profiling activé (10% en production)*
> - *Tags d'environnement (dev/production)*
> - *Contexte utilisateur et stack trace complète*
> - *Alertes par email en cas d'erreur critique"*

### Démonstration (optionnelle)

**Déclencher une erreur 500 :**
```python
# Créer temporairement une vue qui lève une exception
def trigger_error(request):
    division_by_zero = 1 / 0
```

**Montrer dans le dashboard Sentry :**
1. L'erreur capturée en temps réel
2. La stack trace complète
3. Les variables locales
4. Le contexte de la requête

** À dire :**
> *"Sentry nous permet de détecter et résoudre rapidement les bugs en production avant qu'ils n'affectent trop d'utilisateurs."*

---

##  PARTIE 6 : DOCUMENTATION SPHINX (1 minute)

**Ouvrir la documentation locale :**
```bash
cd docs
make html
open _build/html/index.html
```

Ou montrer la structure sur GitHub :
```
https://github.com/steveraffner/oc-lettings-refactored/tree/main/docs
```

** À dire :**
> *"La documentation technique est générée avec Sphinx et comprend :*

###  Structure de la documentation

1. **Installation** : Guide de mise en place locale
2. **Architecture** : Explication des 3 applications
3. **Déploiement** : Procédure CI/CD et Docker
4. **API/Modèles** : Documentation auto-générée depuis les docstrings
5. **Tests** : Guide pour lancer les tests
6. **Contribution** : Bonnes pratiques pour l'équipe

** Continuer :**
> *"Points importants :*
> - *Création avec Sphinx et reStructuredText*
> - *Génération automatique depuis les docstrings Python*
> - *Documentation des modèles, vues et configurations*
> - *Thème ReadTheDocs pour une meilleure lisibilité*
> - *Guide d'installation et de déploiement complets"*
> - *Recherche full-text intégrée"*

---

##  CONCLUSION (30 secondes)

** À dire :**
> *"Pour résumer, l'application OC Lettings est maintenant :*
> 
> -  **Modulaire** : Architecture en 3 applications indépendantes et maintenables
> -  **Propre** : Dette technique réduite, code documenté, tests >80%
> -  **Automatisée** : Pipeline CI/CD avec tests automatiques et déploiement continu
> -  **Conteneurisée** : Image Docker portable et reproductible
> -  **Surveillée** : Monitoring Sentry pour détecter les erreurs rapidement
> -  **Documentée** : Documentation complète sur Read The Docs
>
> *L'application est prête pour la production et peut facilement être mise à l'échelle pour l'expansion aux États-Unis. Le processus de déploiement est entièrement automatisé et sécurisé."*

---

##  CHECKLIST AVANT SOUTENANCE

###  Préparation technique

- [ ] Repository GitHub public accessible
- [ ] Site fonctionne en local (`python manage.py runserver`)
- [ ] Tests passent avec `pytest --cov` (>80%)
- [ ] Flake8 ne retourne aucune erreur
- [ ] Pipeline CI/CD configuré sur GitHub Actions
- [ ] Compte Docker Hub avec images disponibles
- [ ] Site déployé avec URL publique fonctionnelle
- [ ] Sentry configuré avec projet actif
- [ ] Documentation Sphinx générée
- [ ] Toutes les variables d'environnement configurées

###  Préparation démonstration

- [ ] Tester `docker pull` et `docker run` AVANT la soutenance
- [ ] Préparer la modification dans `templates/index.html`
- [ ] Vérifier que le pipeline GitHub Actions fonctionne
- [ ] Tester l'accès admin local (identifiants prêts)
- [ ] Vérifier l'URL de production
- [ ] Dashboard Sentry ouvert dans un onglet
- [ ] Documentation Sphinx générée et consultable
- [ ] Docker Hub ouvert dans un onglet
- [ ] Terminal prêt avec commandes Docker

###  Documents à avoir sous la main

- [ ] URL du repository GitHub : https://github.com/steveraffner/oc-lettings-refactored
- [ ] URL du site en production : https://oc-lettings-av9a.onrender.com
- [ ] URL Docker Hub : https://hub.docker.com/r/immeuble11/oc-lettings
- [ ] URL Dashboard Sentry : https://steve-raffner.sentry.io/projects/oc-lettings/
- [ ] URL GitHub Actions : https://github.com/steveraffner/oc-lettings-refactored/actions
- [ ] Identifiants admin Django
- [ ] Commandes Docker à copier-coller

---

## ️ QUESTIONS PROBABLES ET RÉPONSES

### 1️⃣ "Pourquoi avoir choisi [Render/Railway/Heroku] ?"

**Réponse préparée :**
> *"J'ai choisi [Render/Railway/Heroku] pour plusieurs raisons :*
> - **Render** : Support Docker natif, plan gratuit suffisant, déploiement via GitHub, base PostgreSQL incluse
> - **Railway** : CLI puissant, déploiement simple, logs en temps réel, scaling facile
> - **Heroku** : Plateforme mature, nombreux add-ons, documentation extensive, mais payant
>
> *J'ai comparé les 3 et [votre choix] offre le meilleur rapport simplicité/coût/features pour OC Lettings."*

---

### 2️⃣ "Comment gérez-vous les secrets en production ?"

**Réponse préparée :**
> *"Les secrets sont gérés via variables d'environnement :*
> - `SECRET_KEY` : Clé Django générée aléatoirement
> - `SENTRY_DSN` : URL de connexion Sentry
> - `DATABASE_URL` : Connexion PostgreSQL (si applicable)
> - `DOCKER_USERNAME` / `DOCKER_PASSWORD` : Secrets GitHub Actions
>
> *Aucun secret n'est stocké dans le code ou l'image Docker. Tout est injecté au runtime."*

---

### 3️⃣ "Que se passe-t-il si un test échoue dans le pipeline ?"

**Réponse préparée :**
> *"Si un test échoue :*
> 1. Le pipeline s'arrête immédiatement à l'étape de test
> 2. Les étapes suivantes (build, push, deploy) ne s'exécutent pas
> 3. GitHub envoie une notification d'échec
> 4. Le développeur corrige le code et refait un commit
> 5. Le pipeline redémarre automatiquement
>
> *Cela garantit qu'aucun code défectueux n'atteint la production."*

---

### 4️⃣ "Comment faire un rollback en cas de problème ?"

**Réponse préparée :**
> *"Plusieurs stratégies de rollback :*
> 
> **Option 1 - Via Docker Hub :**
> ```bash
> docker pull immeuble11/oc-lettings:[SHA-previous-commit]
> # Redéployer cette version
> ```
>
> **Option 2 - Via Git :**
> ```bash
> git revert [commit-hash]
> git push origin main
> # Le pipeline redéploie automatiquement
> ```
>
> **Option 3 - Via la plateforme :**
> - Render : Rollback depuis le dashboard
> - Redéploiement d'une version précédente en 1 clic
>
> *Toutes les versions sont tagguées et accessibles sur Docker Hub."*

---

### 5️⃣ "Expliquez le processus de migration des données"

**Réponse préparée :**
> *"J'ai créé des migrations personnalisées en 3 phases :*
>
> **Phase 1 - Création des nouveaux modèles :**
> ```bash
> python manage.py makemigrations lettings profiles
> ```
>
> **Phase 2 - Copie des données (migration personnalisée) :**
> ```python
> def copy_data(apps, schema_editor):
>     try:
>         OldProfile = apps.get_model('oc_lettings_site', 'Profile')
>         NewProfile = apps.get_model('profiles', 'Profile')
>         
>         for old_profile in OldProfile.objects.all():
>             NewProfile.objects.create(
>                 id=old_profile.id,
>                 user=old_profile.user,
>                 favorite_city=old_profile.favorite_city
>             )
>     except LookupError:
>         # L'ancienne app n'existe pas (ex: test database)
>         pass
> ```
>
> **Phase 3 - Suppression des anciens modèles :**
> - Après validation, suppression des anciens modèles
> - Migration finale pour nettoyer la base
>
> *Aucune utilisation de SQL direct, tout passe par l'ORM Django pour la sécurité."*

---

### 6️⃣ "Comment amélioreriez-vous ce projet ?"

**Réponse préparée :**
> *"Plusieurs pistes d'amélioration :*
>
> **Court terme :**
> - Tests end-to-end avec Selenium ou Playwright
> - Monitoring de performance avec New Relic ou Datadog
> - Mise en cache avec Redis pour les requêtes fréquentes
>
> **Moyen terme :**
> - CDN (CloudFlare) pour les fichiers statiques
> - Environnement staging pour tester avant prod
> - Backup automatique de la base de données
>
> **Long terme :**
> - Architecture microservices si forte croissance
> - API REST avec Django REST Framework
> - Frontend découplé (React/Vue.js)
> - Kubernetes pour l'orchestration si multi-régions
>
> *Tout dépend de l'évolution du trafic et des besoins business d'OC Lettings."*

---

### 7️⃣ "Pourquoi ne pas avoir utilisé Docker Compose en production ?"

**Réponse préparée :**
> *"Docker Compose est excellent pour le développement local, mais :*
> - Les plateformes cloud gèrent déjà l'orchestration (PostgreSQL, Redis, etc.)
> - Une seule image Docker suffit pour notre application Django
> - Les services externes (DB, cache) sont des add-ons gérés
> - Plus simple à maintenir avec un seul conteneur
>
> *Si l'architecture devenait plus complexe (workers Celery, Nginx, etc.), alors Docker Compose ou Kubernetes serait justifié."*

---

### 8️⃣ "Comment gérez-vous les migrations en production ?"

**Réponse préparée :**
> *"Les migrations sont exécutées automatiquement au déploiement :*
>
> **Dans le Dockerfile :**
> ```dockerfile
> CMD python manage.py migrate && \
>     python manage.py collectstatic --noinput && \
>     gunicorn oc_lettings_site.wsgi
> ```
>
> **Sécurité :**
> - Migrations testées en local d'abord
> - Tests automatiques avant déploiement
> - Backup de la base avant migration sensible
> - Rollback possible via Docker Hub
>
> *Pour une migration critique, je ferais un déploiement manuel avec fenêtre de maintenance."*

---

##  CONSEILS POUR LA PRÉSENTATION

###  À FAIRE

-  Parler clairement et à rythme modéré
-  Regarder l'évaluateur, pas seulement l'écran
-  Utiliser les termes techniques précis
-  Montrer l'URL déployée le plus tôt possible
-  Avoir les onglets pré-ouverts (GitHub, Docker Hub, Sentry, RTD)
-  Expliquer chaque étape en temps réel
-  Rester calme si un bug survient (expliquer le debugging)
-  Montrer de l'enthousiasme pour le projet

###  À ÉVITER

-  Lire mot à mot le téléprompteur
-  Aller trop vite ou trop lentement
-  Paniquer si le pipeline prend du temps
-  Improviser sans préparation
-  Oublier de montrer les modifications déployées
-  Négliger les questions de l'évaluateur
-  Utiliser du jargon sans l'expliquer

---

## ⏱️ TIMING DÉTAILLÉ

| Section | Durée | Total cumulé |
|---------|-------|--------------|
| Introduction | 1 min | 1 min |
| Démo locale | 3 min | 4 min |
| Architecture modulaire | 2 min | 6 min |
| Dette technique | 1,5 min | 7,5 min |
| **Pipeline CI/CD (ESSENTIEL)** | **5 min** | **12,5 min** |
| Sentry | 1,5 min | 14 min |
| Read The Docs | 1 min | 15 min |
| Conclusion | 0,5 min | 15,5 min |

**️ Temps limite : 10-20 minutes (refus si hors limites)**

---

##  CONTACT ET DERNIERS RAPPELS

### Avant la soutenance (48h avant)
- [ ] Tester TOUT le parcours de A à Z
- [ ] Vérifier que tous les services sont UP
- [ ] Préparer une version backup de la démo
- [ ] Relire ce téléprompteur 3 fois

### Le jour J (1h avant)
- [ ] Vérifier la connexion Internet
- [ ] Ouvrir tous les onglets nécessaires
- [ ] Tester le micro et la caméra
- [ ] Avoir une bouteille d'eau à portée
- [ ] Respirer profondément et rester confiant(e) 

---

##  BONNE CHANCE !

*Vous avez travaillé dur sur ce projet. Vous maîtrisez le sujet. Faites confiance à votre préparation et montrez votre expertise avec assurance !*

**N'oubliez pas : Dominique veut voir que vous comprenez ce que vous avez fait, pas que vous récitez parfaitement. Soyez authentique et pédagogue.**

---

**Dernière révision : Janvier 2026**
