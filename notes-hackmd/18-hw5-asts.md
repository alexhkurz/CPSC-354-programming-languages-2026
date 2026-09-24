---
tags: programming languages
---

# Homework 5 (abstract syntax trees)

In [Programming Assignment 1](https://hackmd.io/@alexhkurz/HJIOalf5fg) you extend the calculator from hw4 by new operations. This homework prepares you for this by thinking about the abstract syntax trees (ASTs) that your calculator will produce.

Recall that concrete syntax is a string such as `1+2*3` whereas the corresponding abstract syntax is a tree. In the [reference implementation](https://codeberg.org/alexhkurz/calculator-2024) (see `CalcTransformer` in `calculator.py`), ASTs are written in Python notation as nested tuples. For example, the AST of `1+2*3` is

```python
('plus', ('num', 1), ('times', ('num', 2), ('num', 3)))
```

## Examples: The ASTs of the hw4 strings

For reference, here are the ASTs of the strings from hw4 in the Python notation:

- `2+1`

    ```python
    ('plus', ('num', 2), ('num', 1))
    ```

- `1+2*3`

    ```python
    ('plus', ('num', 1), ('times', ('num', 2), ('num', 3)))
    ```

- `1+(2*3)`

    ```python
    ('plus', ('num', 1), ('times', ('num', 2), ('num', 3)))
    ```

- `(1+2)*3`

    ```python
    ('times', ('plus', ('num', 1), ('num', 2)), ('num', 3))
    ```

- `1+2*3+4*5+6`

    ```python
    ('plus', ('plus', ('plus', ('num', 1), ('times', ('num', 2), ('num', 3))), ('times', ('num', 4), ('num', 5))), ('num', 6))
    ```

Note that `1+2*3` and `1+(2*3)` have the same AST: parentheses are part of the concrete syntax and do not appear in the abstract syntax.

## Homework (preparation for Quiz 5 and PA1)

The grammar of PA1 extends the hw4 grammar by subtraction, unary minus, exponentiation, and logarithm:

```
exp -> exp '+' exp
exp -> exp '*' exp
exp -> exp '^' exp
exp -> exp '-' exp
exp -> '-' exp 
exp -> 'log' exp 'base' exp
exp -> '(' exp ')'
exp -> number
```

For each of the following strings, write the AST in the Python notation. You will have to invent suitable constructors for the new operations (for example `'minus'`, `'neg'`, `'pow'`, `'log'`). The AST should reflect the order of operations required by the PA1 test cases.

- `2-(4+2)`
- `--1`
- `2^3^2`
- `log 8 base 2 + 1`
- `-3^2`
