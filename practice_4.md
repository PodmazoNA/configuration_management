# Практическая работа №4
## 🌸Задача №1
На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
![pract4_1](https://github.com/user-attachments/assets/4e21d977-746a-4999-a856-10a902763de5)
```bash
git commit
git tag in
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout in
```
![pract4_2](https://github.com/user-attachments/assets/3d471cf4-c50f-4110-9a77-5be99314279f)
## 🌸Задача №2
Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.
```bash
git init
git config user.name "coder1"
git config user.email "coder1@gmail.com"
echo print("Hello, World!") > prog.py
git add prog.py
git commit -m "first commit"
```
![pract4_3](https://github.com/user-attachments/assets/b9b81204-6cd1-4f4f-b914-18341ca00d4b)
## 🌸Задача №3
Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.  
Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.  
Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.  
Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.  
Прислать список набранных команд и содержимое git log.  
```bash
git init
git config user.name "coder1"
git config user.email "coder1@gmail.com"
echo print("Hello, World!") > prog.py
git add prog.py
git commit -m "first commit"

cd C:\Users\Admin\Desktop\pract4_repo
git init --bare server
git remote add server C:\Users\Admin\Desktop\pract4_repo\server
git remote -v
git push server master

git clone C:\Users\Admin\Desktop\pract4_repo\server C:\Users\Admin\Desktop\pract4_repo\client
cd C:\Users\Admin\Desktop\pract4_repo\client
git config user.name "coder2"
git config user.email "coder2@gmail.com"

echo "Author Information:" > readme.md
git add readme.md
git commit -m "docs"

git remote rename origin server
git push server master

cd C:\Users\Admin\Desktop\pract4_repo
git pull server master

echo "Author: coder1" >> readme.md
git add readme.md
git commit -m "coder1 info"
git push server master

cd C:\Users\Admin\Desktop\pract4_repo\client
echo "Author: coder2" >> readme.md
git add readme.md
git commit -m "coder2 info"
git push server master
git pull server master

git add readme.md
git commit -m "readme fix"
git push server master

cd ..
cd server
git log -n 5 --graph --decorate --all
```
![pract4_10](https://github.com/user-attachments/assets/9ebc1d69-f504-43d8-ba4f-89d9cb28e520)
