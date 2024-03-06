

FROM ubuntu:latest
MAINTAINER marcus DST <marcus@gmail.com>

# Définir le fuseau horaire sans interaction
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Mise à jour des packages
RUN apt-get update && apt-get upgrade -y

RUN apt-get install tree certbot python3-certbot-nginx rsync openssh-server unzip  passwd sudo nano vim curl -y  
RUN apt-get install mariadb-server mariadb-client python3 python3-pip -y 
RUN apt-get -qq clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

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
        
# Copiez vos scripts dans le conteneur
COPY ./*.sh /infra2_exam2/apps/exploit/
RUN chmod +x /infra2_exam2/apps/exploit/

# ENTRYPOINT définit la commande principale du conteneur
#ENTRYPOINT ["/bin/bash", "-c", "/infra2_exam2/apps/exploit/start_DB.sh"]



CMD ["/usr/sbin/init"]
#CMD ["/bin/sh", "-c", "/infra1_exam/apps/exploit/init_infra1_scripts.sh"]



