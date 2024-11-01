# Практическая работа №5
## 🌸Задача №1
Опишите по шагам, что делает каждая из следующих команд (приведите эквивалентное выражение на Python):
```bash
11 0 LOAD_FAST 0 (x) 2 LOAD_CONST 1 (10) 4 BINARY_MULTIPLY 6 LOAD_CONST 2 (42) 8 BINARY_ADD 10 RETURN_VALUE
```
Данный код является байт-кодом для виртуальной машины Python.

1) 11 0 LOAD_FAST 0 (x):  
11 - индекс инструкции в байт-коде  
0 - размер инструкции  
LOAD_FAST 0 (x) - команда, загружающая значение переменной с индексом 0 из локальной области видимости (в данном случае это переменная x)  
  
2) 2 LOAD_CONST 1 (10):  
2 - индекс инструкции в байт-коде  
0 - размер инструкции  
LOAD_CONST 1 (10) - команда, загружающая константу с индексом 1 из константного пула (в данном случае это число 10)  
  
3) 4 BINARY_MULTIPLY:  
4 - индекс инструкции в байт-коде  
0 - размер инструкции  
BINARY_MULTIPLY - команда, производящая умножение двух значений, находящихся на вершине стека  
  
4) 6 LOAD_CONST 2 (42):  
6 - индекс инструкции в байт-коде  
0 - размер инструкции  
LOAD_CONST 2 (42) - команда, загружающая константу с индексом 2 из константного пула (в данном случае это число 42)  
  
5) 8 BINARY_ADD:  
8 - индекс инструкции в байт-коде  
0 - размер инструкции  
BINARY_ADD - команда, производящая сложение двух значений, находящихся на вершине стека  
  
6) 10 RETURN_VALUE:  
10 - индекс инструкции в байт-коде  
0 - размер инструкции  
RETURN_VALUE - команда, возвращающая значение, находящееся на вершине стека, как результат выполнения функции  
  
Таким образом, эквивалентым выражением на Python будет:
```bash
def f(x):
    return x*10+42
```