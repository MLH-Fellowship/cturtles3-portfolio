FROM python:3.8-slim-buster
 
RUN mkdir /cturtles3-portfolio
COPY requirements.txt /cturtles3-portfolio
WORKDIR /cturtles3-portfolio
RUN pip3 install -r requirements.txt
 
COPY . /cturtles3-portfolio

#Below will be done by bashscript 
#CMD ["gunicorn", "wsgi:app", "-w 1", "-b 0.0.0.0:80"]

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]
