# Apache LetsEncrypt

[source](https://linuxize.com/post/secure-apache-with-let-s-encrypt-on-ubuntu-18-04/)

Make the certificate directory specifically for Apache

    mkdir -p /etc/apache2/certs

Generate secure OpenSSL parameters (that can take a while)

    openssl dhparam -out /etc/apache2/certs/dhparam.pem 2048


Make the challenge directory

    mkdir -p /var/lib/letsencrypt/.well-known
    chgrp www-data /var/lib/letsencrypt
    chmod g+s /var/lib/letsencrypt


Apache configuration file `/conf-available/letsencrypt.conf`

    Alias /.well-known/acme-challenge/ "/var/lib/letsencrypt/.well-known/acme-challenge/"
    <Directory "/var/lib/letsencrypt/">
        AllowOverride None
        Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
        Require method GET POST OPTIONS
    </Directory>


Apache configuration file `/conf-available/ssl-params.conf`

    SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
    SSLProtocol All -SSLv2 -SSLv3 -TLSv1 -TLSv1.1
    SSLHonorCipherOrder On
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
    Header always set X-Frame-Options DENY
    Header always set X-Content-Type-Options nosniff
    # Requires Apache >= 2.4
    SSLCompression off
    SSLUseStapling on
    SSLStaplingCache "shmcb:logs/stapling-cache(150000)"
    # Requires Apache >= 2.4.11
    SSLSessionTickets Off
    SSLOpenSSLConfCmd DHParameters "/etc/apache2/certs/dhparam.pem"

Enable some modifications

    a2enmod ssl
    a2enmod headers

Enable the above configuration files

    a2enconf letsencrypt
    a2enconf ssl-params

(disable them with)

    a2disconf letsencrypt
    a2disconf ssl-params

Enable some more modifications

    a2enmod http2

Restart Apache2 (Ubuntu 18)

    systemctl reload apache2

Template certbot command

    certbot certonly --agree-tos --email admin@example.com --webroot -w /var/lib/letsencrypt/ -d example.com -d www.example.com

Specific certbot command    

    certbot certonly --agree-tos --email noreply@virtcard.co --webroot -w /var/lib/letsencrypt/ -d notes.virtcard.co
