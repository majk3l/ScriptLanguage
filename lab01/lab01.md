# Lab #01 - Simple scripts that take arguments from command line

### Exercises:

### 01.1:
Write simple script, that takes following arguments from command-line: two numbers and operator (+, -, *) i does simple arithmetic operations. The script file should be named ```arithmetics.py```. The arguments should be separated by space, like in this example script execution from command line:
```text
python arithmetics.py 2 + 4
6
```

### 01.2:
Write simple script, that counts all the input arguments provided by use have 3 or more characters. The script file should be named ```arguments.py```. The result should be printed out to standard output:
```text
python arguments.py This is test sentence
3
```
Modify this script so, the scripts prints out the selected words (3 or more character) in reversed order:
```text
python arguments.py This is test sentence
3
sentence test This
```
### 01.3:
Write script ```quadratic.py```  that solves quadratic equation. Coefficients (a, b, c) should be taken from command-line. The script should print out:
- first line: number of solutions (2/1/0)
- second line: solutions, if they exist

Example:

```text
python quadratic.py 1 4 3
2
-1.0 -3.0
```
