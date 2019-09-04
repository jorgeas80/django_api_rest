Proyecto para curso de Django + REST Framework
===============================================

Repositorio para curso de creación de API REST con Django. Este fichero contiene notas útiles para empezar a trabajar.


==============
Base de datos
==============

La configuración de base de datos para que funcione con lo subido al repo sería así (en Linux):

.. code-block:: bash
    :linenos:
    :language: bash
    sudo su - postgres
    psql


Una vez en la base de datos:

.. code-block:: sql
    :linenos:
    :language: sql
    create database drf_api;
    create user "jorge" with password 'jorge';
    grant all privileges on database "drf_api" to "jorge";
