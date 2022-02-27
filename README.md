# Título del Proyecto

_API REST PARA RESERVA DE HABITACIONES_

### Despliegue 🔧

_sigue los siguientes pasos para poder desplegar el proyecto en tu pc_

_1 - clona el repositorio_

```
git clone https://github.com/cesarmayta/reservasapi.git
```

_2 - crear un entorno virtual y activalo_

```
python -m venv venv
source venv/scripts/activate
```

_3 - instala las dependencias_

```
pip install -r requirements.txt
```

_4 - realiza las migraciones_

```
python manage.py migrate
```

_5 - despliega el proyecto_

```
python manage.py runserver
```

### endpoints del proyecto 🔩

_http://localhost:8000/registro_ [metodos: POST]
permite el registro de un nuevo cliente que es el 1er paso para poder generar una reserva

_http://localhost:8000/login_[metodos: POST]
permite el login de un cliente registrado y devuelve un jwt para autenticación

_http://localhost:8000/habitacion_[metodos: GET]
permite el mostrar las habitaciones

_http://localhost:8000/habiacion/[id]_ [metodos: GET]
carga una sola habitación

_http://localhost:8000/reserva_ [metodos: POST]
permite el registro de la reserva

NOTA: todos los endpoints necesitan autenticación JWT excepto registro y login

