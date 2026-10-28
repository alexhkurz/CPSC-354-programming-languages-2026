---
tags: programming languages
---

# HW6 solutions: lambda calculus

## Exercise 1: Confluence and Termination

### (i) Two reduction sequences for $T = (\lambda x.\ x\ x)\ (I\ a)$

**Inner redex first** (the subterm $I\ a$):

$$
\begin{aligned}
(\lambda x.\ x\ x)\ (I\ a) 
& \rightsquigarrow (\lambda x.\ x\ x)\ a \\
& \rightsquigarrow a\ a
\end{aligned}
$$

2 steps.

**Outer redex first** (the whole term, which is itself a redex):

$$
\begin{aligned}
(\lambda x.\ x\ x)\ (I\ a) 
& \rightsquigarrow (I\ a)\ (I\ a) \\
& \rightsquigarrow a\ (I\ a) \\
& \rightsquigarrow a\ a
\end{aligned}
$$

3 steps. (Reducing the other copy of $I\ a$ first gives a variant of the same length.)

Both sequences reach the same normal form $a\ a$. The outer-first sequence duplicates work: since the body $x\ x$ contains *two* copies of the formal parameter, the argument $I\ a$ is duplicated by the substitution, so the redex $I\ a$ has to be reduced twice.

This is the pattern behind **confluence**: whenever a term can reduce in two different directions, the two results can always be reduced further to a common term. A corollary is that the normal form of a lambda term is unique — *if* it exists.

### (ii) $\Omega$ reduces to itself

Writing $\omega = \lambda x.\ x\ x$, the term $\Omega = \omega\ \omega = (\lambda x.\ x\ x)\,\omega$ is a redex. Substituting $\omega$ for $x$ in the body $x\ x$:

$$\Omega = (\lambda x.\ x\ x)\ \omega \ \rightsquigarrow\ \omega\ \omega = \Omega$$

So $\Omega$ reduces to a term identical to itself: the reduction $\Omega \rightsquigarrow \Omega \rightsquigarrow \Omega \rightsquigarrow \cdots$ never terminates and never reaches a normal form.

### (iii) Reducing $(\lambda x.\ y)\ \Omega$

**Outermost redex first** (normal order): the whole term is a redex. Since $x$ does not occur in the body $y$, the argument is discarded:

$$(\lambda x.\ y)\ \Omega \ \rightsquigarrow\ y$$

Normal form in 1 step.

**Argument first** (applicative order): the argument $\Omega$ reduces to itself forever,

$$(\lambda x.\ y)\ \Omega \ \rightsquigarrow\ (\lambda x.\ y)\ \Omega \ \rightsquigarrow\ (\lambda x.\ y)\ \Omega \ \rightsquigarrow\ \cdots$$

so this strategy never terminates.

Confluence still holds: every term reachable from $(\lambda x.\ y)\ \Omega$ either is $y$ or still contains the outer redex and can reduce to $y$. So any two reduction sequences can be rejoined — confluence says that a normal form is unique *if found*, not that every reduction order finds it. Normal order always does.

## Exercise 2: S and K

Recall $K = \lambda x.\lambda y.\ x$ and $S = \lambda x.\lambda y.\lambda z.\ x\ z\ (y\ z)$.

$$
\begin{aligned}
S\ K\ K\ a 
& = (\lambda x.\lambda y.\lambda z.\ x\ z\ (y\ z))\ K\ K\ a \\
& \rightsquigarrow (\lambda y.\lambda z.\ K\ z\ (y\ z))\ K\ a \\
& \rightsquigarrow (\lambda z.\ K\ z\ (K\ z))\ a \\
& \rightsquigarrow K\ a\ (K\ a) \\
& \rightsquigarrow (\lambda y'.\ a)\ (K\ a) \\
& \rightsquigarrow a
\end{aligned}
$$

(We renamed the bound variable of $K$ to $y'$ for readability; recall $K\ a = (\lambda x.\lambda y.\ x)\ a \rightsquigarrow \lambda y'.\ a$.)

So $S\ K\ K\ a \rightsquigarrow a$ for every term $a$: applied to an argument, $S\ K\ K$ behaves exactly like the identity $I = \lambda x.\ x$. In fact one can also compute $S\ K\ K \rightsquigarrow \lambda z.\ K\ z\ (K\ z) \rightsquigarrow \lambda z.\ z$, which is $\alpha$-equivalent to $I$.

## Exercise 3: Mockingbirds

$$
\begin{aligned}
(\lambda x.\ x\ x)\ (\lambda x.\ x)
& \rightsquigarrow (\lambda x.\ x)\ (\lambda x.\ x) \\
& \rightsquigarrow \lambda x.\ x
\end{aligned}
$$

The normal form is $I = \lambda x.\ x$, reached in 2 steps.

Both $\Omega = (\lambda x.\ x\ x)(\lambda x.\ x\ x)$ and this term apply a function to itself, but the outcomes differ. In $\Omega$, substituting $\omega$ for $x$ in the body $x\ x$ *rebuilds the very same redex* $\omega\ \omega$, so the reduction loops forever. Here the substitution produces $(\lambda x.\ x)(\lambda x.\ x)$, which is an application of the *identity* to itself — the identity does not apply its argument to itself, it just returns it, so the next step consumes the redex instead of reproducing it. Self-application loops only when the self-applied term keeps self-application alive.

*Remark (fixed points):* A **fixed point** of a term $F$ is a term $M$ with $F\ M = M$. This exercise is secretly about fixed points of $\omega = \lambda x.\ x\ x$: the identity $I$ is a fixed point of $\omega$, since $\omega\ I \rightsquigarrow I\ I \rightsquigarrow I$; and $\Omega$ is a fixed point of the reduction step itself, since $\Omega \rightsquigarrow \Omega$. In week 9 we will meet the fixed-point combinator $Y$, which uses this same self-application trick to compute a fixed point $Y\ F$ of an arbitrary term $F$.
