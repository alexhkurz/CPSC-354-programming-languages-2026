---
tags: programming languages
---

# HW5 solutions: abstract syntax trees

The format follows the homework: each string is written as a nested Python tuple, in the same style as the reference calculator (`CalcTransformer` in `calculator.py`). Parentheses from the concrete syntax do not appear in the tree.

Constructors for the new operations are `'minus'` (binary subtraction), `'neg'` (unary minus), `'pow'` (exponentiation), and `'log'` (logarithm). In `('log', x, b)` the first child is the argument and the second is the base.

The shape of each tree is the one required by the PA1 test cases, which fix this order of operations, from loosest to tightest:

1. `+` and binary `-`, both associating to the left
2. `*`
3. unary `-`
4. `^`, associating to the right
5. `log ... base ...`, then parentheses and numbers

## Expression: `2-(4+2)`

PA1 evaluates this to `-4`.

```python
('minus', ('num', 2), ('plus', ('num', 4), ('num', 2)))
```

The parentheses force `4+2` to be computed before the subtraction. They do not appear as a node; they only decide that `plus` is the right child of `minus`.

## Expression: `--1`

PA1 evaluates this to `1`.

```python
('neg', ('neg', ('num', 1)))
```

Each `-` is unary: nothing stands to the left of either of them, so the constructor is `'neg'` and not `'minus'`. Applying unary minus twice returns the original number.

## Expression: `2^3^2`

PA1 evaluates this to `512`.

```python
('pow', ('num', 2), ('pow', ('num', 3), ('num', 2)))
```

Exponentiation associates to the right, so the string is read as `2^(3^2)`. That is `2^9 = 512`. The other grouping, `(2^3)^2`, would be `64`, and the corresponding tree would have the inner `pow` on the left.

## Expression: `log 8 base 2 + 1`

PA1 evaluates this to `4`.

```python
('plus', ('log', ('num', 8), ('num', 2)), ('num', 1))
```

`log ... base ...` binds more tightly than `+`, so the string is `(log 8 base 2) + 1`. Since `log` base `2` of `8` is `3`, the sum is `4`. The other reading, `log` base `(2+1)` of `8`, is not an integer and is not what the test expects.

## Expression: `-3^2`

PA1 evaluates this to `-9`.

```python
('neg', ('pow', ('num', 3), ('num', 2)))
```

`^` binds more tightly than unary minus, so the string is `-(3^2)`, which is `-9`. The other reading, `(-3)^2`, would be `9`, and the corresponding tree would have `'neg'` as the left child of `'pow'`.
