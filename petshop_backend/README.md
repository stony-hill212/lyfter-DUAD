# Pet Shop Backend API

API Backend para un sistema e-commerce desarrollado mediante Flask, SQLAlchemy, PostgreSQL, JWT authentication, 
Redis caching, asi como pruebas (unit testing) automatizadas.

## Features

- User registration and login
- JWT authentication (RS256)
- Role-based authorization (Admin/User)
- Product management
- Shopping cart management
- Purchase checkout
- Invoice generation
- Purchase returns
- Stock management
- Redis caching
- Automated unit testing

## Tecnologias utilizadas

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Marshmallow
- Redis
- Pytest


## Installation

Clonar el repositorio:
git clone <repository_url>

Crear ambiente virtual:

python -m venv venv

Activar ambiente:
venv\Scripts\activate

Instalar dependencias:
pip install -r requirements.txt


## Variables del ambiente virtual

Crear un archivo .env con:

DATABASE_URL=

SECRET_KEY=

REDIS_URL=

JWT_PRIVATE_KEY=

JWT_PUBLIC_KEY=


## Database Setup

flask db init

flask db migrate -m "Initial migration"

flask db upgrade


## Correr la aplicacion

python app.py


## Authentication

POST /auth/register

POST /auth/login

GET /auth/profile


## Products

POST /products/

GET /products/

GET /products/<id>

PUT /products/<id>

DELETE /products/<id>


## Cart

GET /cart/

POST /cart/add

PUT /cart/update

DELETE /cart/remove/<product_id>


## Purchases

POST /purchases/checkout


## Invoices

GET /invoice/

GET /invoice/<invoice_number>


## Returns

POST /return/<invoice_number>


## Redis Caching

Endpoints con caching implementado:

- GET /products/
- GET /products/<id>
- GET /invoice/
- GET /invoice/<invoice_number>

La invalidacion ocurre cuando:

- Los productos son creados
- Los productos son actualizados
- Los productos son eliminados
- Se realiza alguna devolucion

TTL fue aplicado.


## Correr los tests

Activar ambiente virtual:

```bash
venv\Scripts\activate
```

Correr unit testing:

```bash
pytest -v
```

Generar reporte automatico:

```bash
python run_tests.py
```

Total de pruebas realizadas: 14
