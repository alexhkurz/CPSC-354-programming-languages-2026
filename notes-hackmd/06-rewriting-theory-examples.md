---
tags: programming languages
---

# Rewriting Theory: Examples

We will cover a lot of ground in this course, including:

- functional programming
- pattern matching
- recursion over algebraic data types
- context-free grammars and parsing
- lambda calculus
- how to implement a simple interpreter

In particular, we will learn how to write intepreters for simple programming languages that have arithmetic expressions (calculator) and functions (lambda-calculus).

Underlying all of this is the idea of computation as equational reasoning, as evaluation of expressions. Over the next couple of weeks we will have a closer look at this model of computation.

Apart from providing a foundation for computing, another reason to study rewriting as a model of computation is that it can be instantiated at various levels of abstraction, from hardware via algorithms and programming languages to high-level software engineering. 

Some knowledge of rewriting will come in useful in all areas of computing.

Let us review some examples.

## High School Algebra

Much of high school algebra can be summarised by the equations

\begin{align}
0+x &= x \\
x+(y+z) &= (x+y)+z \\
y+x &= x+y \\
x+(-x) & = 0\\
1\cdot x & = x\\
x\cdot(y\cdot z) &= (x\cdot y)\cdot z \\
y\cdot x &= x\cdot y \\
x\cdot x^{-1} & = 1\\
x\cdot (y+z) & = x\cdot y + x\cdot z 
\end{align}

and much of what you did in high school math came down to rewriting various mathematical expressions according to these equations.

**Exercise/Activity:** Can one turn the equations into an algorithm that decides when two expressions are equal? [^hsa]

[^hsa]: Tip: Decide equality by rewriting to normal form. What should be the normal forms here? 

## Functional Programming

One way to advertise functional programming is that it has a simple computational model consisting of rewriting mathematical equations. The following delve deeper into this:

- Lecture: [A Model of Computation Based on Equational Reasoning](https://hackmd.io/@alexhkurz/Sy_uAuaTh)
- Videos: 
  - [The computational model of functional programming](https://youtu.be/u_OMwv8tDVg)
  - [Haskell Tips I (Recursion)](https://youtu.be/wj0j2HjMw6w)
  - [Recursion over algebraic data types in Haskell](https://youtu.be/2YLfJvOtLwA)
  - [The call stack or what is difficult about recursion](https://hackmd.io/@alexhkurz/HJiulVg0U)

We will practice this model of computation in many of the homework and quiz assignments.

## A Calculator 

If we run a program on our computer it is impossible for us to understand what exactly is going on in our machine. There are too many complicated mechanism involved: the compiler, CPU, Cache, memory management, etc. 

Therefore, we need a **model of computation**, or a **virtual machine**, that allows us to execute programs on a higher level of abstraction.

For example, evaluating arithmetic expressions in successor numbers, we get a simple recursively defined algorithm that gives us a full specification (and implementation) of a calculator that does not depend on any machine specific knowledge. 

The following code is in Haskell. You can [run the Haskell code here](https://code.world/haskell#PUjDAQy_J_3DKPH5L34zNNA). It follows the same principles as in the [Lean Number Game](https://adam.math.hhu.de/#/g/leanprover-community/nng4/world/Addition/level/0). 

```haskell
data NN = O | S NN 
data Exp = Plus Exp Exp | Times Exp Exp | Num NN

add O n = n
add (S n) m = S (add n m)

mult O n = O
mult (S n) m = add m (mult n m)

eval (Num n) = n
eval (Plus n m) = add (eval n) (eval m)
eval (Times n m) = mult (eval n) (eval m)
```

Reading the equations for `add`, `mult`, `eval` from left to right, they define a **rewrite relation**. 


## Turing machines 

A [Turing machine](https://plato.stanford.edu/entries/turing-machine/) is a finite state machine moving a head over an infinite tape, reading and writing one symbol at a time. A particular TM can be specified by set of rules of the form

$$
(q,S,S',M,q')
$$

saying that if the TM is in state $q$ reading $S$ on the tape then it replaces $S$ by $S'$, moves the head in direction $M\in\{L,R\}$ and goes to state $q'$. 

Equivalently, a TM can be formulated as a string rewriting system: The current state as well as the tape are represented as a string

    a1 ... an q b1 ... bm
    
where the `ai` and `b_i` are symbols on the tape and `q` is the current state of the finite state machine operating on the tape. It can be represented by rewrite rules of the kind

    qS -> S'q'
    
saying "replace `S` by `S'`, go to state `q'` and move the head to the right".

This is best explored interactively, e.g. here:
https://turingmachinesimulator.com/

**Exercise:** Write down a rewrite rule for moving the head to the left.

## More Examples

### Goedel, Escher, Bach

A great book about the many facets of computation is  [Douglas R. Hofstadter's "Gödel Escher Bach" (GEB)](https://www.physixfan.com/wp-content/files/GEBen.pdf). Chapter 1 captures exactly the concept of term rewriting in the guise of a puzzle:<

![](https://hackmd.io/_uploads/HJXqkntlp.png =500x)



### Conway's Game of Life

[Find forms](https://playgameoflife.com/) that are stable, are periodic, or show some other interesting behaviour. Which [pentominos](https://en.wikipedia.org/wiki/Pentomino) stay alive?

### Langton's Ant

Can you explain [Langton's Ant](https://kartoweb.itc.nl/kobben/D3tests/LangstonsAnt/) as a rewrite system? 

By the way, whether all starting configurations of Langton's Ant will eventually converge to "the cannon" (or "highway") is an open problem. Another open problem is the

### Collatz Problem

The [Collatz Problem](https://en.wikipedia.org/wiki/Collatz_conjecture) is rewriting integers. If $n\ge 2$ is even then we divide it by $2$ and if $n\ge 3$ is odd we replace it by $3n+1$. It is an open problem whether this is terminating. To play around with it you can use this [calculator](https://www.dcode.fr/collatz-conjecture). Notice that the numbers can grow and shrink in seemingly unpredictable ways before they reach 1. (What is the smallest number $n$ such that the reduction sequence has "more than $n$ peaks"? I don't know the answer but I'd hope that it was possible to find the answer by writing a little computer program.) If you like these kind of problems you find more information in this [Quanta article](https://www.quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/) and this [Numberphile video](https://www.youtube.com/watch?v=5mFpVDpKX70), the [second part](https://www.youtube.com/watch?v=O2_h3z1YgEU) of which explains how a generalised Collatz Problem is related to Turing's halting problem.

## Questions

Defining as a computation any process that is specified by a *finite* set of *definite* rules the following questions arise.

- What counts as a result of a computation?
- What happens if at any one point in time, more than one rule can be applied?
- Does a given set of rules guarantee that all computations terminate? 
- Do all computations starting with the same data give the same result?
- Bonus Question: What is the meaning (if at all) of infinite computations?


## Summary

These notes argued by example that "all computation is rewriting". In the following lectures we will look at some rewriting theory, motivated by the questions above.

Apart of applications to programming languages, rewriting also provides a powerful problem solving technique that can be applied to many algorithms and other situations with great profit.
