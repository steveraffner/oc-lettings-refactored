# Guide de déploiement Render

Ce guide vous explique comment déployer l'application OC Lettings sur Render avec la création automatique d'un compte administrateur.

## ⚡ Solution rapide

Si le superutilisateur n'est pas créé automatiquement, exécutez ce script via la **Console Render** :

```bash
./manual-deploy.sh
```

Ce script va :
1. Appliquer les migrations
2. Créer le superutilisateur admin/Abc1234!
3. Ajouter les données d'exemple

## 📋 Configuration Render (Dashboard)

### 1. Build Command
```bash
./build.sh
```

### 2. Start Command  
```bash
python -m gunicorn oc_lettings_site.wsgi:application
```

### 3. Variables d'environnement
Sur le dashboard Render, ajoutez :

```bash
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@oc-lettings.com  
DJANGO_SUPERUSER_PASSWORD=Abc1234!
SECRET_KEY=<généré automatiquement>
DEBUG=false
DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
```

## 🔧 Dépannage

### Le build ne fonctionne pas
1. Vérifiez que **Build Command** = `./build.sh`
2. Consultez les logs de build sur Render
3. Exécutez manuellement : `./manual-deploy.sh`

### Impossible de se connecter
- URL : https://oc-lettings-av9a.onrender.com/admin/
- Login : `admin`  
- Password : `Abc1234!`

### Reset complet
```bash
python manage.py reset_superuser
```

## Configuration automatique avec render.yaml

Le fichier `render.yaml` configure automatiquement votre service Render avec :
- Variables d'environnement prédéfinies
- Script de build automatique
- Création du superutilisateur

## Variables d'environnement

### Variables obligatoires
- `DJANGO_SUPERUSER_USERNAME` : Nom d'utilisateur admin (défaut: admin)
- `DJANGO_SUPERUSER_EMAIL` : Email admin (défaut: admin@oc-lettings.com)  
- `DJANGO_SUPERUSER_PASSWORD` : Mot de passe admin (défaut: Abc1234!)
- `SECRET_KEY` : Clé secrète Django (générer automatiquement)
- `DEBUG` : Mode debug (défaut: false)

### Variables optionnelles
- `SENTRY_DSN` : URL Sentry pour le monitoring
- `ALLOWED_HOSTS` : Hosts autorisés (défaut: .onrender.com)

## Processus de déploiement

1. **Build automatique** (`build.sh`) :
   - Installation des dépendances
   - Collection des fichiers statiques
   - Migrations de la base de données
   - Création du superutilisateur
   - Création des données d'exemple

2. **Démarrage** :
   - Lancement via Gunicorn
   - Application accessible sur votre domaine Render

## Connexion administrateur

Une fois déployé, vous pouvez vous connecter à l'interface d'administration :
- URL : `https://votre-app.onrender.com/admin/`
- Login : `admin` (ou votre `DJANGO_SUPERUSER_USERNAME`)
- Mot de passe : `Abc1234!` (ou votre `DJANGO_SUPERUSER_PASSWORD`)

## Commandes disponibles

### Création manuelle du superutilisateur
```bash
python manage.py create_superuser
```

### Création des données d'exemple
```bash
python manage.py create_sample_data
```

### Reset complet des utilisateurs
```bash
python manage.py reset_superuser
```

## Scripts de diagnostic

### Vérifier les utilisateurs
```bash
./debug-users.sh
```

### Déploiement manuel complet
```bash
./manual-deploy.sh
```

## Dépannage

### Le superutilisateur n'existe pas
- Vérifiez que les variables d'environnement sont configurées
- Relancez un déploiement
- Consultez les logs de build sur Render
- Exécutez `./manual-deploy.sh` via la console Render

### Erreur de connexion
- Vérifiez les variables `DJANGO_SUPERUSER_*`
- Assurez-vous que le script de build s'est exécuté sans erreur

### Base de données vide
- Les migrations sont automatiquement appliquées
- Les données d'exemple sont créées automatiquement
- En cas de problème, redéployez l'application