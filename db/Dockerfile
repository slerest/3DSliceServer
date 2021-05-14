FROM postgres:12.6

COPY ./1_create_table.sql /docker-entrypoint-initdb.d/
COPY ./2_insert_material.sql /docker-entrypoint-initdb.d/
COPY ./3_insert_slicer.sql /docker-entrypoint-initdb.d/
COPY ./4_insert_machine.sql /docker-entrypoint-initdb.d/
