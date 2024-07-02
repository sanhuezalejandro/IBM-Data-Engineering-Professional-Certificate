#!/bin/bash

# Obtener la contraseña de root de MySQL del archivo .env
MYSQL_ROOT_PASSWORD=$(grep MYSQL_ROOT_PASSWORD MySQL/.env | cut -d '=' -f2)

# Definir el comando para exportar los datos
COMMAND="docker exec -i mysql_container mysqldump -uroot -p${MYSQL_ROOT_PASSWORD} sales sales_data > sales_data.sql"

# Ejecutar el comando
eval $COMMAND

