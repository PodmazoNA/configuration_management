import os
import sys
import tarfile
import csv
import datetime

class ShellEmulator:
  def __init__(self, hostname, tar_path, log_path):
    self.hostname = hostname
    self.tar_path = tar_path
    self.log_path = log_path
    self.current_directory = "/"
    self.virtual_fs = {}
    self.load_filesystem()

  def load_filesystem(self):
    with tarfile.open(self.tar_path, 'r') as tar:
      for member in tar.getmembers():
        self.virtual_fs[member.name] = member
      print(f"Loading virtual file system from {self.tar_path}")

  def log_action(self, action):
    now = datetime.now()
    with open(self.log_path, mode = 'a', newline = '') as log_file:
      log_writer = csv.writer(log_file)
      log_writer = writerow([now.strftime("%Y-%m-%d %H:%M:%S"), action])

  def ls(self):
    items = [name for name in self.virtual_fs.keys() if name.startswith(self.current_directory) and name != self.current_directory]
    items = [os.path.basename(item) for item in items]
    print(" ".join(items))
    self.log_action("ls")

  def cd(self, path):
    if path in self.virtual_fs:
      self.current_directory = path
    else:
      print(f"cd: no such file or directory: {path}")
    self.log_action(f"cd {path}")

  def exit(self):
    self.log_action("exit")
    print("Exiting shell...")
    sys.exit(0)

  def cal(self): #ох, ох, ох
    
    self.log_action("cal")

  def cp(self, src, dest):
    if src in self.virtual_fs:
      self.virtual_fs[dest] = self.virtual_fs[src]
      print(f"Copied {src} to {dest}")
      self.log_action(f"cp {src} {dest}")
    else:
      print(f"cp: source file does not exist: {src}")
