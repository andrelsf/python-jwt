# API PHP Slim and Doctrine

Struturing API with PHP Slim and Doctrine for Project.

## API

### Config

Add file in api folder
```
driver=pdo_mysql
host=10.62.0.3
port=3306
dbname=project
user=project
password=project
charset=utf-8
```

MySQL ENV
```
MYSQL_ROOT_PASSWORD=R00t
MYSQL_DATABASE=project
MYSQL_USER=project
MYSQL_PASSWORD=project
```

## Docker Compose

Build and UP:
```
docker-compose build --no-cache
docker-compose up -d
```

## PHP
Install Composer:
```
docker exec -it project_backend_1 composer install
```

Doctrine:
```
php vendor/bin/doctrine orm:info
php vendor/bin/doctrine orm:schema-tool:create
php vendor/bin/doctrine orm:schema-tool:drop --force
php vendor/bin/doctrine orm:schema-tool:create
```

## Endpoints

| Endpoint                 | Method   | Code Status       | Response                  | Deploy |  
|:-------------------------|:--------:|:-----------------:|---------------------------|:------:|
| __/api/ping__            | `GET`    | __200__/__500__   | Pong                      | `OK`   |


### Login
```
curl -X POST -H "Content-Type: application/json" -H "Accept: application/json" -d "{'email':'your_email','password':'your_passowrd'}" localhost:5000/auth/login
```

```
curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" -H "Authorization: Bearer ACCESS_TOKEN_JWT" localhost/api/ping
```

## Referencias

* [PHP Slim Requests](http://www.slimframework.com/docs/v3/objects/request.html)
* [PHP Slim EntityManager](http://www.slimframework.com/docs/v3/cookbook/database-doctrine.html)
* [PHP Slim Docs](http://www.slimframework.com/docs/v3/tutorial/first-app.html)
* [Doctrine DateTime](https://www.doctrine-project.org/projects/doctrine-orm/en/2.6/cookbook/working-with-datetime.html#working-with-datetime-instances)
* [Doctrine Basic Mapping](https://www.doctrine-project.org/projects/doctrine-orm/en/2.6/reference/basic-mapping.html)