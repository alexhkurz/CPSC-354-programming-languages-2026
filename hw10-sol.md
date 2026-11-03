---
tags: programming languages
---

# HW10 solutions: Lambda-calculus interpreters

## Exercise 1: From concrete syntax to ASTs

1. `x y z` means `(x y) z`.

   ```python
   ('app',
       ('app', ('var', 'x'), ('var', 'y')),
       ('var', 'z'))
   ```

2. `x (y z)`:

   ```python
   ('app',
       ('var', 'x'),
       ('app', ('var', 'y'), ('var', 'z')))
   ```

3. `\x. x y`:

   ```python
   ('lam', 'x',
       ('app', ('var', 'x'), ('var', 'y')))
   ```

4. `(\x. x) y`:

   ```python
   ('app',
       ('lam', 'x', ('var', 'x')),
       ('var', 'y'))
   ```

5. `\x.\y. x (y x)`:

   ```python
   ('lam', 'x',
       ('lam', 'y',
           ('app',
               ('var', 'x'),
               ('app', ('var', 'y'), ('var', 'x')))))
   ```

Removing the parentheses from term 2 changes `x (y z)` into `x y z`,
whose AST is term 1. Removing the parentheses from term 4 changes
`(\x. x) y` into `\x. x y`, whose AST is term 3. Removing the
parentheses from term 5 changes `x (y x)` into `x y x`, because
application associates to the left.

## Exercise 2: Free variables and safe substitution

### (a) Free variables

1. $\mathrm{FV}(\lambda x. x y) = \{y\}$.
2. $\mathrm{FV}(\lambda x.\lambda y. x z) = \{z\}$.
3. $\mathrm{FV}((\lambda x. x y)(\lambda y. y z)) = \{y,z\}$.

In the third term, the first `y` is free because it lies outside the
scope of `\y`. The `z` is also free.

### (b) Substitution

1. Replace the free `x` by `y`:
   $(x z)[y/x] = y z$.

2. The outer lambda binds `x`, so there are no free occurrences of `x`
   in its body:
   $(\lambda x. x z)[y/x] = \lambda x. x z$.

3. The bound `y` must first be renamed to a fresh variable, say `w`:
   $(\lambda y. x y)[y/x] = (\lambda w. x w)[y/x] = \lambda w. y w$.

The naive result `\y. y y` is wrong because the free `y` inserted for
`x` becomes bound by the existing `\y`. This changes the meaning of the
replacement term; the error is called **variable capture**.

## Exercise 3: Evaluation with variable renaming

The bound `y` in the function conflicts with the free `y` in the
argument. Rename the bound variable before substituting:

```text
(\x.\y. x (x y)) ((\z. z) y)
→ (\x.\w. x (x w)) ((\z. z) y)                  <alpha>
→ \w. ((\z. z) y) (((\z. z) y) w)              <beta>
→ \w. y (((\z. z) y) w)                        <beta>
→ \w. y (y w)                                   <beta>
```

The normal form is `\w. y (y w)`. Its `y` remains free, as required.
Its AST is

```python
('lam', 'w',
    ('app',
        ('var', 'y'),
        ('app', ('var', 'y'), ('var', 'w'))))
```

Any fresh name may be used instead of `w`; the resulting terms are
$\alpha$-equivalent.

## Exercise 4: The substitution algorithm

For

```python
substitute(('lam', parameter, body), variable, replacement)
```

the three cases are:

1. If `parameter == variable`, return the lambda unchanged. Occurrences
   of `variable` in `body` are bound by this lambda, so substitution
   must not enter its body.
2. If the names differ and `parameter` is not free in `replacement`,
   recursively substitute in `body`, keeping the same parameter.
3. If the names differ and `parameter` is free in `replacement`, first
   rename `parameter` throughout its bound occurrences in `body` to a
   fresh name. Then recursively perform the requested substitution in
   the renamed body.

One possible outline is:

```python
if parameter == variable:
    return ('lam', parameter, body)
elif parameter not in free_variables(replacement):
    return ('lam', parameter,
            substitute(body, variable, replacement))
else:
    fresh = fresh_name()
    renamed = substitute(body, parameter, ('var', fresh))
    return ('lam', fresh,
            substitute(renamed, variable, replacement))
```

The fresh name must not occur anywhere in `body` or `replacement`, and
it should also differ from `variable`. These conditions prevent both
capture and accidental changes to existing variables.
