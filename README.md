### MYSQL

Download mysql images from DockerHub 

```
docker pull mysql
```

then run mysql image so data base is ready to use 

```
docker run -d --env MYSQL_ROOT_PASSWORD="password" --env MYSQL_DATABASE="database_name" --name <set_cotnainer_name> <image_name/image_ID>
```
### PYTHON

then run python dockerfile so first build then images and then run images

build python dockerfile

```
docker build .
```

run python image

```
docker run -it -rm <image_name/image_ID>
```

### DOCKER COMPOSE 

if use docker compose then create first yml/yaml file yml file is for run multiple container using single command

```
docker compose up
```

but run this command to where the dockerfile 


after this this code is interactive code so go the python container 

```
docker exec -it mypyapp sh
```
then run the command in side the container 

```
python sql_demo.py
```

