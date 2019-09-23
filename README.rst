Proyecto para curso de Django + REST Framework
===============================================

Repositorio para curso de creación de API REST con Django. Este fichero contiene notas útiles para empezar a trabajar.


=========================
Configuración del entorno
=========================

Necesitaremos instalar en nuestra máquina:

* `Python 3 <https://www.python.org/>`_.
* `PostgreSQL <https://www.postgresql.org>`_.
* `VSCode <https://code.visualstudio.com/>`_.
* `Cliente GIT <https://git-scm.com/downloads>`_.
* `Emulador de consola CMDer (opcional, solo Windows) <https://cmder.net/>`_.

Una vez instalado, crearemos manualmente un directorio de trabajo en nuestra máquina. A partir de ahora, todas las operaciones las haremos desde dentro de ese directorio.


----------------------------
Creación de entorno virtual
----------------------------


A continuación, crearemos un entorno virtual desde una línea de comandos, ejecutando lo siguiente [#]_::

    python -m venv venv

Siendo el segundo *venv* el nombre del entorno virtual. Se puede usar el nombre que se quiera.

Activamos el entorno virtual ejecutando lo siguiente **desde sistemas Windows**::

    venv\Scripts\activate.bat

O lo siguiente **desde sistemas Linux/Mac**::

    source venv/bin/activate

----------------------------------
Instalación de software necesario
----------------------------------

Ahora instalaremos los paquetes de Python necesarios para poder comenzar a trabajar en un proyecto Django. Para ello, ejecutamos lo siguiente [#]_::

    pip install Django djangorestframework psycopg2

Adicionalmente, se puede instalar `PGAdmin 3 <https://www.pgadmin.org/>`_, un popular gestor gráfico para la base de datos PostgreSQL.

==============
Base de datos
==============

Vamos a crear una base de datos para el proyecto y un usuario con permisos para dicha base de datos. Se puede hacer visualmente con PGAdmin o mediante el cliente psql.

Si se hace mediante el cliente de consola psql, debemos hacer lo siguiente (en Linux)::

    sudo su - postgres
    psql

Una vez en la base de datos::

    create database drf_api;
    create user "jorge" with password 'jorge';
    grant all privileges on database "drf_api" to "jorge";
    alter user jorge createdb;

Hecho estto, estaríamos listos para iniciar un proyecto de Django.


============================
Creación de proyecto Django
============================

Desde línea de comandos, ejecutamos::

    django-admin.py startproject djapi

Eso creará el esqueleto del proyecto dentro del subdirectorio *djapi*. Es un buen momento para guardar el trabajo en un repositorio.


====================
Configurar usuarios
====================

Vamos a configurar autenticación y autorización para nuestros usuarios usando DRF. Así que, lo primero que haremos, será añadir
esto en el fichero *settings.py* al final de INSTALLED_APPS::

    'rest_framework',
    'rest_framework.authtoken'

Después, añadiremos al final de dicho fichero *settings.py* lo siguiente::

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        )
    }

Y por último, correremos las migraciones::

    python manage.py migrate

Con esto estaríamos listos para empezar a trabajar


===============================================
Almacenamiento del proyecto en repositorio git
===============================================

Vamos a crear un repositorio vacío y guardar lo creado hasta ahora::

    git init
    git add -A
    git commit -am "Initial commit"

Si estamos usando Github o similar, podemos hacer también *git push* para sincronizarnos con el repositorio central.




.. [#] Si en la máquina está instalado también Python 2, el ejecutable a lanzar será python3
.. [#] En Linux, para instalar psycopg2, antes hay que ejecutar  `sudo apt install python3-dev postgresql-server-dev-all`
