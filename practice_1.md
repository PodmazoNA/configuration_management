<h1 align="center">Практическая работа 1</h1>
<h2>🌸Задача 1</h2>
cut -d: -f1 /etc/passwd | sort
<h2>🌸Задача 2</h2>
cat /etc/protocols | awk '{print $2, $1}' | sort -n -r | head -n 5
<h2>🌸Задача 3</h2>
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
