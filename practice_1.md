# Практическая работа №1.
## 🌸Задача №1
```bash
cut -d: -f1 /etc/passwd | sort
```
## 🌸Задача 2
```bash
cat /etc/protocols | awk '{print $2, $1}' | sort -n -r | head -n 5
```
## 🌸Задача 3
