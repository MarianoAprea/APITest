import requests



# Realizar una solicitud POST
data = {
  "id": 10,
  "nombre": "Henry",
  "apellido": "Costas",
  "edad": 70
}
#response = requests.post('http://127.0.0.1:8000/users', data=data)


def test_get_users_ok ():
   # Realizar una solicitud GET a una URL
   response = requests.get('http://127.0.0.1:8000/users')
   assert response.status_code == 200
   #assert isinstance(response.json(), list)

def test_get_some_user_ok ():
   # Realizar una solicitud GET apara obtener un usuario específico
   response = requests.get('http://127.0.0.1:8000/user/1')
   assert response.status_code == 200
   user = response.json()
   assert user["id"] == 1
   assert user["nombre"] == "mariano"

   