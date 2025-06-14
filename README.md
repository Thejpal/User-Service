# **User Service**
User authentication service to handle user registration, login and getting the current user. This is a sample service to explore the concepts of Logger, Middleware, Docker and gain a deeper understanding of FastAPI framework.

## **Index**
* [Setup](#Setup)
* [Usage](#Usage)
* [Folder Structure](#Folder-structure)

## **Setup**
Clone the repository
```python
git clone https://github.com/Thejpal/User-Service.git
```
Install the requirements to run the files
```python
pip install -r requirements.txt
```
Set the following environmental variables in .env file
```python
JWT_SECRET_KEY="<your-secret-key>"
ALGORITHM="HS256"
TOKEN_EXPIRATION_MINUTES=30
DATABASE_URL="postgresql+psycopg2://admin:password@postgres:5432/userdb"
POSTGRES_USER="admin"
POSTGRES_PASSWORD="password"
POSTGRES_DB="userdb"
SERVICE_NAME="User Service"
```
Run the following command in bash shell to generate a random hex string for JWT_SECRET_KEY
```python
openssl rand -hex 32
```

## **Usage**
Start the application
```python
docker-compose up -d
```
Stop the application
```python
docker-compose down
```

## **Folder Structure**
- [src](/src) - *The source code of the project resides here*
   * [auth](/src/auth) - *Model, Controller and Service code for the Authentication service*
       * [model.py](/src/auth/model.py) - *Pydantic model definitions for the service*
       * [controller.py](/src/auth/controller.py) - *Defining the endpoints for the service*
       * [service.py](/src/auth/service.py) - *Business logic to handle the authentication*
   * [database](/src/database) - *Initialize database*
       * [db.py](/src/db.py) - *Database creation or initialization logic for the service*
   * [entities](/src/entities) - *Database model definitions*
       * [user.py](/user.py) - *User table definition for the database*
   * [logger.py](/src/logger.py) - *Setting logger with formatter and handler*
   * [middleware.py](src/middleware.py) - *Setting middleware to work with requests before and after processing*
   * [settings.py](src/settings.py) - *Environmental variables as settings for the application*
   * [context.py](src/context.py) - *Defining request context*
- [main.py](/main.py) - *Entrypoint for the application*
- [Dockerfile](/Dockerfile) - *Dockerfile to build an image for the FastAPI application*
- [docker-compose.yml](/docker-compose.yml) - *Docker compose file to spin up both postgres and FastAPI servers*
- [requirements.txt](/requirements.txt) - *Requirements to setup and run the service*
- [.dockerignore](/.dockerignore) - *Files to ignore during docker image creation*
- [docker_notes.txt](/docker_notes.txt) - *Notes on docker and docker-compose*