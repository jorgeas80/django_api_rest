#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 <<-EOSQL
    create database drf_api;
    create user "jorge" with password 'jorge';
    grant all privileges on database "drf_api" to "jorge";
    alter user jorge createdb;
EOSQL
