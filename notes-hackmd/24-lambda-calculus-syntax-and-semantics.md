# Lambda Calculus, Syntax and Semantics

([up](https://hackmd.io/@alexhkurz/HkfERdbbkl))

Lambda calculus is the simplest programming language. It has only variables and functions. Interestingly, that is enough to make it Turing complete.

All programming languages contain a core that is a variation of lambda calculus.

## Syntax

### Overview

Lambda calculus has only three programming constructs:

- **Abstraction:** If $e$ is a program (also called an expression in lambda calculus), possibly containing a variable $x$, then
$$\lambda x.e$$ is the program (or function), which has as a formal parameter $x$. This is called abstraction, because the program $\lambda x.e$ does not depend on $x$ anymore, $x$ is abstracted away. We will explain this in more detail below.

- **Application:** If $e_1$ and $e_2$ are programs then 

$$
e_1\, e_2$$ 

is the program which applies the function $e_1$ to the argument $e_2$.

- **Variables:** The basic programs are just the variables.

## The Abstract Syntax of Lambda Calculus

<!--
In textbooks and articles, one often finds the following 

**Definition 1 (abstract syntax):** The abstract syntax of the $\lambda$-calculus is the language defined by the grammar

$$
e ::= \lambda x.e \mid e\, e \mid x
$$

where $x$ ranges over an infinite set, the elements of which are called variables.

**Activity:** 
- Compare the three bullet points above with $\ e ::= \lambda x.e \mid e e \mid x\ .$ Both have the same meaning. What are the advantages of the shorter notation? 
- Recall from our discussion of the calculator that abstract syntax is a syntax for trees. Build (produce, generate) some abstract syntax trees from the grammar. 
-->

**Remark:** We will comment on the three clauses in turn.
- (Abstraction, function definition.) $\lambda x.e$ is a function. If we compare this with a C-like language 

    $$
    \texttt{int plus_one(int x) { return x+1 }}$$
     
  we note the following differences:
    - No types, that is, `plus_one(x){ return x+1 }`
    - No need for `return`, we just return the last value as in `plus_one(x){x+1}`
    - No functions names which leaves us with `(x){x+1}` which we write as 
    
    $$
    \lambda x. x+1$$

    or, in ASCII, as 

    $$
    \texttt{\x.x+1}$$

    or, in Lean, as

    $$
    \lambda x \mapsto x+1$$

  <!--We will see later what to do about the `+ 1`.-->
  
  
- Why is it called "abstraction"? Function definition is called abstraction since in the same way as the definitions 

      int plus_one(int x) { return x+1 }

  and
  
      int plus_one(int y) { return y+1 }
     
  denote the same function, so do 
  
  $\lambda x.x+1$ and $\lambda y.y+1$
  
  denote the same function. More generally,
  
  $\lambda x.e$ and $\lambda y.e'$

  denote the same lambda term if $e'$ arises from $e$ by substituting $y$ for $x$. In other words, the meaning of $\lambda x.e$ does not depend on $x$, the name $x$ has been *abstracted*.
  

  
- (Function Application.) In a C-like language we would write function application as 

      plus_one(2)
      
  whereas now we write, as in functional programming languages (Haskell, Ocaml, Lean, etc)
  
      plus_one 2 
      
  or, with a nameless/anonymous function, 
  
      (\x.x+1) 2
     
  in other words, we juxtapose (write next to each other) the function and its argument.
  
- (Variables.) Variables are mere names. The only operation available on names will be testing whether two names are equal. In particular, there will be no assignment of values to variables. (The variables of lambda calculus are not references to memory.)


<!--
**Remark:** The grammar $\ e ::= \lambda x.e \mid e\, e \mid x$ defines the syntax of lambda expressions as abstract syntax trees. We add parenthesis if we want to disambiguate a string as in $$(\lambda x. (\lambda y. ((x y) z))) (((a b) c)d)$$

If you want to be sure that a string is not ambiguous, you can modify the grammar as follows
$$\ e ::= (\lambda x.e) \mid (e\, e) \mid x$$

**Exercise:** Write $(\lambda x. (\lambda y. ((x y) z))) (((a b) c)d)$ as an abstract syntax tree.
-->

## Rules for Dropping Parentheses

To recap the difference between abstract and concrete syntax, while abstract syntax is syntax for trees, concrete syntax is syntax for strings. When we linearize trees to strings we get many parentheses, as for example in

$$(((((\lambda a.(\lambda b.(\lambda c.(\lambda d. (((a + b) + c)+d)))))\, 1)\,2)\,3)\, 4)$$

instead of the much more readable [^meaning]

$$(\lambda a.\lambda b.\lambda c.\lambda d. a + b + c+d)\, 1\,2\,3\, 4$$

So we want rules for dropping parenthesis. [^lambdaxyz]

*Remark:* If you already got used to the rules for dropping parentheses in Haskell what comes next will look familiar.

- **Application associates to the left**. This means that, for example

	|short|all parentheses |
	|---|---|
	|$a\,b\,c$| $((a\,b)c)$|
    |$a\,b\,c\,d$|$(((a\,b)c)d)$|
    
- **Abstraction** is essentially a unary operation, so we can drop parentheses without creating ambiguities. For example,

	|short|all parentheses |
	|---|---|
    |$\lambda a.\lambda b. \lambda c. e$|$(\lambda a.(\lambda b. (\lambda c. e)))$|
    |$\lambda a.\lambda b. \lambda c. \lambda d.e$|$(\lambda a.(\lambda b. (\lambda c.(\lambda d. e))))$|
    
- **Application has higher precedence than abstraction**. For example, 
    
    |short|longer | all parentheses
	|---|---|---|
    |$\lambda a.\lambda b. a\, b$|$\lambda a.\lambda b. (a\, b)$ | ($\lambda a.(\lambda b. (a\, b)))$
    |$\lambda a.\lambda b. \lambda c. a\,b\,c$|$\lambda a.\lambda b. \lambda c. (a\,b\,c)$|$(\lambda a.(\lambda b. (\lambda c.((a\,b)c))))$|

    We sometimes say that the scope of a $\lambda$ extends as far to the right as possible.

**Exercise:** Use the convention on parentheses described in the previous remark in order to eliminate as many parentheses as possible from $(\lambda x. (\lambda y. (x y z))) ((a b) c)$ without changing the abstract syntax tree denoted by the expression.

## Semantics of the Lambda Calculus

From the previous section, we know how to write a lambda calculus expression. In this section, we will learn how to execute it.

We will see that the simple idea of computing with number by rewriting equations carries over to $\lambda$-calculus.

### An Example of Substitution

Before getting into the technicalities, let us start with an example. For this, we add addition and multiplication and as many numbers as we want to the lambda calculus.

  $$e ::= \lambda x.e \mid e\, e \mid x \mid e+e \mid e*e \mid 0 \mid 1 \mid 2 \mid 3 \mid 6 \mid 7$$
  
**Exercise:** Write in the syntax above the familiar mathematical function 
$$f(x)=2*x +1.$$

Now let us see how a computation in arithmetic would work. If we want to apply the function $f$ from the previous exercise to an argument such as 3, we compute

\begin{align}
f(3) & = 2*3 + 1 \\
& = 6+1 \\
& = 7
\end{align}

In this lecture we are working to generalise the first computation step 

$$f(3) \ \rightsquigarrow \ 2*3 + 1$$

to lambda calculus. We write $\rightsquigarrow$ now instead of = to emphasise that computation runs in time and that, typically, computations cannot be run backwards. (Btw, reversible computing is a very interesting topic, let me know if you want to know more.) 

**Remark:** The computation step $f(3) \ \rightsquigarrow\  2*3 + 1$ merely **substitutes 3 for $x$ in $f$**, which we will write as $f[3/x]$. [^church] Next week, we will see that even the computation steps $2*3+1\ \rightsquigarrow\  6+1\ \rightsquigarrow\  7$ can be performed by substitution only.

So how would the substitution $f(3) \rightsquigarrow 2*3 + 1$ look in lambda calculus? 

Not much different actually:

$$(\lambda x. 2*x+1)\, 3 \ \rightsquigarrow \ 2 * 3 + 1$$

The only visible difference is that we replaced the name $f$ by the lambda-expression it refers to.

To summarize, substitution so far is is only replacing a placeholder (formal parameter) by an argument.

### An Example of a Function with Two Arguments

The function that adds two numbers can be written as

$$\lambda x. \lambda y. x+y$$

and we apply it to two arguments as follows

$$(\lambda x.\lambda y. x+y) \ 2 \ 3 $$

**Reminder:** According to the rules for dropping parentheses, this is short for $$((\lambda x.(\lambda y. x+y)) \ 2) \ 3$$

**Question:** Do we need a new substitution rule that can deal with simultaneously substituting two arguments? 

No, we just keep everything as it is and apply the  substitution rule twice:

\begin{align}
(\lambda x.\lambda y. x+y) \ 2 \ 3
& \rightsquigarrow (\lambda y. 2+y) \ 3\\
& \rightsquigarrow 2+3 \\
\end{align}

Note that we applied the "inner substitution" 

$$ (\lambda x.\lambda y. x+y) \ 2 
\rightsquigarrow (\lambda y. 2+y) $$

first, while leaving the "3" untouched. 

**Remark:** A familiar idea here is to perform reductions inside bigger expressions. For example, above, in 
\begin{align}
f(3) & \ \rightsquigarrow\  2*3 + 1 \\
& \ \rightsquigarrow\  6+1 \\
& \ \rightsquigarrow\  7
\end{align}
the second "$\rightsquigarrow$" reduces $2*3$ to $6$ inside a bigger expression.

**Remark:** A new idea here is that expressions can reduce to functions. For example, above, in 
\begin{align}
(\lambda x.\lambda y. x+y) \ 2 \ 3
& \ \rightsquigarrow\  (\lambda y. 2+y) \ 3\\
& \ \rightsquigarrow\  2+3 \\
\end{align}
the result of the inner substitution is the function $\lambda y.2+y$, which in turn is applied to the second argument.

**Terminology (Currying):** To replace a function in two arguments by a function that takes one argument and returns a function that takes the second argument is called "currying" after the mathematician and logician [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry).

**Exercise:** Reduce the following. 
\begin{gather}
(\lambda x.\lambda y. x+y) \ 2 \ 3 \\
(\lambda x.\lambda y. y+x) \ 2 \ 3 \\
(\lambda x.\lambda y. x+x) \ 2 \ 3 \\
(\lambda x.\lambda y. y+y) \ 2 \ 3 \\
(\lambda x.\lambda y. z+z) \ 2 \ 3 
\end{gather}

### An Example of Capture Avoiding Substitution

The only way two lambda calculus programs $M$ and $N$ communicate with each other is via an application $(\lambda x.M) N$ . But what happens if there are [name clashes](https://en.wikipedia.org/wiki/Name_collision) between $\lambda x.M$ and $N$? Here is an example:

$$(\lambda x.\lambda y. x + y)\ y \ 2$$

The $y$ in $M=\lambda y. x + y$ means something differnt from the $y$ in $N=y$. We say that the $y$ in $M$ is *bound* and the $y$ in $N$ is *free*. We will learn more about free and bound variables later in the course. For now it is enough to understand that bound variables are formal parameters (and thus are mere place holders that do not have a meaning), whereas free variables have a meaning determined by the larger context in which the program exists.

**Exercise:** Keeping in mind that the meaning of the free occurrence of $y$ is determined by the larger context in which the program exists, what is wrong with the following computation? What would be the correct result?

**Example** of a **wrong** computation:
\begin{align}
(\lambda x.\lambda y. x + y)\ y \ 2 
& \rightsquigarrow 
(\lambda y. y + y)\ 2 \\
& \rightsquigarrow 
2 + 2
\end{align}

The problem with the computation above becomes apparent if we typeset the free $\color{red} y$ in red and the bound $\color{blue} y$, as well as its binder $\color{blue}{\lambda y}$, in blue and compute

\begin{align}
(\lambda x.\color{blue}{\lambda  y}. x + \color{blue} y)\ \color{red}  y \ 2 
& \rightsquigarrow (\color{blue}{\lambda y}. {\color{red} y} + \color{blue}y) \ 2
\end{align}

highlighting that the red $y$ should really be different from the blue $y$.

In fact, if we take the two $y$s to be different, we see that the computation should continue as

\begin{align}
(\lambda x.\color{blue}{\lambda  y}. x + \color{blue} y)\ \color{red}  y \ 2 
& \rightsquigarrow (\color{blue}{\lambda y}. {\color{red} y} + \color{blue}y) \ 2 \\
& \rightsquigarrow {\color{red} y} + 2
\end{align}

The solution to the problem then is to define substitution in such a way that variable $\color{red} y$ cannot be captured by the $\color{blue}{\lambda y}$. 

This is called **capture avoiding substitution**.

How does it work? Simply rename formal parameters (=bound variables). So we compute

\begin{align}
(\lambda x.\lambda y. x + y)\  y 
& = 
(\lambda x.\lambda z. x + z)\  y \\
& \rightsquigarrow  \lambda z. y + z
\end{align}

where the first step only renames the formal parameter (=bound variable) $y$ into $z$. Note that this renaming only renames the bound $y$, not the free 
$y$.

### Renaming Formal Parameters

First, we need to make sure that we know how to rename formal parameters. For example, we have that

$$\lambda x.x=\lambda y.y,$$

that is, the formal parameter $x$ can be renamed to $y$ without changing the meaning of the lambda expression. We also say that $\lambda x.x$ and $\lambda y.y$ are *alpha-equivalent*.

Since formal parameters can be renamed, we can always make them different from all other variables in the program.

This is important to define how lambda calculus programs compute. There is only one computation rule in the lambda calculus. It goes as follows.

### The Computation Rule: $\beta$-Reduction


If $\lambda x. M$ is a lambda term and $N$ is another lambda term, then

$$(\lambda x. M) N$$ 


computes to $$M[N/x]$$ which is our notation for the term $M$ where each occurrence of $x$ is substituted by $N$. 

For this computation step to be allowed, we assume that 

  - the formal parameters of $M$ do not occur in $N$,
  - the formal parameters of $M$ are all different.
  
(If this is not the case we can rename the formal prameters.)


In short we write

$$(\lambda x. M) N \ \rightsquigarrow \ M[N/x]$$ 

and say this as

$$\textrm{Replace} \  x \ \textrm{in} \ M \ \textrm{by } N$$

or also 

    Replace the formal parameter in the body of the function
    by the argument.

**Example:** In $(\lambda x. \lambda y. x)\, a\, b$ the formal parameter is $x$ and the argument is $a$. So we replace $x$ in $\lambda y.x$ by $a$ and get $(\lambda y. a)\, b$ in the first computation step. Now the formal parameter is $y$ and the argument is $b$. Since $y$ does not occur in $a$, replacing $y$ in $a$ by $b$ does not change $a$ and the result is simply $a$ itself.


**Exercise:** Reduce the following (where "S" is a new constant (think of $S$ as "successor" or "plus one")):
- $(\lambda x. S\, x)\,(S\,0)$
- $(\lambda x. S\, x)\, (S\,x)$
- $(\lambda x. (\lambda y. x)) \,y$

**Exercise:** Explain why we need to rename variables before being able to reduce $\ (\lambda x. (\lambda y. x)) \,y$. 


### Another Example on Capture Avoiding Substitution 

This example illustrates a subtle point about renaming variables. 

\begin{align}
(\lambda x.\lambda y. x)\,M\,N & \rightsquigarrow (\lambda y. M)N \\
& \rightsquigarrow M
\end{align}

Let us comment on the two reductions in turn.
- The first reduction shows that we are allowed to apply reductions to subterms. In this case, since we can reduce $$(\lambda x.(\lambda y. x))M\rightsquigarrow \lambda y. M$$

    we can also do this reduction inside a bigger term such as
$$((\lambda x.(\lambda y. x))M)N\rightsquigarrow (\lambda y. M)N$$

    The subterm that we reduce is called the **redex**, short for *reducible expression* (or maybe *reduced expression*).
    
- The second reduction is only correct if we can assume that $y$ does not occur in $M$. Do we need to make this assumption? No, because the first reduction $(\lambda x.(\lambda y. x))M\rightsquigarrow \lambda y. M$ substituted $M$ in a capture avoiding way. Other phrases to express this include
  - the binder $\lambda y$ does not capture free variables in $M$,
  - $y$ is not free in $M$,
  - $y$ is fresh for $M$.
  
## Workout

To practice the $\alpha$ and $\beta$ rule the following is a good workout. (Do it in an editor that can match parentheses.) Evaluate
```
(\f.\x.f(f(x))) (\f.\x.(f(f(f x))))
```

**Remark:** Remember that Alonzo Church invented the lambda calculus in the 1930ies as a foundation of mathematics before computers existed. Can you guess what the mathematical interpretation of this calculation could be?

## Solution to Selected Exercises

$f(x)=2*x +1$ can be written as $\lambda x.2*x+ 1$.

The following computation is correct:
\begin{align}
(\lambda x.\lambda y. x + y)\ y \ 2 
& \rightsquigarrow 
(\lambda z. y + z)\ 2 \\
& \rightsquigarrow 
y + 2 
\end{align}

## Additional Exercises

(the following exercises will prepare us for next week's material)

- The $\beta$-rule looks simple, but it is extremely powerful. In fact, we can use it to run any algorithm at all. In this exercise you can explore some of the things one can do with the $\beta$-rule. Importantly, we can erase, duplicate, and loop:

	- Write a $\lambda$-expression that takes two arguments and returns the first, discarding the second.
	- Write a $\lambda$-expression that takes two arguments and returns the second, discarding the first. 
	- Write a $\lambda$-expression that takes three arguments and deletes the middle one.
	- Write a $\lambda$-expression that takes one argument and duplicates it.
	- Write a $\lambda$-expression that reduces to itself.
	
## Further Reading

- The first sections of [Functional Programming and Lambda Calculus](https://www.cs.jhu.edu/~jason/465/readings/lambdacalc.html) cover the same material. Subsequent sections are recommended browsing to get a glimpse of the relevant landscape.

[^church]: Using so-called Church encodings (coming up soon), even the computation steps $2*3+1\rightsquigarrow 6+1\rightsquigarrow 7$ can be performed by substitution only.
 
[^penandpaper]: To be clear, pen-and-paper means "by hand" as opposed to "by running an Interpreter on your machine". In fact, I recommend to use an editor and Latex's `lstlisting`-environment.


