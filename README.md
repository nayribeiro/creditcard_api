# Solução do Problema

Foi utilizado o tutorial modificado do Eduardo Mendes

https://www.youtube.com/watch?v=WzaKIRJBGXo

## Ferramentas

* Flask
* Marshmallow
* SQLAlchemy
* Flask Migrate
* Flask SQLAlchemy


## Como rodar esse projeto

```sh
set FLASK_APP=app
set FLASK_ENV=Development
set FLASK_DEBUG=True

flask run
```

## Como fazer as migrações

```sh
flask db init
flask db migrate
flask db upgrade
```

## Endpoints

```
POST - /register - Cadastra cartão
GET - /show - Mostra cartões cadastrados
```


## Documentação:

https://flask.palletsprojects.com/en/1.1.x/

https://marshmallow.readthedocs.io/en/stable/

https://flask-migrate.readthedocs.io/en/latest/

https://flask-sqlalchemy.palletsprojects.com/en/2.x/

