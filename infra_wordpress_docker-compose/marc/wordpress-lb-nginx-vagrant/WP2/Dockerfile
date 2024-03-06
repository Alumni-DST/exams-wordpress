

FROM ubuntu:latest
MAINTAINER marcus DST <marcus@gmail.com>

# Définir le fuseau horaire sans interaction
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Ajouter le référentiel Ondřej Surý pour PHP
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:ondrej/php -y

# Mise à jour des packages
RUN apt-get update && apt-get upgrade -y

RUN apt-get install tree certbot python3-certbot-nginx rsync openssh-server unzip apache2 passwd sudo nano vim curl -y  
RUN apt-get install  mariadb-client python3 python3-pip -y 
RUN apt-get install php8.0 php8.0-fpm php8.0-curl php8.0-mysql php8.0-gd php8.0-mbstring php8.0-xml php8.0-imagick php8.0-zip php8.0-xmlrpc -y 
RUN apt-get -qq clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configuration de PHP
RUN a2enmod rewrite
RUN service apache2 restart

# Téléchargement et installation de WordPress
WORKDIR /var/www/html
#RUN rm -rf *
ADD https://wordpress.org/latest.tar.gz /var/www/html/

RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 755 /var/www/html


# Exposer le port par défaut d'Apache
EXPOSE 80



RUN cd /lib/systemd/system/sysinit.target.wants/ \
    && for i in *; do \
           [ "$i" = "systemd-tmpfiles-setup.service" ] || rm -f "$i"; \
       done

RUN rm -f /lib/systemd/system/multi-user.target.wants/*
RUN rm -f /etc/systemd/system/*.wants/*
RUN rm -f /lib/systemd/system/local-fs.target.wants/*
RUN rm -f /lib/systemd/system/sockets.target.wants/*udev*
RUN rm -f /lib/systemd/system/sockets.target.wants/*initctl*
RUN rm -f /lib/systemd/system/basic.target.wants/*
RUN rm -f /lib/systemd/system/anaconda.target.wants/*

RUN systemctl enable ssh.service;

RUN useradd --create-home -s /bin/bash vagrant
RUN echo -n 'vagrant:vagrant' | chpasswd
RUN echo 'vagrant ALL = NOPASSWD: ALL' > /etc/sudoers.d/vagrant
RUN chmod 440 /etc/sudoers.d/vagrant

RUN mkdir -p /home/vagrant/.ssh; \
    chmod 700 /home/vagrant/.ssh
ADD https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub /home/vagrant/.ssh/authorized_keys
RUN chmod 600 /home/vagrant/.ssh/authorized_keys; \
    chown -R vagrant:vagrant /home/vagrant/.ssh

RUN chown -R vagrant:vagrant /home/vagrant/.ssh
RUN sed -i -e 's/Defaults.*requiretty/#&/' /etc/sudoers
RUN sed -i -e 's/\(UsePAM \)yes/\1 no/' /etc/ssh/sshd_config

RUN mkdir /var/run/sshd

RUN apt-get -y install openssh-client

VOLUME [ "/sys/fs/cgroup" ]
VOLUME [ "/infra2_exam2/logs" ]
VOLUME [ "/infra2_exam2/backup" ]
VOLUME [ "/infra2_exam2/apps" ]

#avec VOLUMES
RUN mkdir -p /infra2_exam2/apps
RUN mkdir -p /infra2_exam2/logs
RUN mkdir -p /infra2_exam2/backup
        
#RUN chmod -R 755 /infra1_exam1
#COPY exploit /infra1_exam1/apps/

#Mise en place des liens
#RUN ln -s /var/log/nginx /infra1_exam1/logs
#RUN ln -s /etc/nginx/conf.d/wordpress.conf /infra1_exam1/backup/wordpress.conf



CMD ["/usr/sbin/init"]
#CMD ["/bin/sh", "-c", "/infra1_exam/apps/exploit/init_infra1_scripts.sh"]



