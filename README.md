# Real-Time Web

Real-time website implementation with different methods in Django.


#

# How to Run Project

## Download Codes

```
git clone https://github.com/dori-dev/real-time-web.git
```

```
cd real-time-web

python -m venv env
source env/bin/activate
```

## Short Polling

```
cd short-polling
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

## Long Polling

```
cd long-polling
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic

python -m gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker
```

## Web Socket

```
cd websocket
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

## Server Send Event(SSE)

```
cd sse
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```

## Open In Browser

Main Page: [127.0.0.1:8000](http://127.0.0.1:8000/)<br>

#

## Links

Download Source Code: [Click Here](https://github.com/dori-dev/real-time-web/archive/refs/heads/master.zip)

My Github Account: [Click Here](https://github.com/dori-dev/)
