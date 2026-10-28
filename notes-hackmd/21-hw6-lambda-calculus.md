---
tags: programming languages
---

# Homework 6 (lambda calculus)

This homework trains the mechanics of computation by substitution. In the coming weeks we will use lambda terms to encode data structures (booleans, numbers, ...) and recursively defined functions; here we only practice the $\beta$-rule

$$(\lambda x. M)\ N \ \rightsquigarrow \ M[N/x]$$

and the renaming of bound variables ($\alpha$-equivalence) that makes substitution safe. All the background you need is in the notes on [Lambda Calculus, Syntax and Semantics](https://hackmd.io/@alexhkurz/rJR2H3YCR).

## Exercise 1: Confluence and Termination

Let $I = \lambda x.\ x$ and consider the term
$$T = (\lambda x.\ x\ x)\ (I\ a)$$

which contains two redexes: the whole term and the subterm $I\ a$.

(i) Write down two different reduction sequences starting from $T$: one that reduces the inner redex first, and one that reduces the outer redex first. Verify that both reach the same normal form. How many steps does each take? Which sequence duplicates work, and why?

(ii) Let $\Omega = (\lambda x.\ x\ x)(\lambda x.\ x\ x)$. Show that $\Omega \rightsquigarrow \Omega$.

(iii) Reduce $(\lambda x.\ y)\ \Omega$ in two ways: first by always reducing the outermost redex, then by always reducing the argument first. What happens in each case? Does confluence still hold?

*The strategy "always reduce the leftmost-outermost redex" is called normal order. It always finds a normal form if one exists; lazy evaluation in Haskell works this way.*

## Exercise 2: S and K

Define
$$K = \lambda x.\lambda y.\ x \qquad S = \lambda x.\lambda y.\lambda z.\ x\ z\ (y\ z)$$

Reduce $S\ K\ K\ a$ to normal form, showing each step. Which familiar function did we just rebuild out of $S$ and $K$?

*It is a theorem that every lambda term can be translated into a combination of $S$ and $K$ alone. Next week we will build booleans and numbers in a similar spirit.*

## Exercise 3: Mockingbirds

Reduce $(\lambda x.\ x\ x)\ (\lambda x.\ x)$ to normal form. Why does this terminate while $\Omega$ does not, even though both are built from self-application?

## Further Reading

- Raymond Smullyan, [To Mock a Mockingbird and Other Logic Puzzles](https://en.wikipedia.org/wiki/To_Mock_a_Mockingbird) (1985). Combinatory logic taught as a puzzle book: a forest of birds where the kestrel is $K$, the starling is $S$, and the mockingbird is $\lambda x.\ x\ x$. Highly recommended if you want like puzzle books and are interested in learning more about lambda calculus.
