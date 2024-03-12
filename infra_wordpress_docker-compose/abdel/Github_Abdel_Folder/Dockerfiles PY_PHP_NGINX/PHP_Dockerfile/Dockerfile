FROM alpine 3.19
LABEL maintainer="Abdellah B."


# Installation des dépendances supplémentaires si nécessaire
RUN apt-get update && apt-get install -y \
    apt-get -y install ca-certificates apt-transport-https software-properties-common; \
    apt-get update &&\
    apt-get install -y nginx &&\
    add-apt-repository -y ppa:ondrej/php && apt-get update &&\
    apt-get install -y php${PHP_VERSION} php${PHP_VERSION}-fpm php${PHP_VERSION}-curl php${PHP_VERSION}-mysql php${PHP_VERSION}-gd\
    php${PHP_VERSION}-mbstring php${PHP_VERSION}-xml php${PHP_VERSION}-imagick php${PHP_VERSION}-zip php${PHP_VERSION}-xmlrpc &&\
    mkdir -p /home/www-data/var/run/php && touch /home/www-data/var/run/php/php${PHP_VERSION}-fpm.sock && chown -R www-data:www-data /home/www-data/var/run/php; \
    apt-get -qq clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Configuration PHP
ADD ./php/${PHP_VERSION}/fpm/php.ini /etc/php/${PHP_VERSION}/fpm/php.ini
ADD ./php/${PHP_VERSION}/fpm/pool.d/www.conf /etc/php/${PHP_VERSION}/fpm/pool.d/www.conf
ADD ./php/${PHP_VERSION}/fpm/php-fpm.conf /etc/php/${PHP_VERSION}/fpm/php-fpm.conf


RUN systemctl enable php${PHP_VERSION}-fpm

# Exposer le port 9000 par défaut utilisé par PHP-FPM
EXPOSE 9000

# Commande par défaut pour démarrer PHP FPM
CMD ["php-fpm"]