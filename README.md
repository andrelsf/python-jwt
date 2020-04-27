# Flask-JWT

Learning about JWT with Python3.6.

## Entities

Entity `Users`
```json
{
  "name": "String",
  "email": "string",
  "password": "String",
  "active": "Boolean",
  "createAt": "DateTime",
  "UpdatedAt": "DateTime"
}
```

## Endpoints

| Endpoints     |  Method  | Status Codes| Response | Query String | DONE
|:--------------|:--------:|:-----------:|:---------|:-------------|:----------:
| /users        | `GET` | `200` | List of users! Default 10 users | /users?limit=20 | `OK` |
| /users/:id    | `GET` | `200`   | Get user by ID  | /users?isactive return if user is active or no | `OK` |
| /users/:id    | `PUT` | `200`   | Update user by ID | | `OK` |
| /auth/login   | `POST` | `200`   | Create AccessToken by email and password || `OK` |
| /auth/logout  | `POST` | `200`   | Refoke AccessToken || `OK` |
| /auth/registry| `POST` | `201`   | Create new account by default active=False || `OK` |
| /auth/verify  | `POST` | `200`   | Verify if access token is valid|| `OK` |

## References

### Install Python3.6
* [Tecmint](https://www.tecmint.com/install-python-in-ubuntu/)

### Python, SQLAlchemy and Flask
* [Flask Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [JWT Authorization in Flask](https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb)
* [SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [UUID](https://websauna.org/docs/narrative/modelling/models.html)
* [Flask JWT Extended Docs](https://flask-jwt-extended.readthedocs.io/en/stable/changing_default_behavior/)
* [Flask Handler Errors](https://flask.palletsprojects.com/en/1.1.x/errorhandling/#application-errors)
* [Request Parsing](https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html?highlight=reqparse#full-parameter-parsing-example)
* [Req Parsing Handler Erros](https://flask-restful.readthedocs.io/en/latest/reqparse.html?highlight=reqparse#parser-inheritance)
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Iana HTTP Status Codes](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
* [Python if condition](http://excript.com/python/atribuicao-condicional-python.html)
* [Flask-CORS docs](https://flask-cors.corydolphin.com/en/3.0.7/)
* [Flask JWT Custom Decorators](https://flask-jwt-extended.readthedocs.io/en/stable/custom_decorators/)
