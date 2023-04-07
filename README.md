# Docker_lab
Лабораторная работа DevOps (Макаров).
1. Создаем образ с помощью docker-файла (прикреплен), загружаем Питон, собираю в PowerShell с помощью build.
 ![image](https://user-images.githubusercontent.com/60113205/230615684-8dc02cd2-43ec-4dbb-8103-5fae56b22b97.png)
![image](https://user-images.githubusercontent.com/60113205/230615698-bf64725e-0693-4996-a120-f86e4628ae66.png)

 
2. Создаю Питон-файл, и привязываю к папке.
 ![image](https://user-images.githubusercontent.com/60113205/230615716-b0f92622-775b-4e07-973c-5eaf2337b9d3.png)
![image](https://user-images.githubusercontent.com/60113205/230615740-0445c480-840d-4f28-b391-fbbc101c1f43.png)
Все в наличии.

Дописываем COPY в файл Докер и заново билдим в консоли. Получаем контейнер версии 3, в котором уже есть программа.
![image](https://user-images.githubusercontent.com/60113205/230615781-0358b015-5ac0-4d95-818d-e553978dc13f.png)
 
Дополняем функционал докер-файла, чтобы скрипт выполнялся сразу при запуске контейнера, билдим его как 16 версию и запускаем.

Демонстрация работы.
![image](https://user-images.githubusercontent.com/60113205/230615880-a5c5e450-54d6-4a4e-97ab-29143f9205ea.png)

 
