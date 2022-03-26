# proyectobasedj

Este repositorio es una base para nuevos proyectos en Djando

### revisiones pendientes 0.0.4
- lo del boton de agregar a favorito (Pendiente)
- lo del paquete meta (Desinstalado, para futuras versiones)
- en el footer mejor la alineacion y la barra de despazamiento (SOLUCIONADO!!)
- ckeditor agregar el code (Sin Solucion!!)
- mejorar la pagina editar contraseña / perfil (SOLUCIONADO!!)
- en perfil mejorar la parte del usuario (SOLUCIONADO!!)
- agregar el Ckeditor al home y a parte de entradas (SOLUCIONADO!!)
- lo del usuario y el email al registrarse (SOLUCIONADO!!!)
- por que el views de entrada tiene en comentarios los managers (se elimino del views.py y se importo a models.py SOLUCIONADO!!)
- lo del email de activacion (solucion 1 registrarse sin email de activacion SOLUCIONADO!!)


### Modificaciones
0.0.4
- Aplicacion home instalada
- Aplicacion entradas instalada
- Aplicacion favoritos instalada
- Quite la opcion apellidos
- El login sera con el mail no con el username
- Sitemap
- Slug
  
0.0.3
- Aplicacion de users modificada

0.0.1
- Archivo settings.py, dividido y modificado en la carpeta settings, dividido en 3 partes, base, local y prod (manager.py y wsgi.py se le agrego la direccion nueva a .local)
- Clave secreta protegida en el archivo secret.json
- Carpeta media para la subida de contenido
- Carpeta template para el front
- Carpeta static para los archivos estaticos 

### Paquetes instalados:
0.0.4
- django-model-utils
- ckeditor

0.0.2
- django-meta 2.0.0 https://django-meta.readthedocs.io/en/latest/index.html
  
0.0.1
- postgress
- pillow