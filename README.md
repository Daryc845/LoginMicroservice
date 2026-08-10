# Login Microservice

Microservicio de autenticación desarrollado con Django y MySQL, pensado para integrarse en un sistema de microservicios más grande donde la autenticación es un servicio independiente, escalable y fácil de operar.

## 🎯 Propósito

Este servicio expone dos operaciones básicas:

- Crear usuarios
- Autenticar usuarios

Su objetivo es actuar como un punto de entrada para la lógica de login dentro de una arquitectura distribuida, donde otros servicios pueden consumirlo de forma desacoplada.

---

## 🧰 Tecnologías utilizadas

- Python 3.x
- Django 5.x
- MySQL
- MySQL Workbench
- Django ORM
- SQLite-like local development support via Django project structure

### Stack técnico resumido

- Backend: Django
- Persistencia: MySQL
- ORM: Django Models
- Gestión de base de datos: MySQL Workbench
- Arquitectura objetivo: microservicios con descubrimiento de servicios mediante Eureka

---

## 🏗️ Estructura del proyecto

```text
login_microservice/
├── manage.py
├── login_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
└── login_microservice/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## ⚙️ Requisitos previos

Antes de ejecutar este microservicio, asegúrate de tener instalado:

- Python 3.10 o superior
- pip
- MySQL Server
- MySQL Workbench
- Virtualenv (opcional pero recomendado)

---

## 🚀 Ejecución local

### 1. Crear un entorno virtual

```bash
python -m venv venv
source venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```bash
pip install -r login_microservice/requirements.txt
```

### 3. Configurar la base de datos en MySQL

Este proyecto está preparado para trabajar con MySQL. Puedes crear la base de datos desde MySQL Workbench con este comando SQL:

```sql
CREATE DATABASE login_microservice_db;
```

También puedes crear el esquema manualmente desde Workbench y verificar que el usuario configurado en [login_microservice/settings.py](login_microservice/settings.py) tenga permisos sobre esa base de datos.

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Levantar el servicio

```bash
python manage.py runserver 0.0.0.0:8000
```

El servicio quedará disponible en:

```text
http://localhost:8000
```

---

## 🔗 Endpoints disponibles

### Crear usuario

```bash
curl -X POST http://localhost:8000/login_app/create/ \
  -H "Content-Type: application/json" \
  -d '{"userid":"admin","password":"123456"}'
```

### Autenticar usuario

```bash
curl -X POST http://localhost:8000/login_app/auth/ \
  -H "Content-Type: application/json" \
  -d '{"userid":"admin","password":"123456"}'
```

---

## 🗄️ Integración con MySQL Workbench

MySQL Workbench se utiliza para diseñar, administrar y visualizar la base de datos relacional del servicio. En este proyecto, la base de datos principal es:

```text
login_microservice_db
```

### Flujo recomendado

1. Crear la base de datos en Workbench.
2. Conectar el servicio Django a esa instancia.
3. Revisar tablas generadas por los modelos con migraciones.
4. Monitorear y ajustar estructuras según crezca el sistema.

Esto permite tener una visión más clara del modelo de datos y facilita la evolución del microservicio cuando se integran más módulos.

---

## 🧩 Integración en un esquema de microservicios con Eureka

En una arquitectura más grande de microservicios, este proyecto puede funcionar como el servicio de autenticación del sistema. Su rol sería:

- recibir solicitudes de login y registro,
- validar credenciales contra la base de datos MySQL,
- devolver una respuesta de autenticación al gateway o a otros servicios.

### Cómo encaja con Eureka

En un ecosistema distribuido, Eureka se usa para el descubrimiento de servicios. En ese contexto:

- este microservicio sería registrado como un servicio disponible,
- otros servicios podrían encontrarlo dinámicamente sin hardcodear IPs o puertos,
- el gateway podría dirigir las peticiones de autenticación hacia este servicio automáticamente.

### Visión de arquitectura

```text
Client → API Gateway → Login Microservice
                      ↓
                 Eureka Server
                      ↓
            Otros microservicios
```

En este diseño:

- el microservicio de login expone la lógica de usuario,
- Eureka permite descubrirlo de forma centralizada,
- MySQL Workbench administra la persistencia relacional del servicio.

> Nota: este repositorio actual contiene la implementación del microservicio Django y su conexión a MySQL, mientras que la integración con Eureka sería la siguiente capa de despliegue y descubrimiento en un sistema más amplio.

---

## 🛠️ Troubleshooting

Si aparece un error relacionado con MySQL:

- verifica que el servidor esté corriendo,
- confirma que la base de datos exista,
- revisa las credenciales en [login_microservice/settings.py](login_microservice/settings.py),
- asegúrate de que el usuario tenga permisos sobre la base de datos.

Si aparece un error de dependencias:

```bash
pip install --upgrade pip
pip install -r login_microservice/requirements.txt
```

---

## ✅ Resumen

Este microservicio representa una base sólida para manejar autenticación con Django y MySQL, con una arquitectura lista para crecer hacia un sistema distribuido donde MySQL Workbench y Eureka juegan papeles clave en persistencia y descubrimiento de servicios.
