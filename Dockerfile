FROM python:3.8

RUN pip3 install Django==4.1.5
RUN pip3 install requests
RUN pip3 install django-environ

RUN mkdir /home/Tp_Docker_G5

VOLUME /home/Tp_Docker_G5
