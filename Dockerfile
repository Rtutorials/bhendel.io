FROM python:3.8

WORKDIR /opt
ADD / /opt
RUN pip freeze > requirements.txt
RUN pip install -r req.txt
RUN pip install flask
RUN set FLASK_APP=app.py
RUN ls 


ENTRYPOINT export FLASK_APP=app.py
ENTRYPOINT flask run --host 0.0.0.0
