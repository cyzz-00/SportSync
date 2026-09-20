# Actualización de SportSync: usuarios y base de datos

Esta guía explica cómo actualizar el proyecto después de incorporar el registro y el inicio de sesión mediante correo electrónico.

## ✅ Funcionalidades disponibles

- Registro con nombre, correo electrónico y contraseña.
- Validación de correo único y confirmación de contraseña.
- Inicio de sesión con correo y contraseña.
- Saludo al usuario autenticado.
- Cierre de sesión.

Las cuentas se guardan en la base de datos local. Las contraseñas se almacenan mediante un **hash**, no como texto legible.

Se incorporaron la aplicación `usuarios` y el modelo personalizado `Usuario`.

> **Pendiente:** implementar los roles de Participante, Organizador y Administrador, junto con sus permisos.

## 1. Descargar los cambios

Cuando los cambios estén integrados en `main`:

1. Detén el servidor de Django con **Ctrl + C**.
2. Guarda y confirma tus cambios pendientes antes de cambiar de rama.
3. En GitKraken, selecciona la rama **`main`**.
4. Pulsa **Pull** para descargar los cambios.
5. Abre **Anaconda Prompt**.
6. Activa tu entorno de desarrollo y entra a la carpeta que contiene `manage.py`.

> Cada integrante debe utilizar el nombre de su propio entorno y la ruta local de su proyecto.

## 2. Revisar tu base de datos

El proyecto ahora utiliza un modelo de usuario personalizado. El procedimiento depende del estado de tu base local:

| Situación | Qué debes hacer |
|---|---|
| Acabas de clonar el proyecto y no tienes `db.sqlite3`. | Continúa con el paso 3. |
| Ya tienes una base actualizada con el modelo `usuarios.Usuario`. | Continúa con el paso 3. No la renombres. |
| Tienes una base anterior al cambio y solo contiene datos de prueba que no necesitas trasladar. | Consérvala como respaldo siguiendo las instrucciones de abajo. |
| Tienes una base anterior con datos que necesitas conservar en la nueva versión. | Consulta con el equipo antes de continuar para planificar su traslado. |

### Respaldar la base anterior

Con el servidor detenido, ejecuta desde la carpeta del proyecto:

```bat
ren db.sqlite3 db_antes_usuarios.sqlite3
```

Este comando cambia el nombre del archivo anterior para conservarlo como respaldo.

- Realiza este paso **una sola vez**, al pasar del modelo de usuario original al personalizado.
- Si ya existe un archivo con ese nombre, utiliza otro nombre para el respaldo y agrégalo a `.gitignore`.
- Los datos del respaldo **no se trasladarán automáticamente** a la nueva base.

## 3. Crear o actualizar las tablas

Ejecuta:

```bash
python manage.py migrate
```

Si no existe `db.sqlite3`, Django creará una nueva base de datos y aplicará las migraciones.

Si ya tienes la base actualizada, aplicará únicamente las migraciones pendientes. El mensaje `No migrations to apply` significa que no hay cambios pendientes.

> Las migraciones están incluidas en el repositorio. **No necesitas ejecutar `makemigrations` para recibir los cambios del equipo.**

## 4. Comprobar e iniciar el proyecto

Primero revisa la configuración:

```bash
python manage.py check
```

El resultado esperado es:

```text
System check identified no issues (0 silenced).
```

Después inicia el servidor:

```bash
python manage.py runserver
```

> Si algún comando muestra un error, comparte el mensaje con el equipo antes de continuar.

## 5. Probar el registro y el acceso

Con el servidor en ejecución, abre estas direcciones en el navegador:

| Página | Dirección |
|---|---|
| Inicio | http://127.0.0.1:8000/ |
| Registro | http://127.0.0.1:8000/usuarios/registro/ |
| Inicio de sesión | http://127.0.0.1:8000/usuarios/login/ |

### Lista de comprobación

- [ ] Crear una cuenta de prueba.
- [ ] Intentar registrar el mismo correo y comprobar que se rechace.
- [ ] Iniciar sesión con el correo y la contraseña registrados.
- [ ] Comprobar que aparezcan el saludo y el botón **Cerrar sesión**.
- [ ] Cerrar sesión y comprobar que vuelvan los botones de acceso.
- [ ] Probar una contraseña incorrecta y comprobar que aparezca un error.

Cada integrante debe crear su propia cuenta de prueba.

**El registro crea cuentas normales: no concede permisos de administrador ni de organizador.**

## 6. Qué compartimos por GitHub

| Se comparte | No se comparte |
|---|---|
| Código Python, HTML y estilos. | Base de datos local. |
| Archivos de migración. | Cuentas y datos de prueba. |
| Documentación del proyecto. | Contraseñas y claves secretas. |

**Push y Pull sincronizan el código, no las cuentas ni los datos de cada computadora.**

Estos archivos deben permanecer excluidos mediante `.gitignore`:

```gitignore
db.sqlite3
/db_antes_usuarios.sqlite3
/config/configuracion_local.py
```

Cada integrante debe conservar su archivo `configuracion_local.py` con su propia `SECRET_KEY`, siguiendo las instrucciones del README.

## Próximo paso

**CR-01: roles y permisos**

Implementaremos las diferencias de acceso entre:

- Participante.
- Organizador.
- Administrador.

---

[← Volver al README](README.md)