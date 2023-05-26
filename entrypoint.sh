#!/bin/sh

# Ejecutar las migraciones
python manage.py migrate

# Ejecutar el servidor
exec "$@"
