from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""para levantar el servidor de uvicorn --> uvicorn fapi:app --reload 
 donde fapi es el nombre del modulo .py que tejecutas """ 
 


"""http://127.0.0.1:8000/docs"""
"""http://127.0.0.1:8000/redoc"""

"""crea una clase y le asigna los campos tipados,  
definidos para no ingresar errores al hacer post o puts"""

class User(BaseModel):
    id:int
    nombre: str
    apellido: str
    edad:int

users_list = [User(id=1, nombre="mariano",apellido="aprea",edad=44),
              User(id=2,nombre="martin",apellido="lopez", edad=33),
              User(id=3,nombre="marta",apellido="loloa", edad=38),
              User(id=4,nombre="martina",apellido="fifo", edad=22)] 


@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id:int):
    users=filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except:
        return {"No se ha encontrado el usuario"}



@app.post("/users/")
async def create_user(item: User):
     return item
