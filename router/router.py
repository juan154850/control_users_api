from fastapi import APIRouter, Response, HTTPException, status, Request
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from schema.user_schema import UserSchema, UserUpdateSchema
from model.users import users
from config.db import engine 
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import re
from math import ceil
from sqlalchemy import select, func

user = APIRouter()
templates = Jinja2Templates(directory="templates")


@user.get("/")
def root(request: Request, skip: int = 0, limit: int = 10):
        with engine.connect() as connection:
            # Obtener el número total de registros
            total = connection.execute(select(func.count(users.c.id))).scalar()

            # Consulta con limit y offset para la paginación
            result = connection.execute(
                users.select().offset(skip).limit(limit)
            ).fetchall()

            all_values_dict = []

            for elem in result:            
                dict_value = dict(zip(["id","first_surname","first_name","other_name","country","email"], elem))     
                all_values_dict.append(dict_value)                           

            # Calcular el número de páginas disponibles
            pages = ceil(total / limit)

            template = "users.html"
            context = {
                "request": request,
                "users": all_values_dict,
                "skip": skip,
                "limit": limit,
                "total": total,
                "pages": pages
            }

            return templates.TemplateResponse(template, context=context)


@user.get("/api/new_user", response_class=HTMLResponse)
async def new_user(request: Request):
    country_options = ["Colombia", "Estados Unidos"]
    context = {"request": request, "country_options": country_options}        
    return templates.TemplateResponse("new_user.html", context=context)    

# Create method
@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as connection:

        new_user = data_user.dict()  
        country = new_user["country"]

        # create the email
        first_name = new_user["first_name"]
        first_surname = new_user["first_surname"].replace(" ", "")
        email_domain = "project.com.us"

        if country.lower() == "colombia":
            email_domain = "project.com.co"

        # check if email already exists
        email_count = 1
        while True:
            email = f"{first_name}.{first_surname}"
            if email_count > 1:
                email += f".{email_count}"
            email += f"@{email_domain}"
            
            # add email validation
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Invalid email format")
            
            result = connection.execute(users.select().where(users.c.email == email)).fetchone()
            if result is None:
                break
            email_count += 1
            
        new_user["email"] = email.lower()       

        connection.execute(users.insert().values(new_user))
        connection.commit()

        return Response(status_code=HTTP_201_CREATED)

# Get all the users method
@user.get("/api/user", response_model=List[UserSchema])
def get_users(skip: int = 0, limit: int = 10):
    with engine.connect() as connection:

        result = connection.execute(
            users.select().offset(skip).limit(limit)
            ).fetchall()
        all_values_dict = []

        for elem in result:            
            dict_value = dict(zip(["id","first_surname","first_name","other_name","country","email"], elem))     
            all_values_dict.append(dict_value)                           

        return all_values_dict

# Get one user method
@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user_by_id(user_id: int):
    with engine.connect() as connection:
        result = connection.execute(
            users.select().where(users.c.id == user_id)
        ).first()
        
        if result:
            dict_value = dict(zip(["id","first_surname","first_name","other_name","country","email"], result))            
            return dict_value            
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#Update user
@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_update:UserUpdateSchema , user_id:str):
    with engine.connect() as connection:
        connection.execute(
            users.update().values(
            first_surname=data_update.first_surname,
            first_name=data_update.first_name,
            other_name=data_update.other_name,
            country = data_update.country 
            ).where(users.c.id == user_id)
        )

        result = connection.execute(
            users.select().where(users.c.id == user_id)
            ).first()
        
        if result:
            dict_value = dict(zip(["id","first_surname","first_name","other_name","country","email"], result))  
            connection.commit()          
            return dict_value            
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        

#Delete User
@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    with engine.connect() as connection:
        connection.execute(
            users.delete().where(users.c.id == user_id)
        )     
        # connection.commit()   
        return Response(status_code=HTTP_204_NO_CONTENT)