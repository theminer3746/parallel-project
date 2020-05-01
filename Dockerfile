FROM php:7.4-fpm

RUN apt-get update \
  && apt-get install -y \
   cron \
   libfreetype6-dev \
   libicu-dev \
   libonig-dev \
   libjpeg62-turbo-dev \
   libmcrypt-dev \
   libxslt1-dev \
   libzip-dev \
   openssh-server \
   openssh-client \
   rsync \
   zlib1g-dev \
   zip unzip

#RUN docker-php-ext-configure \


RUN docker-php-ext-install \
  bcmath \
  gd \
  intl \
  mbstring \
  pdo_mysql \
  soap \
  xsl \
  xml \
  zip \
  && pecl install mcrypt mongodb \
  && docker-php-ext-enable mcrypt mongodb

RUN curl -sS https://getcomposer.org/installer | \
  php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /usr/src/laravel

COPY laravel/composer.* /usr/src/laravel/

RUN composer install --no-autoloader

COPY laravel/.env.docker laravel/.env

COPY laravel/ /usr/src/laravel/

RUN composer dump-autoload

RUN php artisan key:generate && \
    php artisan jwt:secret

RUN ls
