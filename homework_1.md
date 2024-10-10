# Домашняя работа №1
```bash
import os
import shutil
import zipfile
import calendar
from datetime import datetime

def run():
    current_directory = 'archive'
    previos_directory = 'archive'
    while True:
        command = input(f"{current_directory} ")
        if command == "exit":
            break
        if command[:2] == "cd":
            if command[3:] == "/" or command[3:] == "-" or command[3:] == ".." or os.path.isdir(command[3:]):
                result = cd(current_directory, previos_directory, command[3:])
                previos_directory = current_directory
                current_directory = result
            else:
                print(f"sh: cd: can't cd to {command[3:]}: No such file or directory")
        if command[:2] == "ls":
            if len(command) == 2:
                ls(current_directory)
            else:
                try:
                    ls(command[3:])
                except Exception as e:
                    print(f"ls: {command[3:]}: No such file or directory")
        if command[:2] == "cp":
            if os.path.exists(command.split(" ")[1]) and os.path.exists(command.split(" ")[2]):
                cp(command.split(" ")[1], command.split(" ")[2])
            else:
                print("cp: No such file or directory")
        if command[:5] == "rmdir":
            if os.path.isdir(command[6:]) == False:
                print("rmdir: No such directory")
            else:
                try:
                    rmdir(command[6:])
                except Exception as e:
                    print("rmdir: Directory not empty")
        if command[:3] == "cal":
            if len(command.split(" ")) == 1:
                cal(datetime.now().month, datetime.now().year)
            if len(command.split(" ")) == 3:
                cal(int(command.split(" ")[1]), int(command.split(" ")[2]))
            if len(command.split(" ")) == 2:
                for i in range(1, 13):
                    cal(i, int(command.split(" ")[1]))



def create_archive():
    os.makedirs("archive")
    os.makedirs("archive/empty_folder")
    my_file = open("archive/readme.txt" , "w+")
    my_file.write("Why did you open me up, i am just a file...")
    os.makedirs("archive/home")
    my_file = open("archive/home/todolist.txt" , "w+")
    my_file.write("1) noting")
    os.makedirs("archive/home/documents")
    my_file = open("archive/home/documents/document1.txt" , "w+")
    my_file.write("Let's pretend that this is very important information, ok?")
    my_file = open("archive/home/documents/document2.txt" , "w+")
    my_file.write("Let's pretend once again that this is very important information, ok?")
    os.makedirs("archive/files")
    my_file = open("archive/files/hello.py" , "w+")
    my_file.write('print("Hello...")')
    my_file = open("archive/files/world.py" , "w+")
    my_file.write('print("... World")')

def ls(path):
    file_list = os.listdir(path)
    for file in file_list:
        print(file + " ", end='')

def cd(current_directory, previos_directory, path):
    if path == '/': #корневая директория
        return 'archive'
    if path == '-': #предыдущая директория
        return previos_directory
    if path == '..' and current_directory != 'archive': #"верхняя" директория
        return "/".join(current_directory.split("/")[:-1])
    if path == '..' and current_directory == 'archive':
        return 'archive'
    else:
        return path

def cp(current_path_to_file, new_path_to_file):
    shutil.copy(current_path_to_file, new_path_to_file)

def rmdir(path_to_directory):
    os.rmdir(path_to_directory)

def cal(month, year):
    try:
        cal = calendar.TextCalendar()
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)
    except Exception as e:
        print("cal: illegal month value: use 1-12")

create_archive()
run()
```
