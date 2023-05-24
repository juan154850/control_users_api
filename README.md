# API - Registration and control of employees

## Description

The purpose of this project is to create a system that allows the registration of employees for a company. Through the API, current employees can be consulted, new employees can be created and existing employees can be deleted. 

The project has been developed with Python, FastAPI, and Xampp for database management; forms and styles are managed by Jinja2Templates. 


## Authors

- [@juanb154850](https://gitlab.com/juanb154850)

## Necessary programs

For the execution of the project, xampp must be installed to manage the MySQL database. 
Link: https://www.apachefriends.org/es/download.html

Additionally, it is recommended to use VS Code as a code editor.  

## Some of the dependencies are: 
* FastAPI
* uvicorn
* pymysql
* SQLAlchemy
* jinja2

NOTE: Remember that to install the dependencies, you can make use of the following command, where name: is the package you want to install:

```bash
  pip install "name"
```

## Instructions for installation and use:

1. Using the console, the virtual environment is created
```bash
 python3 -m venv venv
```
2. In a python, console run the virtual environment (From VS Code, and located in main.py right click > run python file in terminal).

3. All dependencies are installed with:
```bash
 pip install -r .\requirements.txt
 ```
4. You must import the table data_users.sql in any table you want and in the next step, specify this table.

5. The data to enter the database are changed (config > db.py > line 3).
```bash
  mysql+pymysql://user:password@localhost:3306/table_name
```

6. The server is executed with:
```bash
 uvicorn main:app --reload
 ```
Now, everything will be ready for use

## API Reference

#### Root

```http
  GET /Root
```

| Parameter | Type              | Description                |
| :-------- | :-------          | :------------------------- |
| `skip`    | `integer (query)` | Default value : 0          |
| `limit`   | `integer (query)` | Default value : 10         |  

##### Responses

| Code       | Description                       |
| :--------  | :-------------------------------- |
| `200`      | Successful Response               |
| `422`      | Validation Error                  |

#### New User

```http
  GET /api/new_user
```
* No parameters

##### Responses

| Code      | Description                       |
| :-------- | :-------------------------------- |
| `200`     | Successful Response               | 

#### Get Users

```http
  GET /api/user
```
| Parameter | Type              | Description                |
| :-------- | :-------          | :------------------------- |
| `skip`    | `integer (query)` | Default value : 0          |
| `limit`   | `integer (query)` | Default value : 10         |

##### Responses

| Code      | Description                       |
| :-------- | :-------------------------------- |
| `200`     | Successful Response               |
| `422`     | Validation Error                  |

#### Get User By Id

```http
  GET /api/user/{user_id}
```

| Parameter | Type             | Description                |
| :-------- | :-------         | :------------------------- |
| `user_id` | `integer (path)` | user_id                    |

##### Responses

| Code       | Description                       |
| :--------  | :-------------------------------- |
| `200`      | Successful Response               |
| `422`      | Validation Error                  |

#### Create User

```http
  POST /api/user
```
* No parameters

##### Responses

| Code      | Description                       |
| :-------- | :-------------------------------- |
| `201`     | Successful Response               |
| `422`     | Validation Error                  |

#### Update User

```http
  PUT /api/user/{user_id}
```

| Parameter | Type            | Description                |
| :-------- | :-------        | :------------------------- |
| `user_id` | `string (path)` | user_id                    |

##### Responses

| Code      | Description                       |
| :-------- | :-------------------------------- |
| `200`     | Successful Response               |
| `422`     | Validation Error                  |

#### Delete User

```http
  DELETE /api/user/{user_id}
```

| Parameter | Type            | Description                |
| :-------- | :-------        | :------------------------- |
| `user_id` | `string (path)` | user_id                    |

##### Responses

| Code       | Description                       |
| :--------  | :-------------------------------- |
| `204`      | Successful Response               |
| `422`      | Validation Error                  |

NOTE: If you wish to test and review the API documentation in more detail, go to the "/docs" path on your server. 
