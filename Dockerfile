FROM python:3-slim

# Copiar o código para o container
RUN mkdir /code
COPY . /code
WORKDIR /code

# Instalar as dependências
RUN pip install django django_crispy_forms crispy_bootstrap5 Pillow

# Rodar o migration
RUN python manage.py migrate

# Rodar o servidor
# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]