# Домашняя работа №1
```bash
import os
import shutil
import zipfile
import calendar
from datetime import datetime
import tarfile

def run():
    current_directory = 'archive'
    previos_directory = 'archive'
    while True:
        command = input(f"{current_directory} ")
        if command == "exit":
            break
        if command[:2] == "cd":
            result = cd(current_directory, previos_directory, command[3:])
            previos_directory = current_directory
            current_directory = result
        if command[:2] == "ls":
            if len(command) == 2:
                ls(current_directory)
            else:
                try:
                    ls(command[3:])
                except Exception as e:
                    print(f"ls: {command[3:]}: No such file or directory")
        if command[:2] == "cp":
            try:
                arr = command.split()
                cp(arr[1], arr[2])
            except Exception as e:
                print("cp: No such file or directory")
        if command[:5] == "rmdir":
            rmdir(command[6:])
        if command[:3] == "cal":
            if len(command.split(" ")) == 1:
                cal(datetime.now().month, datetime.now().year)
            if len(command.split(" ")) == 3:
                cal(int(command.split(" ")[1]), int(command.split(" ")[2]))
            if len(command.split(" ")) == 2:
                for i in range(1, 13):
                    cal(i, int(command.split(" ")[1]))



def create_archive():
    file = tarfile.open("archive.tar", "w")
    os.makedirs("empty_folder")
    my_file = open("readme.txt" , "w+")
    my_file.write("Why did you open me up, i am just a file...")
    os.makedirs("home")
    my_file = open("home/todolist.txt" , "w+")
    my_file.write("1) noting")
    os.makedirs("home/documents")
    my_file = open("home/documents/document1.txt" , "w+")
    my_file.write("Let's pretend that this is very important information, ok?")
    my_file = open("home/documents/document2.txt" , "w+")
    my_file.write("Let's pretend once again that this is very important information, ok?")
    os.makedirs("files")
    my_file = open("files/hello.py" , "w+")
    my_file.write('print("Hello...")')
    my_file = open("files/world.py" , "w+")
    my_file.write('print("... World")')
    file.add("empty_folder")
    file.add("readme.txt")
    file.add("home")
    file.add("files")
    file.close()

def ls(path):
    i = 0
    arr = []
    if path[:7] == "archive":
        with tarfile.open("archive.tar", "r") as tar:
            for member in tar.getmembers():
                if(path == "archive"):
                    i = 1
                    arr.append(member.name.split('/')[0])
                if(path != "archive" and member.name.startswith(path[8:] + "/")):
                    i = 2
                    arr.append(member.name)
    if len(arr) != 0:
        if i == 1:
            print(arr[0] + " ")
            for j in range(1, len(arr)):
                if arr[j-1] != arr[j]:
                    print(arr[j] + " ")
        if i == 2:
            num = path.count("/")
            str1 = arr[0].split("/")[num]
            print(str1)
            for j in range(1, len(arr)):
                if str1 != arr[j].split("/")[num]:
                    str1 = arr[j].split("/")[num]
                    print(str1)
    if i == 0:
        print(f"ls: {path}: No such file or directory")

def cd(current_directory, previos_directory, path):
    i = 0
    if path == '/': #корневая директория
        return 'archive'
    if path == '-': #предыдущая директория
        return previos_directory
    if path == '..' and current_directory != 'archive': #"верхняя" директория
        return "/".join(current_directory.split("/")[:-1])
    if path == '..' and current_directory == 'archive':
        return 'archive'
    else:
        with tarfile.open('archive.tar', 'r') as tar:
            for member in tar.getmembers():
                if member.name.startswith(path[8:] + '/'):
                    i = 1
        if i == 0:
            print(f"sh: cd: can't cd to {path}: No such file or directory")
            return current_directory
        else:
            return path

def cp(current_path_to_file, new_path_to_file):
    i = 0
    with tarfile.open('archive.tar', 'r') as tar:
        with tarfile.open('temp.tar', 'w') as temp_tar:
            for member in tar.getmembers():
                temp_tar.addfile(member, tar.extractfile(member))
                if member.name.startswith(current_path_to_file[8:]):
                    i = 1
                    member.name = new_path_to_file[8:]
                    temp_tar.addfile(member, tar.extractfile(member))
            temp_tar.close()
        tar.close()
    
    with tarfile.open('temp.tar', 'r') as temp_ttar:
        with tarfile.open('archive.tar', 'w') as ttar:
            for member in temp_ttar.getmembers():
                ttar.addfile(member, temp_ttar.extractfile(member))
            ttar.close()
        temp_ttar.close()
    os.remove('temp.tar')
    if i == 0:
        print("cp: No such file or directory")
        return

def isDirEmpty(tar, member):
    for inner_member in tar.getmembers():
        if inner_member.name.startswith(member.name) and inner_member.name != member.name:
            return False
    return True

def rmdir(path_to_directory):
    i = 0
    with tarfile.open('archive.tar', 'r') as tar:
        with tarfile.open('temp.tar', 'w') as temp_tar:
            for member in tar.getmembers():
                if member.name.startswith(path_to_directory[8:]):
                    i = 1
                    if not isDirEmpty(tar, member):
                        print("rmdir: Directory not empty")
                        return
                if member.name != path_to_directory[8:]:
                    temp_tar.addfile(member, tar.extractfile(member))
            temp_tar.close()
        tar.close()
    with tarfile.open('temp.tar', 'r') as temp_ttar:
        with tarfile.open('archive.tar', 'w') as ttar:
            for member in temp_ttar.getmembers():
                ttar.addfile(member, temp_ttar.extractfile(member))
            ttar.close()
        temp_ttar.close()
    os.remove('temp.tar')
    if i == 0:
        print("rmdir: No such directory")
        return

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
