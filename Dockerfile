# Multi-stage build pour optimiser la taille de l'image
FROM python:3.13-slim as builder

# Variables d'environnement pour Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier et installer les dépendances Python
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage final
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/root/.local/bin:$PATH

WORKDIR /app

# Copier les dépendances Python du builder
COPY --from=builder /root/.local /root/.local

# Créer un utilisateur non-root
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Copier le code de l'application
COPY --chown=appuser:appuser . .

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Passer à l'utilisateur non-root
USER appuser

# Exposer le port
EXPOSE 8000

# Commande de démarrage avec gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "oc_lettings_site.wsgi:application"]
