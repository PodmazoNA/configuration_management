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
```bash
#!/bin/bash

if [ $# -eq 0 ]; then
        echo "Usage: $0 your_text"
        exit 1
fi

TEXT="$1"
LENGTH=${#TEXT}
BORDER_LENGTH=$((LENGTH + 2))
 
printf '+'
for ((i=0; i < BORDER_LENGTH; i++)); do
        printf '-'
done
printf '+\n| '
printf "$TEXT"
printf ' |\n+'
for ((i=0; i < BORDER_LENGTH; i++)); do
        printf '-'
done
printf '+\n'

```
