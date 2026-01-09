# 🎤 Téléprompteur de Soutenance - OC Lettings

**Durée : 15 minutes (±5 minutes)**  
**Date de soutenance : _________**

---

## 📋 INTRODUCTION (1 minute)

> *"Bonjour Dominique, je vais vous présenter les améliorations apportées au site OC Lettings. J'ai travaillé sur 5 axes majeurs conformément à vos demandes :*
> 
> 1. *La refactorisation en architecture modulaire*
> 2. *La réduction de la dette technique*
> 3. *La mise en place d'un pipeline CI/CD avec Docker*
> 4. *L'intégration du monitoring avec Sentry*
> 5. *La documentation technique sur Read The Docs*
>
> *Je vais maintenant vous faire une démonstration complète du site et du processus de déploiement."*

---

## 💻 PARTIE 1 : DÉMONSTRATION LOCALE (3 minutes)

### 🔧 Lancement du site en local

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Lancer le serveur de développement
python manage.py runserver
```

**💬 À dire :**
> *"Voici le site fonctionnel sur http://localhost:8000. Lors de la mise en place de l'environnement de développement, j'ai rencontré quelques défis :*
> 
> - **[Mentionner vos problèmes réels]** : 
>   - *Problèmes de migrations de données*
>   - *Configuration de la base de données SQLite*
>   - *Gestion des dépendances Python*
>   - *Configuration des fichiers statiques*
> 
> *Je les ai résolus en [expliquer brièvement vos solutions]."*

### 🌐 Parcourir le site

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
   - Se connecter avec les identifiants admin
   - *"Notez la pluralisation correcte des modèles"*
   - Montrer : Lettings, Addresses, Profiles

---

## 🏗️ PARTIE 2 : ARCHITECTURE MODULAIRE (2 minutes)

**💬 À dire :**
> *"J'ai restructuré l'application monolithique initiale en 3 applications Django distinctes pour améliorer la maintenabilité et la scalabilité :*

### 📦 Structure des applications

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

**💬 Continuer :**
> *"Les migrations personnalisées ont permis de copier les données des anciens modèles vers les nouveaux sans perte :*
> 
> - *Utilisation de `apps.get_model()` pour accéder aux modèles*
> - *Fonction `RunPython` pour copier les données*
> - *Suppression des anciens modèles après vérification*
> - *Aucune utilisation de SQL direct (RunSQL)*
>
> *Cette approche garantit une migration sûre et traçable."*

---

## 🧹 PARTIE 3 : RÉDUCTION DE LA DETTE TECHNIQUE (1,5 minute)

**💬 À dire :**
> *"J'ai travaillé sur 5 points pour réduire la dette technique :*

### ✅ 1. Linting avec Flake8

```bash
flake8
```

> *"Aucune erreur de linting détectée. Le code respecte les conventions PEP 8."*

### ✅ 2. Docstrings

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

### ✅ 3. Tests et couverture >80%

```bash
pytest --cov=. --cov-report=term-missing
```

> *"Couverture de test supérieure à 80% avec pytest-django et pytest-cov. Les tests couvrent :*
> - *Les modèles (création, validation)*
> - *Les vues (GET requests, contexte)*
> - *Les URLs (résolution des routes)*
> - *L'intégration admin"*

### ✅ 4. Pluralisation correcte dans l'admin

> *"Configuration de `verbose_name_plural` dans les modèles pour corriger :*
> - *'Profiles' → 'Profiles' (correct)*
> - *'Addresss' → 'Addresses' (corrigé)"*

### ✅ 5. Pages d'erreur personnalisées

> *"Création de templates personnalisés :*
> - *`404.html` : Page non trouvée*
> - *`500.html` : Erreur serveur*
>
> *Ces pages offrent une meilleure expérience utilisateur."*

---

## 🚀 PARTIE 4 : PIPELINE CI/CD ET DÉPLOIEMENT (5 minutes) ⭐

### 📋 Architecture du pipeline

**💬 À dire :**
> *"Le pipeline CI/CD est configuré avec GitHub Actions et comprend 4 étapes automatisées :*

```yaml
Pipeline CI/CD :
1️⃣ Tests & Linting (pytest + flake8)
2️⃣ Build Docker (si tests OK)
3️⃣ Push Docker Hub (si branche main)
4️⃣ Déploiement automatique (si branche main)
```

**Montrer le fichier `.github/workflows/ci-cd.yml`**

---

### 🎬 DÉMONSTRATION EN DIRECT : Modification et Redéploiement

#### **Étape 1 : Modifier le titre de la page d'accueil** ⏱️ 30 sec

```bash
# Ouvrir le fichier
code templates/index.html
```

**Modification à faire :**
```html
<!-- AVANT -->
<title>Holiday Homes</title>

<!-- APRÈS -->
<title>OC Lettings - Welcome 2026</title>
```

**💬 À dire :**
> *"Je modifie maintenant le titre de la page d'accueil comme vous l'avez demandé."*

---

#### **Étape 2 : Commit et Push** ⏱️ 30 sec

```bash
git add templates/index.html
git commit -m "feat: Update homepage title for presentation demo"
git push origin main
```

**💬 À dire :**
> *"Je pousse les modifications sur la branche main, ce qui va automatiquement déclencher le pipeline CI/CD."*

---

#### **Étape 3 : Montrer le pipeline GitHub Actions** ⏱️ 2 min

**Aller sur GitHub :**
1. Ouvrir l'onglet **Actions**
2. Cliquer sur le workflow en cours d'exécution
3. Expliquer chaque étape en temps réel

**💬 À dire pendant que le pipeline tourne :**

> *"Vous pouvez voir le pipeline se dérouler :*
> 
> - **✅ Setup** : Installation de Python et des dépendances
> - **✅ Linting** : Vérification flake8 en cours...
> - **✅ Tests** : Exécution de la suite de tests avec pytest...
> - **⏳ Build Docker** : Construction de l'image Docker...
> - **⏳ Push Docker Hub** : Envoi de l'image vers Docker Hub...
> - **⏳ Deploy** : Déploiement sur [Render/Railway/Heroku]...
>
> *Si une étape échoue, le pipeline s'arrête immédiatement et aucun déploiement n'est effectué."*

---

#### **Étape 4 : Vérifier Docker Hub** ⏱️ 30 sec

**Ouvrir Docker Hub dans le navigateur :**
```
https://hub.docker.com/r/[votre-username]/oc-lettings
```

**💬 À dire :**
> *"Pendant que le déploiement se termine, regardons Docker Hub :*
> - *Voici le repository avec l'image Docker*
> - *Système de tags : `latest` et `[SHA-commit]`*
> - *L'image fait environ [XXX MB]*
> - *Elle contient l'application Django, les dépendances et les fichiers statiques"*

---

#### **Étape 5 : Vérifier le site déployé** ⏱️ 1 min

**Ouvrir l'URL de production :**
```
https://[votre-app].onrender.com
# ou
https://[votre-app].herokuapp.com
```

**💬 À dire :**
> *"Le déploiement est maintenant terminé. Vous pouvez constater que :*
> - ✅ *Le nouveau titre apparaît bien : 'OC Lettings - Welcome 2026'*
> - ✅ *Le site est entièrement fonctionnel en production*
> - ✅ *Les fichiers statiques se chargent correctement*
> - ✅ *La base de données PostgreSQL est opérationnelle"*

**Naviguer rapidement dans le site :**
- Page d'accueil
- Lettings
- Profiles

---

#### **Étape 6 : Pull et Run Docker en local** ⏱️ 1 min

```bash
# Pull de l'image depuis Docker Hub
docker pull [votre-username]/oc-lettings:latest

# Lancement du conteneur
docker run -p 8000:8000 \
  -e SECRET_KEY="demo-secret-key-for-presentation" \
  -e DEBUG=False \
  -e ALLOWED_HOSTS="localhost,127.0.0.1" \
  [votre-username]/oc-lettings:latest
```

**💬 À dire :**
> *"L'image Docker fonctionne parfaitement en local avec exactement la même configuration qu'en production :*
> - *Port 8000 exposé*
> - *Variables d'environnement injectées*
> - *Application prête en quelques secondes*
>
> *Cela garantit la portabilité et la reproductibilité des déploiements."*

**Ouvrir `http://localhost:8000` pour vérifier**

---

## 🔍 PARTIE 5 : MONITORING AVEC SENTRY (1,5 minute)

**💬 À dire :**
> *"J'ai intégré Sentry pour la surveillance en temps réel des erreurs en production :*

### Configuration

```python
# Dans settings.py
import sentry_sdk

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
```

**💬 Continuer :**
> *"Les points clés de l'intégration Sentry :*
> - *DSN stocké en variable d'environnement (sécurisé)*
> - *Capture automatique des exceptions non gérées*
> - *Logging configuré aux points critiques*
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

**💬 À dire :**
> *"Sentry nous permet de détecter et résoudre rapidement les bugs en production avant qu'ils n'affectent trop d'utilisateurs."*

---

## 📚 PARTIE 6 : DOCUMENTATION READ THE DOCS (1 minute)

**Ouvrir la documentation :**
```
https://[votre-projet].readthedocs.io
```

**💬 À dire :**
> *"La documentation technique est hébergée sur Read The Docs et comprend :*

### 📖 Structure de la documentation

1. **Installation** : Guide de mise en place locale
2. **Architecture** : Explication des 3 applications
3. **Déploiement** : Procédure CI/CD et Docker
4. **API/Modèles** : Documentation auto-générée depuis les docstrings
5. **Tests** : Guide pour lancer les tests
6. **Contribution** : Bonnes pratiques pour l'équipe

**💬 Continuer :**
> *"Points importants :*
> - *Création avec Sphinx et reStructuredText*
> - *Génération automatique depuis les docstrings Python*
> - *Mise à jour automatique à chaque push via webhook GitHub*
> - *Versioning de la documentation (main, branches)*
> - *Recherche full-text intégrée"*

---

## 🎯 CONCLUSION (30 secondes)

**💬 À dire :**
> *"Pour résumer, l'application OC Lettings est maintenant :*
> 
> - ✅ **Modulaire** : Architecture en 3 applications indépendantes et maintenables
> - ✅ **Propre** : Dette technique réduite, code documenté, tests >80%
> - ✅ **Automatisée** : Pipeline CI/CD avec tests automatiques et déploiement continu
> - ✅ **Conteneurisée** : Image Docker portable et reproductible
> - ✅ **Surveillée** : Monitoring Sentry pour détecter les erreurs rapidement
> - ✅ **Documentée** : Documentation complète sur Read The Docs
>
> *L'application est prête pour la production et peut facilement être mise à l'échelle pour l'expansion aux États-Unis. Le processus de déploiement est entièrement automatisé et sécurisé."*

---

## 📌 CHECKLIST AVANT SOUTENANCE

### ✅ Préparation technique

- [ ] Repository GitHub public accessible
- [ ] Site fonctionne en local (`python manage.py runserver`)
- [ ] Tests passent avec `pytest --cov` (>80%)
- [ ] Flake8 ne retourne aucune erreur
- [ ] Pipeline CI/CD configuré sur GitHub Actions
- [ ] Compte Docker Hub avec images disponibles
- [ ] Site déployé avec URL publique fonctionnelle
- [ ] Sentry configuré avec projet actif
- [ ] Read The Docs publié et accessible
- [ ] Toutes les variables d'environnement configurées

### ✅ Préparation démonstration

- [ ] Tester `docker pull` et `docker run` AVANT la soutenance
- [ ] Préparer la modification dans `templates/index.html`
- [ ] Vérifier que le pipeline GitHub Actions fonctionne
- [ ] Tester l'accès admin local (identifiants prêts)
- [ ] Vérifier l'URL de production
- [ ] Dashboard Sentry ouvert dans un onglet
- [ ] Read The Docs ouvert dans un onglet
- [ ] Docker Hub ouvert dans un onglet
- [ ] Terminal prêt avec commandes Docker

### ✅ Documents à avoir sous la main

- [ ] URL du repository GitHub
- [ ] URL du site en production
- [ ] URL Docker Hub
- [ ] URL Read The Docs
- [ ] URL Dashboard Sentry
- [ ] Identifiants admin Django
- [ ] Commandes Docker à copier-coller

---

## ⚠️ QUESTIONS PROBABLES ET RÉPONSES

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
> docker pull [username]/oc-lettings:[SHA-previous-commit]
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
> - Render/Railway : Rollback depuis le dashboard
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
>     OldProfile = apps.get_model('oc_lettings_site', 'Profile')
>     NewProfile = apps.get_model('profiles', 'Profile')
>     
>     for old_profile in OldProfile.objects.all():
>         NewProfile.objects.create(
>             user=old_profile.user,
>             favorite_city=old_profile.favorite_city
>         )
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

## 🎬 CONSEILS POUR LA PRÉSENTATION

### ✅ À FAIRE

- ✅ Parler clairement et à rythme modéré
- ✅ Regarder l'évaluateur, pas seulement l'écran
- ✅ Utiliser les termes techniques précis
- ✅ Montrer l'URL déployée le plus tôt possible
- ✅ Avoir les onglets pré-ouverts (GitHub, Docker Hub, Sentry, RTD)
- ✅ Expliquer chaque étape en temps réel
- ✅ Rester calme si un bug survient (expliquer le debugging)
- ✅ Montrer de l'enthousiasme pour le projet

### ❌ À ÉVITER

- ❌ Lire mot à mot le téléprompteur
- ❌ Aller trop vite ou trop lentement
- ❌ Paniquer si le pipeline prend du temps
- ❌ Improviser sans préparation
- ❌ Oublier de montrer les modifications déployées
- ❌ Négliger les questions de l'évaluateur
- ❌ Utiliser du jargon sans l'expliquer

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

**⚠️ Temps limite : 10-20 minutes (refus si hors limites)**

---

## 📞 CONTACT ET DERNIERS RAPPELS

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
- [ ] Respirer profondément et rester confiant(e) 💪

---

## 🚀 BONNE CHANCE !

*Vous avez travaillé dur sur ce projet. Vous maîtrisez le sujet. Faites confiance à votre préparation et montrez votre expertise avec assurance !*

**N'oubliez pas : Dominique veut voir que vous comprenez ce que vous avez fait, pas que vous récitez parfaitement. Soyez authentique et pédagogue.**

---

**Dernière révision : Janvier 2026**
