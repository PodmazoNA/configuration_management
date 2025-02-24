# Практическая работа №2 :) 
## 🌸Задача №1
```bash
pip show matplotlib
```
## 🌸Задача №2
```bash
npm info express
```
## 🌸Задание №3
```bash
digraph G {
    matplotlib [shape=oval, style=filled, color=yellow];
    node [shape=rect, style=filled, color=orange];

    matplotlib -> "numpy";
    matplotlib -> "pillow";
    matplotlib -> "cycler";
    matplotlib -> "kiwisolver";
    matplotlib -> "pyparsing";
    matplotlib -> "python-dateutil";
}
```
## 🌸Задание №4
```bash
include "alldifferent.mzn";

var 1..9: a1;  
var 0..9: a2; 
var 0..9: a3; 
var 0..9: b1; 
var 0..9: b2;  
var 0..9: b3; 

constraint alldifferent([a1, a2, a3, b1, b2, b3]);
constraint a1 + a2 + a3 = b1 + b2 + b3;
solve minimize a1 + a2 + a3;
```
## 🌸Задание №5
```bash
set of int: menuVer = 1..6;
set of int: dropdownVer = 1..5;
set of int: iconVer = 1..2;

array[menuVer] of int: menu = [150, 140, 130, 120, 110, 100];
array[dropdownVer] of int: dropdown = [230, 220, 210, 200, 180];
array[iconVer] of int: icons = [200, 100];

var menuVer: selected_menu;
var dropdownVer: selected_dropdown;
var iconVer: selected_icons;

constraint
    (selected_menu in 1..5 -> selected_dropdown in 1..4) /\
    (selected_menu = 6 -> selected_dropdown = 5) /\
    (selected_dropdown = 1 -> selected_icons = 1) /\
    (selected_dropdown in 2..5 -> selected_icons in 1..2);

solve satisfy;

output [
    "Your menu version: \(menu[selected_menu])\n",
    "Your dropdown version: \(dropdown[selected_dropdown])\n",
    "Your icon version: \(icons[selected_icons])\n"
];
```
## 🌸Задание №6
```minizinc
include "alldifferent.mzn";

var 1..1: root;
var 1..2: foo;
var 1..2: target;
var 1..2: left;
var 1..2: right;
var 1..2: shared;

constraint (root == 1) -> (foo == 1 /\ target == 2);
constraint (foo == 2) -> (left == 1 /\ right == 1);
constraint (left == 1) -> (shared == 1 \/ shared == 2);
constraint (right == 1) -> (shared == 1);
constraint (shared == 1) -> (target == 1);

solve satisfy;
```
## 🌸Задание №7
```bash
int: num_packages; %число пакетов
set of int: Packages = 1..num_packages;
array[Packages] of var int: selected_version; %выбранные в итоге версии пакетов
array[Packages] of set of int: dependencies; %зависимости пакетов
array[Packages, Packages] of int: min_version; %матрица, показывающая какие минимум версии одних пакетов нужны другим пакетам
array[Packages, Packages] of int: max_version; %матрица, аналогичная первой, только с максимальными версиями

constraint
  forall(i in Packages) (
    forall(dep in dependencies[i]) (
      selected_version[dep] >= min_version[i, dep] /\
      selected_version[dep] <= max_version[i, dep]
    )
  );

solve satisfy;
```
