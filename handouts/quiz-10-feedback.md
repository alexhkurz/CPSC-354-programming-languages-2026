# Quiz 10 solutions

## Section S1

**(a)** Write the AST of: `a b c d`.

`a b c d` means $((a\,b)\,c)\,d$.

```
('app',
    ('app',
        ('app', ('var', 'a'), ('var', 'b')),
        ('var', 'c')),
    ('var', 'd'))
```

**(b)** Write the AST of: `\a.\b. a b`.

```
('lam', 'a', ('lam', 'b', ('app', ('var', 'a'), ('var', 'b'))))
```

**(c)** Find the set of free variables of $\lambda a.\lambda b.\,a\,c$.

\[
\operatorname{FV}(\lambda a.\lambda b.\,a\,c)=\{c\}.
\]

**(d)** Compute $(\lambda y.\,y\,x)[y/x]$.

\[
(\lambda y.\,y\,x)[y/x]
= (\lambda w.\,w\,x)[y/x]
= \lambda w.\,w\,y.
\]

The first equality is an $\alpha$-renaming. The naive result $\lambda y.\,y\,y$ captures the free $y$.

**(e)** Reduce to normal form (leftmost-outermost; free `y` must remain free):

```
(\x.\y. x x y) ((\z. z) y)
(\x.\w. x x w) ((\z. z) y)                    <alpha>
\w. ((\z. z) y) ((\z. z) y) w                <beta>
\w. y ((\z. z) y) w                          <beta>
\w. y y w                                     <beta>
```

The normal form is $\lambda w.\,(y\,y)\,w$. Any fresh bound variable may replace $w$.

**(f)** Write the AST of the normal form from (e).

```
('lam', 'w',
    ('app', ('app', ('var', 'y'), ('var', 'y')), ('var', 'w')))
```

---

## Section S2

**(a)** Write the AST of: `f (g h)`.

```
('app', ('var', 'f'), ('app', ('var', 'g'), ('var', 'h')))
```

**(b)** Write the AST of: `\f. f (f g)`.

```
('lam', 'f',
    ('app', ('var', 'f'), ('app', ('var', 'f'), ('var', 'g'))))
```

**(c)** Find the set of free variables of $\lambda f.\,g\,(f\,h)$.

\[
\operatorname{FV}(\lambda f.\,g\,(f\,h))=\{g,h\}.
\]

**(d)** Compute $(\lambda x.\,x\,(x\,y))[x/y]$.

\[
(\lambda x.\,x\,(x\,y))[x/y]
= (\lambda z.\,z\,(z\,y))[x/y]
= \lambda z.\,z\,(z\,x).
\]

The first equality is an $\alpha$-renaming.

**(e)** Reduce to normal form (leftmost-outermost; free `v` must remain free):

```
(\u.\v. (v u) u) ((\r. r) v)
(\u.\w. (w u) u) ((\r. r) v)                  <alpha>
\w. (w ((\r. r) v)) ((\r. r) v)              <beta>
\w. (w v) ((\r. r) v)                        <beta>
\w. (w v) v                                   <beta>
```

The normal form is $\lambda w.\,(w\,v)\,v$. Any fresh bound variable may replace $w$.

**(f)** Write the AST of the normal form from (e).

```
('lam', 'w',
    ('app', ('app', ('var', 'w'), ('var', 'v')), ('var', 'v')))
```

---

## Section S3

**(a)** Write the AST of: `p q r`.

```
('app', ('app', ('var', 'p'), ('var', 'q')), ('var', 'r'))
```

**(b)** Write the AST of: `\p. p q`.

```
('lam', 'p', ('app', ('var', 'p'), ('var', 'q')))
```

**(c)** Find the set of free variables of $\lambda p.\,p\,q$.

\[
\operatorname{FV}(\lambda p.\,p\,q)=\{q\}.
\]

**(d)** Compute $(\lambda q.\,p\,q)[q/p]$.

\[
(\lambda q.\,p\,q)[q/p]
= (\lambda s.\,p\,s)[q/p]
= \lambda s.\,q\,s.
\]

The first equality is an $\alpha$-renaming.

**(e)** Reduce to normal form (leftmost-outermost; free `q` must remain free):

```
(\p.\q. p (q p)) ((\r. r) q)
(\p.\s. p (s p)) ((\r. r) q)                  <alpha>
\s. ((\r. r) q) (s ((\r. r) q))              <beta>
\s. q (s ((\r. r) q))                        <beta>
\s. q (s q)                                   <beta>
```

The normal form is $\lambda s.\,q\,(s\,q)$. Any fresh bound variable may replace $s$.

**(f)** Write the AST of the normal form from (e).

```
('lam', 's', ('app', ('var', 'q'), ('app', ('var', 's'), ('var', 'q'))))
```
