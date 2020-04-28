FROM    php:7.2-apache

ENV     APP_DIR=/usr/src/app/
ENV     APP_DIR_DATA=/usr/src/app/data/
ENV     APP_DIR_LOGS=/usr/src/app/logs/

RUN     apt update | true \
        && apt install -y libzip-dev unzip wget curl libpq5 libghc-postgresql-libpq-dev \
        && docker-php-ext-install pdo pdo_mysql pgsql pdo_pgsql \
        && a2enmod rewrite \
        && service apache2 restart \
        && mkdir -p ${APP_DIR} \
        && mkdir -p ${APP_DIR_DATA} \
        && mkdir -p ${APP_DIR_LOGS} \
        && chown www-data. ${APP_DIR_DATA} -R \
        && chown www-data. ${APP_DIR_LOGS} -R

ADD     ./app.default.conf /etc/apache2/sites-enabled/000-default.conf

WORKDIR /usr/src/app/

#       Add script composer install
ADD     ./composer-install.sh /tmp/composer-install.sh

RUN     bash /tmp/composer-install.sh

EXPOSE  80