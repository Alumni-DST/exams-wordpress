#!/bin/bash

#docker-compose stop

#echo " " > /home/ubuntu/docker_exam/api_test.log

docker ps

docker-compose up 

docker ps

tail -100 /home/ubuntu/docker_exam/api_test.log
