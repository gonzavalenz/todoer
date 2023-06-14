# Requisitos
Tener instalado:
  * Python
  * MySql

Luego de clonar el repo, antes de ejecutar cualquier comando es importante estar ubicados dentro de la carpeta todoer. Se puede verificar con el siguiente comando:

```
pwd
```

Crear un entorno virtual

```
python -m venv myenv
```

Instalar las dependencias

```
pip install -r requirements.txt
```

Crear un archivo '.env' con el siguiente contenido:
```
FLASK_APP='todo'
FLASK_DEBUG=1

FLASK_DATABASE_HOST='localhost'
FLASK_DATABASE_PASSWORD='password'
FLASK_DATABASE_USER='user'
FLASK_DATABASE='todoer'
```

Modificar los valores de las variables que sean necesarios

Por ultimo para correr la app debemos ejecutar el siguiente comando
```
python app.py
```


# Objetivo
El objetivo de la app es crear una lista de tareas a realizar, "ToDos".

* Crear un usuario: Permite a los usuarios registrarse en la aplicación proporcionando la información necesaria, como nombre de usuario y contraseña.

* Iniciar sesión: Los usuarios pueden iniciar sesión en la aplicación utilizando las credenciales de usuario que crearon previamente. Esto les brinda acceso a las funciones y características personalizadas de la aplicación.

* Crear tareas: Una vez que los usuarios han iniciado sesión, tienen la capacidad de crear tareas. Pueden ingresar una descripción de la tarea y marcar si ha sido completada o no.

* Modificar tareas: Los usuarios pueden realizar cambios en las tareas existentes. Pueden editar la descripción de una tarea o marcarla como completada o no completada, según sea necesario.

* Eliminar tareas: Los usuarios tienen la opción de eliminar tareas que ya no son relevantes o que ya han sido completadas. Esto les permite mantener su lista de tareas actualizada y ordenada.

* Cerrar sesión: Cuando los usuarios han terminado de utilizar la aplicación, pueden cerrar sesión de forma segura utilizando la función de logout. Esto asegura que su sesión esté cerrada y protege su información personal.