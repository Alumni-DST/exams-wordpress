FROM alpine:3.19
LABEL maintainer="Abdellah B."

# Installation de NGINX et des dépendances nécessaires
RUN apk update && \
    apk add --no-cache nginx && \
    rm -rf /var/cache/apk/*

# Configuration de l'application Nginx (si nécessaire)
# ADD ./nginx/conf.d/wordpress.conf /etc/nginx/conf.d/wordpress.conf

# Création de l'utilisateur www-data et répertoire pour NGINX
RUN adduser -D -u 33 www-data && \
    mkdir -p /var/www/html && \
    chown -R www-data:www-data /var/www/html


# Exposer les ports
EXPOSE 80
EXPOSE 443


# Commande par défaut pour démarrer NGINX
CMD ["nginx", "-g", "daemon off;"]

# RUN systemctl enable nginx.service
