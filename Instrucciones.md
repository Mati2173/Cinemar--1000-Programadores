# **Instrucciones para trabajar con el repositorio**

### Pasos para clonar el repositorio de GitHub en tu computadora:

1. Crear una carpeta en donde vas a guardar el proyecto localmente.

2. Abrir la carpeta con Visual Studio Code: Hacer click derecho sobre la carpeta y seleccionar **"Abrir con Code"**.

3. Una vez abierto el VSC dentro de la carpeta, en la parte superior apretar en **"Terminal"** y seleccionar **"Nuevo terminal"**.

4. Se va a abrir la consola de Windows en dicha carpeta. Escribir en ella el siguiente comando:
```
   git clone https://github.com/Mati2173/Cinemar--1000-Programadores.git
```
> Este comando copia todos los archivos del respositorio de GitHub en la carpeta seleccionada.

5. Dentro de la carpeta que elegiste, se creó una nueva carpeta con el nombre **"Cinemar--1000-Programadores"**. En ella, están todos los archivos del repositorio. Para realizar cambios en el proyecto, seguí las instrucciones detalladas a continuación.

- - - - - -
### Pasos para subir los cambios en GitHub:

1. Abrir la carpeta donde se encuentran todos los archivos del proyecto con VSC.

2. Una vez abierta, en la parte superior apretar en **"Terminal"** y seleccionar **"Nuevo terminal"**.
> PARA RECORDAR: Comprobar que la terminal esté ubicada dentro de la carpeta correspondiente, de lo contrario podés ir accediendo a cada carpeta con el comando: cd Nombre_de_la_carpeta

3. Hacer los cambios en el proyecto (Crear archivos, modificar otros, etc.) y luego de ello, guardá los cambios localmente.

4. Una vez realizados los cambios, hay que subirlos a GitHub con los siguientes comandos (en el mismo orden):
```
   git add .
```
> Este comando agrega **todos** los nuevos archivos o los cambios hechos en los mismos.

 ```
   git commit -m "Mensaje"
 ```
> En "Mensaje" detallá el cambio que hiciste en pocas palabras. Este comando confirma los cambios.

```
   git push
```
> Este comando sube todos los cambios a GitHub.

5. Los cambios ya están subidos en GitHub.

- - - - - -
### Pasos para traer los cambios desde GitHub (Actualizar los archivos locales):

1. Abrir la carpeta donde se encuentran todos los archivos del proyecto con VSC.

2. Abrir una nueva terminal en dicha carpeta.

3. Escribir el siguiente comando:
```
   git pull
```
> Este comando actualiza el repositorio local con los cambios realizados por otro usuario.

4. El respositorio actualizado con los últimos cambios ya está en tu computadora. Ya podés seguir trabajando con el proyecto. Luego de realizar los cambios necesarios, subilos a GitHub siguiendo las instrucciones detalladas en **"Pasos para subir los cambios en GitHub"**.