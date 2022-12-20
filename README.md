# **Sistema de Gestion - Cinemar**
A través de la app Cinemark se pueden realizar y ver reservas para ver una película en dicho cine, gestionar a los usuarios que se registren en la aplicación, con la intención de disminuir la saturación de las colas y evitar que en algunas salas terminen vendiendo más entradas que la capacidad de la misma, ya que esto provoca pérdidas de ventas en funciones y de esta manera ayuda a no perder clientes.

### Pre-requisitos - se adjunta link de descarga

_*[Python](https://www.python.org) -  Lenguaje de Programación con el que se trabajo.
```
https://www.python.org/downloads/
```

_*[Visual Studio Code (VSC)](https://code.visualstudio.com) - IDE utilizado para el desarrollo de la aplicación.
```
https://code.visualstudio.com
```
_*[SQLite](https://www.sqlite.org) - Sistema de Gestión de base de datos utilizada para almacenar y acceder a los datos solo se descargan las extensiones de SQLite (SQLite Viewer - SQLTools SQlite)  en Visual Studio Code.

_*[TKinter](https://docs.python.org/es/3/library/tkinter.html) - Se importó esta librería de Python para realizar la interfaz gráfica.


### Como probarlo 🚀

* Para probarlo deberás hacer un clon de este proyecto en tu pc para ello las instrucciones se encuentran detalladas en la carpeta información del repositorio. 
* Una vez realizado todos los pasos anteriores para ejecutar el programa lo puedo hacer desde VSC donde dice CineApp.pyw al ejecutarlo se abrirá la ventana del programa.
* También puedo acceder a él desde la carpeta de tu pc donde guarde el proyecto haciendo doble clic en CineApp.pyw si tengo instalado Python correctamente se abrirá la ventana del programa.

### Inicio de sesion 📌
#### Puede iniciar sesión como cliente o como administrador, teniendo en cuenta los usuarios creados previamente:

| **Usuario** | **Contraseña** | **Rol** |
| :---: | :---: | :---: |
| scaloni | 181222 | admin |
| messi_10| 181222 | cliente |

#### En caso de que inicies sesion como cliente 📄 podrás acceder a las siguientes opciones:
* 1 -> Registrarse.
* 2 -> Iniciar sesión.
* 3 -> Ver listado de peliculas
* 4 -> Crear una reserva.
* 5 -> Ver el histórial de mis reservas.
* Otro caracter -> Cerrar Sesión

#### Consideraciones
-	No se puede registrar dos veces el mismo usuario.
-	No se puede seleccionar una función si no hay disponibilidad de butacas.
-	Los usuarios que registren 6 o más reservas dentro de un rango de tres meses acceden a un descuento automáticamente de acuerdo al día.

#### En caso de que inicies sesion como administrador 🛠️📦 podrás acceder a las siguientes opciones:
* 1 -> Iniciar sesión.
* 2 -> Ver listado de descuentos.
* 3 -> Modificar un descuento.
* 4 -> Ver listado de películas
* 5 -> Cargar Películas
* 6 -> Eliminar Película
* 7 -> Ver el listado de Salas.
* 8 -> Agregar una Sala.
* 9 -> Eliminar una Sala.
* 10 -> Ver listado de Funciones 
* 11 -> Editar una Función.
* 12 -> Agregar una Función.
* 13 -> Eliminar una Función
* 14 - Ver clientes que realizaron una reserva
* Otro caracter -> Cerrar Sesión


## Autores ✒️
* **Cardozo Macarena Soledad** - [SOLE-VME](https://github.com/SOLE-VME)
* **Gómez, Matías Agustín** - [Mati2173](https://github.com/Mati2173)
