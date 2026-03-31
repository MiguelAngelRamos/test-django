# Gestión de Superusuarios en Django (PostgreSQL)

Como administrador de un proyecto Django, necesitarás tener control total (acceso al panel de administración `/admin`, permisos sobre las bases de datos de todos los modelos y usuarios del sistema). Para ello crearás una cuenta especial de nivel administrador conocida como **Superusuario**.

A continuación, te mostramos los pasos exactos que debes aplicar en la terminal para gestionar esta cuenta clave, **asegurándote siempre de tener tu entorno virtual activado**.

---

## 1. Activar el Entorno Virtual (Requisito Previo)

Antes de lanzar comandos de administración en Django, asegúrate de estar dentro de tu entorno virtual (`venv`).
Abre tu consola/terminal (ej. PowerShell), dirígete a la carpeta del proyecto y ejecuta:

```powershell
.\venv\Scripts\Activate.ps1
```
*(Sabrás que funcionó porque verás `(venv)` al inicio de tu línea de comandos).*

---

## 2. Crear un Nuevo Superusuario

Una vez en el entorno virtual, usaremos la herramienta `manage.py` de nuestro proyecto:

```bash
python manage.py createsuperuser
```

Al presionar <kbd>Enter</kbd>, Django iniciará un proceso interactivo solicitándote los siguientes datos:
1. **Username (leave blank to use 'tu_usuario_local'):** Ingresa el nombre de administrador que desees (ej: `admin`, `miguel_root`).
2. **Email address:** Puedes colocar tu correo o dejarlo en blanco presionando Enter.
3. **Password:** Escribe tu contraseña. **Nota:** *¡No verás los caracteres mientras escribes en la consola por seguridad! Escríbela y presiona Enter.*
4. **Password (again):** Vuelve a escribirla para confirmar.

Si la contraseña es corta o simple, Django te lanzará un aviso de "Validation Error" advirtiendo que la contraseña es débil, pero **te preguntará si deseas usarla de todos modos**. Si estás en desarrollo local es seguro decir que `y` (sí).

✅ Una vez finalizado te dirá: `Superuser created successfully.`

---

## 3. ¿Olvidaste o quieres Cambiar la Contraseña?

Si posteriormente pierdes el acceso o simplemente deseas actualizar la contraseña por motivos de seguridad, Django te ofrece un comando nativo, evitando tener que tocar la base de datos de PostgreSQL directamente.

Ejecuta lo siguiente:

```bash
python manage.py changepassword nombre_del_usuario
```
*(Reemplaza `nombre_del_usuario` por el nombre real de tu superusuario)*

Se te solicitará:
1. Escribir la nueva contraseña.
2. Confirmar la nueva contraseña.

✅ Al finalizar exitosamente verás: `Password changed successfully for user 'nombre_del_usuario'.`

---

## 4. Probando el Acceso

Para probar que las credenciales funcionan correctamente, levanta tu servidor:

```bash
python manage.py runserver
```

1. Ve a tu navegador y entra a: `http://127.0.0.1:8000/admin/` (o puedes iniciar sesión normal en la app que acabamos de construir).
2. Utiliza las credenciales que acabas de configurar.

¡Felicidades, ahora tienes el control absoluto de la base de datos desde el ecosistema Django!
