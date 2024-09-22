# Практическая работа №1 
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
## 🌸Задача 4
```bash
grep -oE '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | sort -u
```
## 🌸Задача 5
```bash
#!/bin/bash
if [ $# -eq 0 ]; then
        echo "Usage: $0 command_name"
        exit 1
fi
 
COMMAND_NAME=$1
COMMAND_PATH="./$COMMAND_NAME"
 
if [ ! -f "$COMMAND_PATH" ]; then
        echo "Command $COMMAND_NAME not found in the current directory."
        exit 1
fi

chmod +x "$COMMAND_PATH"
cp "$COMMAND_PATH" /usr/local/bin/
echo "Command $COMMAND_NAME registered successfully."
```
## 🌸Задача 6
```bash
#!/bin/bash
if [ $# -ne 1 ]; then
        echo "Usage: $0 command_name"
        exit 1
fi
file=$1
if [ ! -f "$file" ]; then
        echo "File '$file' not found"
        exit 1
fi
case $file in
        *.c)
                first_line=$(head -n 1 "$file")
                if [[ "$first_line" =~ ^\s*// || "$first_line" =~ ^\s*/\* ]]; then
			echo "'$file' has a comment in the first line"  
                else
                        echo "'$file' does not have a comment in the first line"
                fi
                ;;
        *.js)
                first_line=$(head -n 1 "$file")
                if [[ "$first_line" =~ ^\s*// || "$first_line" =~ ^\s*/\* ]]; then
                        echo "'$file' has a comment in the first line"
                else
                        echo "'$file' does not have a comment in the first line"
                fi
                ;;
        *.py)
                first_line=$(head -n 1 "$file")
                if [[ "$first_line" =~ ^\s*# ]]; then
                        echo "'$file' has a comment in the first line"
                else
                        echo "'$file' does not have a comment in the first line"
                fi
                ;;
esac
```
## 🌸Задача 7
```bash
#!/bin/bash
if [ -z "$1" ]; then
        echo "Usage: $0 path_to_directory"
        exit 1
fi
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -dD
```
## 🌸Задача 8
```bash
#!/bin/bash
if [ "$#" -ne 2 ]; then
        echo "Usage: $0 <extension> <archive_name>"
        exit 1
fi
EXTENSION=$1
ARCHIVE_NAME=$2
find . -name "*.$EXTENSION" | xargs tar -cvf "$ARCHIVE_NAME.tar"
echo "Archive has been created"
```
## 🌸Задача 9
```bash
#!/bin/bash
if [ "$#" -ne 2 ]; then
        echo "Usage: $0 <input_file> <output_file>"
        exit 1
fi
INPUT_FILE=$1
OUTPUT_FILE=$2
sed 's/    /\t/g' "$INPUT_FILE" > "$OUTPUT_FILE"
echo "Spaces have been replaced with tabs"
```
## 🌸Задача 10
```bash
#!/bin/bash
if [ "$#" -ne 1 ]; then
        echo "Usage: $0 <directory>"
        exit 1
fi
if [ ! -d "$1" ]; then
        echo "Directory not found"
        exit 1
fi
find "$1" -type f -name "*.txt" -size 0c -print
```
