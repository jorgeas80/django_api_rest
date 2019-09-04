# Proyecto para curso de Django + REST Framework

La configuración de base de datos para que funcione con lo subido al repo sería así (en Linux):

```bash
sudo su - postgres
psql 
```

Una vez en la base de datos:

```sql
create database drf_api;
create user "jorge" with password 'jorge';
grant all privileges on database "drf_api" to "jorge";
```