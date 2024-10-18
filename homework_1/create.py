import os
import tarfile
import sys

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

if __name__ == "__main__":
    create_archive()
