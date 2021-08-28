FROM postgres:12.6

COPY ./1_create_table.sql /docker-entrypoint-initdb.d/
COPY ./2_insert_material.sql /docker-entrypoint-initdb.d/
COPY ./3_insert_slicer.sql /docker-entrypoint-initdb.d/
COPY ./4_insert_machine.sql /docker-entrypoint-initdb.d/
COPY ./5_insert_user.sql /docker-entrypoint-initdb.d/
COPY ./6_insert_part.sql /docker-entrypoint-initdb.d/
COPY ./7_insert_permission_part.sql /docker-entrypoint-initdb.d/
COPY ./8_insert_permission.sql /docker-entrypoint-initdb.d/
