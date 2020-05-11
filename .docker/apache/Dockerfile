FROM    php:7.2-apache

ENV     APP_DIR=/usr/src/app/

#       Install packages for APP Running
RUN     apt update | true \
        && apt install -y libzip-dev unzip wget curl libpq5 libghc-postgresql-libpq-dev \
        && docker-php-ext-install pdo pdo_mysql pgsql pdo_pgsql \
        && a2enmod rewrite \
        && a2enmod remoteip \
        && service apache2 restart \
        && mkdir -p ${APP_DIR}

#       Set timezone
RUN     apt-get update && apt-get install tzdata locales -y \
        && sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && locale-gen \
        && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

ADD     ./app.default.conf /etc/apache2/sites-enabled/000-default.conf
ADD     ./modules/charset.conf /etc/apache2/conf-enabled/charset.conf
ADD     ./modules/remoteip.conf /etc/apache2/conf-enabled/remoteip.confS

#       Add script composer install
ADD     ./composer-install.sh /tmp/composer-install.sh

RUN     bash /tmp/composer-install.sh

#       Add group, add user web and set permissions
RUN     getent group 1000 || groupadd web -g 1000 \
        && getent password 1000 || adduser --uid 1000 --gid 1000 --disabled-password --gecos "" web \
        && usermod -aG web www-data

ENV     APACHE_RUN_USER=web
ENV     APACHE_RUN_GROUP=web

WORKDIR /usr/src/app/

EXPOSE  80 443