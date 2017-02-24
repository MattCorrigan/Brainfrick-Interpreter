# Brainfrick-Interpreter
A simple interpreter for the Brain**** language, which is Turing complete.

# Overview of the Language
This language, which I will call Brainfrick from now on, uses symbols to run commands. The program has a set of cells, each of which can hold one byte of data. There is also a data pointer that points to the current data cell. Here is a description of each of the eight symbols:

**+** is used to increase the current byte by one.

**-** is used to decrease the current byte by one.

**>** is used to move the data pointer to the cell on the right.

**<** is used to move the data pointer to the cell on the left.

**.** is used to print the current byte.

**,** is used to read in one byte from stdin.

**[** is used as an opening while loop. The program skips this character if the current byte is not zero, continuing into the while loop. If it is zero, then the program skips ahead to the *matching* closing bracket.

**]** is used as the closing bracket of the while loop. The program goes back to the *matching* opening bracket if the current byte is not zero. If the current byte is zero, then the program effectively breaks out of the while loop by skipping this symbol.

# Example

Hello World:
```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```
*"But wait, I thought hello world examples were supposed to be simple?"*

