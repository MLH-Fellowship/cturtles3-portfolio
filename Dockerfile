FROM python:3.8-slim-buster
 
RUN mkdir /cturtles3-portfolio
COPY requirements.txt /cturtles3-portfolio
WORKDIR /cturtles3-portfolio
RUN pip3 install -r requirements.txt
 
COPY . /cturtles3-portfolio
 
CMD ["gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:80"]
