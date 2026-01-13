# Guide de déploiement Render

Ce guide vous explique comment déployer l'application OC Lettings sur Render avec la création automatique d'un compte administrateur.

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

## Dépannage

### Le superutilisateur n'existe pas
- Vérifiez que les variables d'environnement sont configurées
- Relancez un déploiement
- Consultez les logs de build sur Render

### Erreur de connexion
- Vérifiez les variables `DJANGO_SUPERUSER_*`
- Assurez-vous que le script de build s'est exécuté sans erreur

### Base de données vide
- Les migrations sont automatiquement appliquées
- Les données d'exemple sont créées automatiquement
- En cas de problème, redéployez l'application