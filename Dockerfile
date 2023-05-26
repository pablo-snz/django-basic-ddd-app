# Dockerfile
FROM python:3.11-slim-buster

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias necesarias
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install poetry

# Copiar pyproject.toml para instalar dependencias
COPY pyproject.toml poetry.lock /app/

# Instalar dependencias
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copiar el código de la app
COPY . /app/

# Copiar el script de entrada y darle permisos de ejecución
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Exponer puerto 8000 para Django
EXPOSE 8000

# Ejecutar el script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
