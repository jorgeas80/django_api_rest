Proyecto para curso de Django + REST Framework
===============================================

Repositorio para curso de creación de API REST con Django. Este fichero contiene notas útiles para empezar a trabajar.


=========================
Configuración del entorno
=========================
En Linux, para instalar psycopg2, antes hay que ejecutar esto::

    sudo apt install python3-dev postgresql-server-dev-all

La alternativa, es instalar psycopg2-binary en vez de psycopg2

==============
Base de datos
==============

La configuración de base de datos para que funcione con lo subido al repo sería así (en Linux)::

    sudo su - postgres
    psql

Una vez en la base de datos::

    create database drf_api;
    create user "jorge" with password 'jorge';
    grant all privileges on database "drf_api" to "jorge";


Para volcar los datos una vez corrida la migración de datos::

    python manage.py dumpdata --indent 2 dj_puro.Category > dj_puro/fixtures/categories.json
    python manage.py dumpdata --indent 2 dj_puro.SubCategory > dj_puro/fixtures/subcategories.json