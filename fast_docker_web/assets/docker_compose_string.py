def getDockerComposeString():
    return '''version: "3"

services:
webserver:
    build: 
    context: ./bin/php74
    container_name: 'docker-apache-php'
    restart: 'always'
    ports:
    - "80:80"
    - "443:443"
    volumes: 
    - ${DOCUMENT_ROOT-./www}:/var/www/html
    - ${PHP_INI-./config/php/php.ini}:/usr/local/etc/php/php.ini
    - ${VHOSTS_DIR-./config/vhosts}:/etc/apache2/sites-enabled
    - ${LOG_DIR-./logs/apache2}:/var/log/apache2'''
