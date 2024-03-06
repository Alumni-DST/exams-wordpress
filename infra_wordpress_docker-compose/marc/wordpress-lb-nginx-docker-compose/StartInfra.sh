echo "---- Step 1 : Set the environment variables and pull the images ---"
source .env
docker-compose pull


echo " --- Step 2 : Bring up the Database and allow it a moment to create the WordPress user and database tables ---"
docker-compose up -d database


echo "--- You will know it's ready when you see something like this in the docker logs ---"
docker-compose logs database


echo " --- Step 3 : Bring up the WordPress and Nginx containers ---"
docker-compose up -d wordpress1 wordpress2 lb adminer
docker ps -a



echo " --- Step 4 : Verify Wordpress via CURL --- "
echo " curl -k https://127.0.0.1:8443/wp-admin/install.php "
curl -k https://127.0.0.1:8443/wp-admin/install.php

