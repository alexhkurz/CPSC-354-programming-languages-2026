---
tags: programming languages
---

# Programming Assignment 2

The aim of this assignment is to understand and modify a Python interpreter for the untyped lambda calculus.

The starter repository [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024) already parses lambda terms (via Lark), builds an AST, and implements capture-avoiding substitution and evaluation. Your task is to explore that code with tests and the debugger, then change the evaluator so that it matches the intended operational behaviour on the provided tests.

Work through the lab note [Lambda Calculus in Python](https://hackmd.io/@alexhkurz/B1FMhwc1bg). Homework [hw10](hw10.md) is preparation for the same AST and substitution ideas.

## Deliverables

- You can work in groups of 2 people. Use the same private GitHub repo as for Programming Assignment 1 (invite your instructor as a collaborator if you have not already).

- In that repo, create a subdirectory `Assignment2`. Inside that, create the following files (do not change the specified names):

	```
	Assignment2
	    interpreter.py
	    grammar.lark
	```

- Start from a copy of [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024). Keep `grammar.lark` as in the starter (do not modify it for the required work). Put your modified evaluator in `interpreter.py`.

## What to do

Follow the numbered exercises in [Lambda Calculus in Python](https://hackmd.io/@alexhkurz/B1FMhwc1bg):

0. Clone or copy [lambdaC-2024](https://codeberg.org/alexhkurz/lambdaC-2024) and install as in its README (`source setup.sh`).
Exercise 1–5. Test the starter interpreter; investigate capture-avoiding substitution; find a minimal expression that should but does not reduce to normal form.
1. Use the VS Code / Cursor debugger (practice only).
Exercise 7–8. Produce the substitution trace and the recursive `evaluate` / `substitute` trace asked for in the lab.
1. Modify `interpreter.py` so the interpreter behaves as intended on your MWE and on the automated tests below.

Setup tip from the lab: open the folder that contains `interpreter.py` as the workspace, and use the provided `.vscode/launch.json` if debugging is awkward.

## Grading guidelines

- The grade is based on automated input/output tests of `interpreter.py`.
- Stick to the naming conventions above; automated tests look for `interpreter.py` together with an unmodified `grammar.lark`.
- The interpreter must accept a program from the command line and print **only** the result (no extra logging), as in the starter:

	```
	python interpreter.py "(\x.x) a"
	a
	```

- We reserve the right to add further test cases beyond the sample list below.

## Testing

Sample tests for item 9 live in the starter as [`testing-data.txt`](https://codeberg.org/alexhkurz/lambdaC-2024/src/branch/main/testing-data.txt). You can run them with [`testing4b.py`](https://codeberg.org/alexhkurz/lambdaC-2024/src/branch/main/testing4b.py) from the same directory and inspect `interpreter.py.txt`.

Representative cases (fresh names such as `Var9` may differ up to renaming):

```
python interpreter.py "(\x.x) a"
a
```

```
python interpreter.py "(\x.\y.x) a b"
a
```

```
python interpreter.py "(\m.\n.\f.\x. m f (n f x)) (\f.\x. f (f x)) (\f.\x.f (f (f x)))"
(\Var9.(\Var11.(Var9 (Var9 (Var9 (Var9 (Var9 Var11)))))))
```

```
python interpreter.py "(\m.\n.\f.\x. m (n f) x) (\f.\x. f (f x)) (\f.\x.f (f (f x)))"
(\Var9.(\Var11.(Var9 (Var9 (Var9 (Var9 (Var9 (Var9 Var11))))))))
```

```
python interpreter.py "((\m.\n.m n)(\f.\x.f(f x)))(\f.\x.f(f(f x)))"
(\Var3.(\Var4.(Var3 (Var3 (Var3 (Var3 (Var3 (Var3 (Var3 (Var3 (Var3 Var4)))))))))))
```

Do not limit your own testing to these cases. Use `interpreter_test.py` and your own entries in `test.lc` while you explore.

## Deadline

**Week 12, Sunday, Nov 15, 11:59 PM** .
