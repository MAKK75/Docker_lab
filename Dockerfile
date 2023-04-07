#качаем образ убунту и входим в него
FROM ubuntu:22.04

#загружаем Питон и соглашаемся с установкой
RUN apt update 
RUN apt install -y python3


#Копируем скрипт внутрь контейнера
COPY prog.py prog.py

#Делаем так, чтобы скрипт выполнялся сразу при запуске контейнера
CMD python3 prog.py
