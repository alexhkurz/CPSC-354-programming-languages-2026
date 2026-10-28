---
tags: programming languages
---

# Intro to Parsing and Context-Free Grammars

## Introduction

The purpose of this lecture is to understand how the example of a calculator scales to real world probramming languages. The main aim is to learn how to automatically translate "concrete syntax" into "abstract syntax".

*Concrete syntax* considers a program as a string as eg in:
```
1 + 2 * 3
```
*Abstract syntax* considers a program as a tree. For example the abstract syntax tree (AST) of the string `1+2*3` can be written as
```ml
('plus', ('num', 1), ('times', ('num', 2), ('num', 3)))
```

**Activity/Exercise:** In what sense are trees and nested lists the same data type?

An AST is an element of an algebraic data type, similar to those we have seen in Lean (namely the natural numbers). ASTs have the advantage that one can write type checkers, interpreters and compilers via recursion on these algebraic data types.

The bad news is that translating strings into trees is more difficult than it should be. The good news is that this is a problem that was solved quite some time ago: The transformation of concrete syntax into abstract syntax is known as **parsing**. And the theory (and practice) of parsing is well understood.[^parsing]

To summarize, the main idea pursued in this lecture is:

```
concrete syntax (string) ---> concrete syntax tree ---> abstract syntax tree
```

## Parsing

Looking at parsing from the point of view of ordinary (1-dimensional) syntax, parsing is about putting the parentheses in the right place. For example,
```
1+2*3
```
is turned into 
```
1+(2*3)
```
But this is still a linear expression that is not easy to process automatically. In particular, matching opening and closing parentheses may be arbitrarily far apart. 

**Discussion:** We can find similar examples in natural language. Use the idea of "putting the parentheses into the right place" to explain how the following sentences (collect your owns) are ambigous.

    Novak Djokovic, five times a champion here, failed 
	to reach the concluding Sunday of the ATP World Tour Finals 
	for a record eighth time [...].

**Discussion:** Have a look at [Fibonacci in LISP](https://lisp-lang.org/learn/functions). Discuss the claim that in LISP the programmer directly writes abstract syntax. Why was LISP was this way? Thanks to Christopher Chang for providing a link to this sketch of a [history of LISP](https://twobithistory.org/2018/10/14/lisp.html).

As discussed already, for processing abstract syntax such as (written now in 2-dimensional syntax):

        Plus
         / \ 
      Num   Times
       |      / \
       1   Num   Num
            |     |
            2     3
            
The upcoming aims in the course are the following.

- Define the concrete syntax of a calculator using a  context free grammar. 
- Write a context-free grammar using the parser generator Lark.
- Use Python to generate a parser that translates concrete arithmetic expressions to abstract ones.

*This session is meant to introduce us to context-free grammars as an important concept of discrete mathematics. We will look at how to use it to solve the engineering problem of how to build a parser in the upcoming programming assignment.*

## A context-free grammar 

A **context-free grammar (CFG)** is a set of rules such as the following. 
```
Exp -> Exp '+' Exp1                                
Exp1 -> Exp1 '*' Exp2                              
Exp2 -> Integer                                         
Exp2 -> '(' Exp ')'    
Exp -> Exp1                                        
Exp1 -> Exp2
```

It is possible to give a finite number of rules to produce all integers, but we ignore this here and just assume that we have a rule to produce any integer we want, for example:

```
Integer -> '1'
Integer -> '2'
Integer -> '3'
```
    
The purpose of a **context-free grammar** is to define a language, that is, a set of strings (aka words). In our case, we want to define arithmetic expressions. A particular string is in the language if it can be derived from the **start symbol**, which is `Exp` in the example. The symbols that will appear in the strings, the so-called **terminals**, are those that are enclosed in single quotes, that is, 

    +
    * 
    ( 
    ) 
    
    1
    2
    3
    
The other symbols such as `Exp`, `Exp1`, etc ... never appear in the parsed string but only control which strings can be derived. 

<!--
(In the following derivation I will drop the single quotes for readability.)

    Exp -> 
    Exp1 ->
    Exp1 * Exp1 ->
    Exp2 * Exp1 ->
    Exp2 * Exp2 ->
    Integer * Exp2 ->
    Integer * Integer ->
    2 * Integer ->
    2 * 1    
    
The same string can have many different derivations as we are free to choose the order in which we apply the rules. On the other hand, for the grammar above, any two different derivations of the same string correspond to the same tree. 

**Exercise:** Study the derivation above. How many other deriviations can you make just by switching the order in which you apply the rules?

**Exercise:** Draw the deriviation above as a tree. How many different derivation trees can you make?
-->

The next exercise is the most important one. You need to do enough exercises of this kind until you feel comfortable parsing small examples by hand.

## <font color=red>Homework (preparation for Quiz 4):</font>

Using the context-free grammar

    Exp -> Exp '+' Exp1 
    Exp1 -> Exp1 '*' Exp2              
	Exp2 -> Integer            
	Exp2 -> '(' Exp ')'  
    Exp -> Exp1             
	Exp1 -> Exp2                                     

write out the derivation trees (also called **parse trees** or **concrete syntax trees**) for the following strings:

- `2+1`
- `1+2*3`
- `1+(2*3)`
- `(1+2)*3`
- `1+2*3+4*5+6`


## More Exercises

**Exercise:** Why do the following strings not have parse trees (given the context-free grammar above)?

- `2-1`
- `1.0+2`
- `6/3`
- `8 mod 6`

**Exercise:** Can you change the grammar, so that the strings in the previous exercise become parsable?

## More on Order of Operations via Precedence Levels

The grammar above has one subtle feature: The grammar makes sure that the *only* way to parse 

    1+2*3
    
is to mean $1 + (2\cdot 3)$ and not as $(1+2)\cdot 3$. 

Watch the video [Order of Operations in CFGs](https://youtu.be/jf1xhZSpCvg) for an explanation.


**Exercise**: This problem follows up on the video [Uniqueness of Parse Trees](https://youtu.be/3ZLkPwB_c9g).

- With the simplified grammar without precedence levels

        Exp -> Exp '+' Exp
        Exp -> Exp '*' Exp
        Exp -> Integer
    
    how many parse trees can you find for the following expressions?

        1+2+3
        1*2*3*4
    
- Answer the question above using instead the grammar 

        Exp -> Exp '+' Exp1                                
        Exp -> Exp1                                        
	    Exp1 -> Exp1 '*' Exp2                              
	    Exp1 -> Exp2                                       
	    Exp2 -> Integer                                         

**Discussion:** What are the similarities and differences between the grammar 

	Exp -> Exp '+' Exp
	Exp -> Exp '*' Exp
	Exp -> Integer

and the following algebraic data type for the abstract syntax?


\begin{align}
\frac{n:{\sf Int}}{n:{\sf Exp}}
\quad\quad
\frac{e:{\sf Exp}\quad e':{\sf Exp}}{e+e':{\sf Exp}}
\quad\quad
\frac{e:{\sf Exp}\quad e':{\sf Exp}}{e*e':{\sf Exp}}
\end{align}

## General Background

General background is available in the Wikipedia articles on [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form) and [context-free grammars](https://en.wikipedia.org/wiki/Context-free_grammar). Also consult the article on the [Chomsky hierarchy](https://en.wikipedia.org/wiki/Chomsky_hierarchy), in particular the table that aligns grammars with automata.

## Further Study: A brief look at the history

A number of deep insights into parsing can be gleaned from

- Jeffrey Kegler's [timeline](https://jeffreykegler.github.io/personal/timeline_v3) of the history of parsing (**highly recommended**). 

The literature on parsing is vast. For more on this topic see the optional course on Compiler Construction. In the following just a few early references that continue to have a lasting influence. (It is always worth to look at the classics, something we don't do enough in science.)


- Joachim Lambek: [The Mathematics of Sentence Structure](https://www.cs.cmu.edu/~fp/courses/15816-f16/misc/Lambek58.pdf). 1958. 

Read sections 1-4 up to the end of page 158. Terms worth learning here are: sentence, nonsentence, syntactic type, leakage, decision problem, primitive type, context, compound type. Section 4 is important because it explains the idea of *parsing-as-deduction*.

While Lambek's work continues to be influential, and is based on many of the same ideas,  his formalism is different from context-free grammars, which were introduced on the first two pages of Chapter 4 of

- Noam Chomsky: [Syntactic Structures](https://www.academia.edu/4073170/Noam_Chomsky_Syntactic_Structure). 1957.


The first two pages of Chapter 4 in particular remain an excellent introduction even today:

![image](https://hackmd.io/_uploads/rJkYomYTC.png)

Also the general background reviewed in Chapter 2 is still worth reading (as much else in this book). For the historical significance also see its introduction and [Wikipedia on Syntactic Structures](https://en.wikipedia.org/wiki/Syntactic_Structures).

Given how simple it is to write an interpreter on abstract syntax, and how difficult it is to write it on concrete syntax (if we do not use libraries or tools that help us with the parsing), it is maybe not a surprise that in one of the first modern programming languages, LISP, programmers write directly in linearised abstract syntax. (That is why LISP programs have so many parentheses.)

- John McCarthy's original article on LISP: [Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I](http://jmc.stanford.edu/articles/recursive/recursive.pdf)

Have a look at the classical article 

- [Towards a Mathematical Science of Computation](http://www-formal.stanford.edu/jmc/towards.ps) by [McCarthy](https://en.wikipedia.org/wiki/John_McCarthy_%28computer_scientist%29).

McCarthy was a pioneer of Computer Science. In 1955 he coined the term "artificial ingelligence", shortly afterwards he invented LISP and garbage collection, [time-sharing systems](https://en.wikipedia.org/wiki/Time-sharing), and in 1962 he introduced, with the quote above, the notion of abstract syntax.

Interesting for us is that McCarthy emphasises that BNF makes it easy to generate, write and synthesize programs, whereas abstract syntax makes it easy to analyse, translate, type check, interprete and compile programs. Another way to put it, is to say that concrete syntax is good for human readers and abstract syntax is good for automated processing.

Another influential article by McCarthy is 

- [Ascribing mental qualities to machines](http://cs.uns.edu.ar/~grs/InteligenciaArtificial/ascribing.pdf), 1979. 

(It is always worth looking at the original work of the pioneers. They are mostly remembered for only a very small part of their ideas, so there is often something interesting and forgotten to discover.)

[^parsing]: If you read articles and books about compilers written before approx 1979, be aware that there was a time where parsing was THE problem of compiler construction. See this excellent [timeline](https://jeffreykegler.github.io/personal/timeline_v3). I found particular revealing the entries from  "Language as of 1965" to "The Parsing Problem as of 1979".

[^echo]: `echo` copy its input to "standard output". The pipe `|` connects standard output of the program to the left with the standard input of the program to the right.

[^AbsNumber]: If you run BNFC, there will be a file `AbsNumber.hs` ... have a look yourself.

[^LBNF]: More precisely, the language in which the context-free grammars are written is called [LBNF](https://bnfc.readthedocs.io/en/latest/lbnf.html), for labelled BNF.

[^LBNF2]: (LBNF for "Labelled BNF" is the name of the language in which one writes the grammar that is then converted to a parser).

