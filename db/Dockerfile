FROM postgres:13.0

COPY ./1_create_table.sql /docker-entrypoint-initdb.d/
COPY ./2_insert_material.sql /docker-entrypoint-initdb.d/
