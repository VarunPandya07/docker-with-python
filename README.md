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
