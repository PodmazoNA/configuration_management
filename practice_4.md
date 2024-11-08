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
