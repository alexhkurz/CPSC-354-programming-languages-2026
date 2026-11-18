---
tags: programming languages
---

# Programming Assignment 3

The aim of this assignment is to put together what we learned from the calculator and the $\lambda$-calculus to create a small functional programming language.

For example, insertion sort on the list `4,3,2,1` should look like this (details of surface syntax may vary slightly as you fix precedence):

```
letrec insert = \x.\xs.
   if xs == # then
     x : #
   else if (x <= (hd xs)) then
     x : xs
   else
     (hd xs) : (insert x (tl xs))
 in
 letrec sort = \xs.
   if xs == # then
     #
   else
     insert (hd xs) (sort (tl xs))
 in
 sort (4 : 3 : 2 : 1 : #)
```

The template repository [lambdaF-2024](https://codeberg.org/alexhkurz/lambdaF-2024) is a lightly modified copy of [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024): comments use `//` instead of `--`, so arithmetic can use double minus. Use the lambdaF template, not your PA2 solution or lambdaC.

There is **one submission** at the end: a single `Assignment3` folder that implements the full language. The three parts below are a recommended order of work (add features incrementally, with tests at each step). You do not submit separate milestones.

## Deliverables

- Work in groups of 2 people. Use the same private GitHub repo as for Programming Assignments 1 and 2 (invite your instructor as a collaborator if you have not already).

- In that repo, create a subdirectory `Assignment3`. Inside that, create the following files (do not change the specified names):

	```
	Assignment3
	    interpreter.py
	    grammar.lark
	    interpreter_test.py
	```

- Copy the [lambdaF-2024](https://codeberg.org/alexhkurz/lambdaF-2024) template into `Assignment3`. Extend `grammar.lark` and `interpreter.py` for the language specified below. Keep adding your own tests in `interpreter_test.py`.

## What to do

Install as in the template README (`source setup.sh`). 

Check that the install works by running `python interpreter.py "(\x.x) a"` (should print `a`) and `python interpreter.py test.lc` (should print `b`).

Open the folder that contains `interpreter.py` as the workspace if you use the debugger.

For each new grammar rule, add a clause in `LambdaCalculusTransformer`, `evaluate`, `substitute`, and `linearize`. Only `evaluate` does real work; the other three are boilerplate. Add features one at a time and run tests after each change.

A workable order:

1. Add one arithmetic operation to the grammar; update Transformer / `substitute` / `linearize`; implement it in `evaluate`; add tests.
2. Continue until Part 1 tests pass.
3. Add conditionals, comparisons, `let`, `letrec`, and `fix` (Part 2).
4. Add sequencing and lists (Part 3), until the example programs below run.

Use the debugger and make MWEs when something goes wrong. Construct tests for pairs of operations to check order of operations. Ideally, for any two operations `A` and `B`, you have cases with `A` outside `B` and with `B` outside `A`.

## Language specification

The target language[^ocaml] is given by this ambiguous CFG (you must disambiguate it in `grammar.lark` so that the tests below parse as intended):

[^ocaml]: The syntax is loosely inspired by the [programming language OCaml](https://ocaml.org/manual/5.3/language.html).

```
lam.        exp -> "\" NAME "." exp
app.        exp -> exp exp
plus.       exp -> exp "+" exp
minus.      exp -> exp "-" exp
times.      exp -> exp "*" exp
neg.        exp -> "-" exp
if.         exp -> "if" exp "then" exp "else" exp
leq.        exp -> exp "<=" exp
eq.         exp -> exp "==" exp
let.        exp -> "let" NAME "=" exp "in" exp
rec.        exp -> "letrec" NAME "=" exp "in" exp
fix.        exp -> "fix" exp
num.        exp -> NUMBER
var.        exp -> NAME
paren.      exp -> "(" exp ")"
prog.       exp -> exp ";;" exp
hd.         exp -> "hd" exp
tl.         exp -> "tl" exp
nil.        exp -> "#"
cons.       exp -> exp ":" exp
```

Fixing precedence needs experimentation. Sequencing (`;;`) has the lowest precedence; list constructors have high precedence. Comments start with `//` (not `--`).

### Evaluation strategy

The interpreter, like [Haskell](https://www.haskell.org/), is lazy: it does not reduce under a lambda, and arguments are not evaluated when substituted ([call-by-name, not call-by-value](https://en.wikipedia.org/wiki/Evaluation_strategy)):

```
\x.(\y.y)x                   -->   (\x.((\y.y) x))
(\x.a x) ((\x.x)b)           -->   (a ((\x.x) b))
```

### Arithmetic (Part 1)

```
(\x.x) (1--2)                -->    3.0
(\x.x) (1---2)               -->   -1.0
(\x.x + 1) 5                 -->    6.0
(\x.x * x) 3                 -->    9.0
(\x.\y.x + y) 3 4            -->    7.0
1-2*3-4                      -->   -9.0
(\x.x * x) 2 * 3             -->   12.0
(\x.x * x) (-2) * (-3)       -->   -12.0
((\x.x * x) (-2)) * (-3)     -->   -12.0
(\x.x) (---2)                -->   -2.0
```

Unusual inputs may yield unusual results, as long as the required cases above hold. For example the following are acceptable:

```
(\x.x * x) -2 * -3         -->  ((\x.(x * x)) - -6.0)
((\x.x * x) -2) * -3       -->  (((\x.(x * x)) - 2.0) * -3.0)
(\x.x) ---2                -->  ((\x.x) - 2.0)
```

### Conditionals, bindings, and fix (Part 2)

Computation rules (see also the lecture on the [Fixed Point Combinator](https://hackmd.io/@alexhkurz/Hk-hjD51bl)):

```
fix F --> F (fix F)
let x = e1 in e2 --> (\x.e2) e1
letrec f = e1 in e2 --> let f = (fix (\f. e1)) in e2
```

`0` encodes false and `1` encodes true. Use Python’s conditional for `if`, and Python’s comparisons for `<=` and `==`.

```
if 0 then A else B --> A
if 1 then A else B --> B
```

Sample cases:

```
if 0 then 2 else 1
--> 1.0

if 1 then 2 else 2
--> 2.0

if 0 then 2 else if 1 then 3 else 4
--> 3.0

if 0 then 2 else if 0 then 3 else 4
--> 4.0

if 0 == 0 then 5 else 6
--> 5.0

if 0 <= 1 then 6 else 7
--> 6.0

if 1 <= 0 then 6 else 7
--> 7.0

let x = 1 in if x == 1 then 8 else 9
--> 8.0

let x = 0 in if x == 1 then 8 else 9
--> 9.0

let f = \x.x in f 10
--> 10.0

let f = \x.x+1 in f 10
--> 11.0

let f = \x.x*6 in let g = \x.x+1 in f (g 1)
--> 12.0

let f = \x.x*6 in let g = \x.x+1 in g (f 2)
--> 13.0

let f = \x.x*6 in let f = \x.x+1 in f (f 2) + 10
--> 14.0

letrec f = \n. if n==0 then 1 else n*f(n-1) in f 4
--> 24.0

letrec f = \n. if n==0 then 0 else 1 + 2*(n-1) + f(n-1) in f 6
--> 36.0
```

Carry the Part 1 tests forward; they should keep working.

### Sequencing and lists (Part 3)

Constructors `#` (nil) and `:` (cons) build lists; they have no computation rules of their own. Destructors:

```
hd a:b    -->    a
tl a:b    -->    b
```

Sequential composition `;;` is only allowed at the top level (no nesting such as `let x = 2 in (x ;; x+1)`). Use lists if you need several values in one expression.

Sample cases:

```
1 ;; 2
--> 1.0 ;; 2.0

1 ;; 2 ;; 3
--> 1.0 ;; 2.0 ;; 3.0

1+1 ;; (\x.x)a ;; (\x.x+x)2
--> 2.0 ;; a ;; 4.0

#
--> #

1:2:3:#
--> (1.0 : (2.0 : (3.0 : #)))

(\x.x) #
--> #

(\x.\y.x) 1:# a
--> (1.0 : #)

(\x.\y.y) a 1:#
--> (1.0 : #)

let f = \x.x+1 in (f 1) : (f 2) : (f 3) : #
--> (2.0 : (3.0 : (4.0 : #)))

1:2 == 1:2
--> 1.0

1:2 == 1:3
--> 0.0

1:2:# == 1:2:#
--> 1.0

(1-2) : (2+2) : # == (-1):4:#
--> 1.0

hd (1:2:#)
--> 1.0

hd 1:2:#
--> 1.0

tl (1:2:#)
--> (2.0 : #)

tl 1:2:#
--> (2.0 : #)

letrec map = \f. \xs. if xs==# then # else (f (hd xs)) : (map f (tl xs)) in (map (\x.x+1) (1:2:3:#))
--> (2.0 : (3.0 : (4.0 : #)))
```

Again, keep the earlier tests working.

### Example programs

If you save the following as `test.lc` 

```
letrec f = \x. if x==0 then 1 else x * f(x-1) in f 5

;;

letrec fib = \ n.
    if n==0 then 0 else
        if n==1 then 1 else
            fib(n-2)+fib(n-1)
in
fib 10

;;

letrec insert = \x.\xs.
  if xs == # then
    x : #
  else if (x <= (hd xs)) then
    x : xs
  else
    (hd xs) : (insert x (tl xs))
in
letrec sort = \xs.
  if xs == # then
    #
  else
    insert (hd xs) (sort (tl xs))
in
sort (5 : 3 : 4 : 3 : 1 : #)
```
and run `python interpreter.py test.lc`, you should get

```
120.0 ;; 55.0 ;; (1.0 : (3.0 : (3.0 : (4.0 : (5.0 : #)))))
```

## Grading guidelines

- There is one graded submission: the final `Assignment3` interpreter. The grade is based on automated input/output tests covering Parts 1–3. There is no write-up.
- Stick to the naming conventions above.
- The interpreter must accept a program from the command line (or a `.lc` file) and print **only** the result (no extra logging) as, for example, in:

	```
	python interpreter.py "(\x.x + 1) 5"
	6.0
	```
- We reserve the right to add further test cases beyond the samples above.
- Partial implementations receive partial credit according to how much of Parts 1–3 they pass. A program that does not run receives no credit by default.

For automated testing you may download [`testing4b.py`](https://codeberg.org/alexhkurz/testing-python-programs/src/branch/main/testing4b.py). The template includes [`testing-data-M1.txt`](https://codeberg.org/alexhkurz/lambdaF-2024/src/branch/main/testing-data-M1.txt) for Part 1; rename it to `testing-data.txt` to run the script. Extend that file with the Part 2 and Part 3 cases as you go.

If you run into technical troubles with the Python scripts, ask on Discord.

## Deadline

**Finals week** (one submission; see Canvas for the exact datetime).
