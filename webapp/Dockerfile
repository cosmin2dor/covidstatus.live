FROM python:3.8-alpine

# arbitrary location choice: you can change the directory
RUN mkdir -p /django
WORKDIR /django

ENV DEBUG 0

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY requirements.txt /django
RUN pip install -r requirements.txt

# copy our project code
COPY . /django
RUN python manage.py collectstatic --no-input -v 2

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
ENTRYPOINT gunicorn webapp.wsgi:application --bind 0.0.0.0:8000