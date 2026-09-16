# ProyectoDjango

# SportSync

Sistema de gestión de actividades y torneos deportivos amateur,
desarrollado con Python y Django para Desarrollo de Software V.

## Estado actual

El proyecto cuenta con la estructura inicial de Django y la aplicación
core. Las funcionalidades de SportSync se desarrollarán progresivamente.

## Herramientas necesarias

- Anaconda o Miniconda.
- Git.
- Visual Studio Code.
- GitKraken, para gestionar el repositorio visualmente.
- Cuenta de GitHub para colaborar.

## 1. Clonar el repositorio

En GitKraken, selecciona Clone e introduce esta dirección:

https://github.com/rd6burgos/SportSync.git

También puedes utilizar la terminal:

```bash
git clone https://github.com/rd6burgos/SportSync.git
cd SportSync
```

## 2. Crear y activar un entorno

Desde Anaconda Prompt:

```bash
conda create -n sportsync python=3.12
conda activate sportsync
```

Acepta la instalación cuando Conda solicite confirmación.

## 3. Instalar Django

Para esta configuración inicial utilizamos la serie Django 5.2:

```bash
python -m pip install "Django>=5.2,<5.3"
```

## 4. Crear la configuración local

Dentro de la carpeta config, crea un archivo llamado:

configuracion_local.py

Genera una clave propia ejecutando:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia el resultado en configuracion_local.py, entre comillas:

```python
SECRET_KEY = "PEGA_AQUI_TU_CLAVE_GENERADA"
```

El archivo config/settings.py debe importar la clave así:

```python
from .configuracion_local import SECRET_KEY
```

Cada integrante utilizará su propia clave local.
configuracion_local.py está excluido por .gitignore y no debe subirse
al repositorio.

## 5. Preparar la base de datos

Desde la carpeta que contiene manage.py:

```bash
python manage.py migrate
```

Esto crea las tablas necesarias en la base de datos local.
Cada integrante tendrá su propio archivo db.sqlite3.

## 6. Iniciar el servidor

```bash
python manage.py runserver
```

Abre en el navegador:

http://127.0.0.1:8000/

Para detener el servidor, presiona Ctrl + C.

## Organización del proyecto

- config/: configuración general y rutas principales.
- core/: aplicación inicial del proyecto.
- manage.py: herramienta para ejecutar comandos de Django.
- .gitignore: indica qué archivos quedan fuera del control de versiones.
- README.md: instrucciones del proyecto.

## Trabajo en equipo

1. Actualizar la rama main antes de comenzar una tarea.
2. Crear una rama con un nombre relacionado con la tarea,
   por ejemplo: pagina-acerca.
3. Desarrollar y comprobar los cambios localmente.
4. Revisar los archivos modificados y realizar un commit descriptivo.
5. Subir la rama a GitHub mediante Push.
6. Abrir un Pull Request hacia main.
7. Solicitar la revisión de otro integrante antes de integrar los cambios.

Cada integrante debe utilizar su propia cuenta e identidad de Git.

## Archivos que no se comparten

- config/configuracion_local.py
- db.sqlite3
- Archivos .env
- Entornos virtuales
- Archivos temporales de Python

Las migraciones de Django sí deben incluirse en el repositorio.