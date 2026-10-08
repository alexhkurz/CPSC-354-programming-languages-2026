# CPSC-354 2025: Assignment 3

- **Github**: https://codeberg.org/alexhkurz/lambdaF-2024
- Milestone 1: see below.
- [Milestone 2](https://hackmd.io/@jweinberger/rJzMHEM-Zx)
- [Milestone 3](https://hackmd.io/@jweinberger/rk0EG_Qb-e)


**Aim:** The purpose of the project is to put together what we learned from the calculator and $\lambda$-calculus to create a small functional programming language.

For example, using insertion sort to sort the list `4,3,2,1` will look like this (details may change):

```
letrec insert = \x.\xs.
   if xs = # then
     x : #
   else if (x <= (hd xs)) = 1 then
     x : xs
   else
     (hd xs) : (insert x (tl xs))
 in
 letrec sort = \xs.
   if xs = # then
     #
   else
     insert (hd xs) (sort (tl xs))
 in
 sort (4 : 3 : 2 : 1 : #)
 ```

We split the project into several *milestones*. We recommend you follow their sequence, but we are also happy about other suggestions or feedback.

**Milestones:**

- M1: lambda calculus + arithmetic
- M2: ... + conditionals + `let` + `let rec` 
- M3: ... + lists (`#`, `:`, `hd`, `tl`) 

## Milestone 1

### Specification

The **ambiguous** CFG is:

```
lam     	exp -> "\" NAME "." exp
app     	exp -> exp exp
var     	exp -> NAME
plus    	exp -> exp "+" exp
times   	exp -> exp "*" exp
minus   	exp -> exp "-" exp
neg     	exp -> "-" exp
num     	exp -> NUMBER
```

To fix an order of precedence is a subtle task which requires experimentation and compromise. We want you to come up with an  order of operations that allows to drop parentheses as specified in the file `testing-data-M1.txt` and repeated here. [^testing]

[^testing]: (The file `testing-data-M1.txt` is for automated testing, otherwise use `test.lc` or `interpreter_test.py`).

First, our interpreter, like the one of Haskell, **follows an evaluation strategy called "lazy"**. This means that it does not "reduce under a lambda" and that arguments are not evaluated when substituted (call-by-name, not call-by-value): [^lambda]
```
\x.(\y.y)x                   -->   (\x.((\y.y) x))
(\x.a x) ((\x.x)b)           -->   (a ((\x.x) b))
```

[^lambda]: This is already implemented by the interpreter.

[^grammar]: For these tests to succeed, you have to change the grammar and the interpreter.

Otherwise we have the following expected reductions: [^grammar]
```
(\x.x) (1--2)                -->    3.0
(\x.x) (1---2)               -->   -1.0
(\x.x + 1) 5                 -->    6.0
(\x.x * x) 3                 -->    9.0
(\x.\y.x + y) 3 4            -->    7.0
```
```
1-2*3-4                      -->   -9.0
(\x.x * x) 2 * 3             -->   12.0
(\x.x * x) (-2) * (-3)       -->   -12.0
((\x.x * x) (-2)) * (-3)     -->   -12.0
(\x.x) (---2)                -->   -2.0
```


This specification aligns with common usage in functional programming languages, see the following links for [Lean](https://live.lean-lang.org/#codez=MQUwbghgNgBAjAOgAwwLQwEzJgKhgZm3QBZkAoUSWACgDMBXAOxgA8YBeAPld1YEpMvfBXDQYdJjy488LAdVQYBeBfj4iq4iczbS2s+Yr7LxqNRrHap3OaYUKlxshZoMdHG71uLeZl1rdrGX40JV9hSktA3RsBVHiMfysYkNR7I3UgA). Many imperative languages also have similar conventions, see eg the code examples in [Python](https://www.online-python.com/L1ldqtJPNK), [Javascript](https://playcode.io/2132373). 

To keep things simple, you are allowed to return unusual results to unusual inputs as long as the above list of requirements is met. For example, our implementation yields[^ast] [^typechecking]

```
(\x.x * x) -2 * -3         -->  ((\x.(x * x)) - -6.0)
((\x.x * x) -2) * -3       -->  (((\x.(x * x)) - 2.0) * -3.0)
(\x.x) ---2                -->  ((\x.x) - 2.0)
```



### Details

Work in the same groups and the same shared repository as previously.

#### Required Files

Your repository will contain (at least) the following.


```
README.md
Assignment1
    ...
Assignment2
    ...
Assignment3
    interpreter.py
    grammar.lark
    interpreter_test.py
```

#### Grammar

In our experience most of the work for M1 will go into encoding the correct order of operations in the grammar rules. Add them one by one, running tests each time. Construct tests for any pair of operations to test order of operations.

Minor comment: We changed comments from `--` to `//` (to not conflict with arithmetic).

#### Interpreter

For each new rule you add to your grammar you need to add a clause in `LambdaCalculusTransformer`, `evaluate`, `substitute`, and `linearize`. 

Only `evaluate` is doing real work, the other three are "boilerplate". (Remember that LLMs can be very good at providing boilerplate code.)

For `evaluate` you do not need to change the implementation of `app` but you need to add clauses for each operation you add to the grammar.

#### Testing

Add your own tests to `interpreter_test.py`. Highlight your new tests in color blue. **Choice of relevant testcases will be taken into account for grading.**

To make sure that your program passes our automated testing, you may download [testing4b.py](https://codeberg.org/alexhkurz/testing-python-programs/src/branch/main/testing4b.py), rename `testing-data-M1.txt` to `testing-data.txt` and run `python testing4b.py`. 

**If you run into technical troubles related to running the Python scripts etc., please refer to the `#technical-troubleshooting` on our Discord server.**


### Tips

* The following steps may work well.
    1. Add one new arithmetic operation to the lambda-calculus grammar.
    1. Run `interpreter_test.py` (should still work).
    1. Change `LambdaCalculusTransformer`,  `substitute`, and `linearize`. `interpreter_test.py` should still pass all tests.
    1. Add an implementation of the new operation to `evaluate`. Add test cases for the new operation to `interpreter_test.py`. 
    1. Test and debug.
    1. Go back to 1.
* Make use of the debugger.
* Come up with MWEs for your tests if sth goes wrong.
  

[^ast]: Which ASTs explain these results?

[^typechecking]: A typechecker would reject an expression such as `(\x.x) - 2.0`, but, due to lack of time, we do not implement a type checker in this course. This would be part of a follow-up course on compiler construction.
