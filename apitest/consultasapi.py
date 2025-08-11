import requests
import allure


@allure.step("Test GET all users")
def test_get_users_ok ():
   # Realizar una solicitud GET a una URL
   response = requests.get('http://127.0.0.1:8000/users')
   assert response.status_code == 200
   #assert isinstance(response.json(), list)

@allure.step("Test GET user by ID")
def test_get_some_user_ok ():
   # Realizar una solicitud GET apara obtener un usuario específico
   response = requests.get('http://127.0.0.1:8000/user/1')
   assert response.status_code == 200
   user = response.json()
   assert user["id"] == 1
   assert user["nombre"] == "mariano"

@allure.step("Test POST user")
def test_post_some_user_ok ():
   # Realizar una solicitud DELETE para eliminar un usuario
   data = {
     "id": 20,
     "nombre": "Gabo",
     "apellido": "Cizo",
     "edad": 28
    }
   response = requests.post('http://127.0.0.1:8000/user', json=data)
   assert response.status_code == 200
   user = response.json()
   assert user["message"] == "Usuario creado"
   assert user["user"] == "Gabo"


@allure.step("Test DELETE user")
def test_delete_some_user_ok ():
   # Realizar una solicitud DELETE para eliminar un usuario
   response = requests.delete('http://127.0.0.1:8000/user/20')
   assert response.status_code == 200
   user = response.json()
   assert user["message"] == "Usuario eliminado"
   assert user["user"] == "Gabo"
   response = requests.get('http://127.0.0.1:8000/user/20')
   assert response.status_code == 200
   #user = response.json()
   #assert user["message"] == "No se ha encontrado el usuario"

@allure.step("Test PUT user")
def test_put_some_user_ok ():
   # Realizar una solicitud PUT para actualizar un usuario
   data = {
       "id": 1,
       "nombre": "Gabo",
       "apellido": "Cizo",
       "edad": 29
   }
   response = requests.put('http://127.0.0.1:8000/user/1', json=data)
   assert response.status_code == 200
   user = response.json()
   assert user["message"] == "Usuario actualizado"

"""  
 assert user["id"] == 1
   assert user["nombre"] == "Gabo"
   assert user["apellido"] == "Cizo"
   assert user["edad"] == 29"""
 