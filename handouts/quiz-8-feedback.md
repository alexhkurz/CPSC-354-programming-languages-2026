# Quiz 8 solutions

## Section S1

**(a)** Reduce $2\, g\, y$ by one $\beta$-step.

```
(\f.\x. f (f x)) g y
(\x. g (g x)) y
```

**(b)** Reduce the answer from (a) by one more $\beta$-step (to normal form).

```
(\x. g (g x)) y
g (g y)
```

**(c)** Reduce by one $\beta$-step:

```
(\m.\n.\f.\x. m f (n f x)) (\f.\x. f (f x))
(\n.\f.\x. (\f.\x. f (f x)) f (n f x))
```

**(d)** Reduce $0\, f\, x$ to normal form.

```
(\f.\x. x) f x
(\x. x) x
x
```

**(e)** Reduce to a Church numeral:

```
(\m.\n.\f.\x. m f (n f x)) (\f.\x. f (f x)) (\f.\x. f x)
(\n.\f.\x. (\f.\x. f (f x)) f (n f x)) (\f.\x. f x)
\f.\x. (\f.\x. f (f x)) f ((\f.\x. f x) f x)
\f.\x. (\x. f (f x)) ((\f.\x. f x) f x)
\f.\x. f (f ((\f.\x. f x) f x))
\f.\x. f (f ((\x. f x) x))
\f.\x. f (f (f x))
```

---

## Section S2

**(a)** Reduce $2\, h\, z$ by one $\beta$-step.

```
(\f.\x. f (f x)) h z
(\x. h (h x)) z
```

**(b)** Reduce the answer from (a) by one more $\beta$-step (to normal form).

```
(\x. h (h x)) z
h (h z)
```

**(c)** Reduce by one $\beta$-step:

```
(\m.\n.\f.\x. m f (n f x)) (\f.\x. f x)
(\n.\f.\x. (\f.\x. f x) f (n f x))
```

**(d)** Reduce $1\, f\, x$ to normal form.

```
(\f.\x. f x) f x
(\x. f x) x
f x
```

**(e)** Reduce to a Church numeral:

```
(\m.\n.\f.\x. m f (n f x)) (\f.\x. f x) (\f.\x. f (f x))
(\n.\f.\x. (\f.\x. f x) f (n f x)) (\f.\x. f (f x))
\f.\x. (\f.\x. f x) f ((\f.\x. f (f x)) f x)
\f.\x. (\x. f x) ((\f.\x. f (f x)) f x)
\f.\x. f ((\f.\x. f (f x)) f x)
\f.\x. f ((\x. f (f x)) x)
\f.\x. f (f (f x))
```

---

## Section S3

**(a)** Reduce $3\, g\, y$ by one $\beta$-step.

```
(\f.\x. f (f (f x))) g y
(\x. g (g (g x))) y
```

**(b)** Reduce $0\, f\, x$ to normal form.

```
(\f.\x. x) f x
(\x. x) x
x
```

**(c)** Reduce by one $\beta$-step:

```
(\m.\n.\f.\x. m (n f) x) (\f.\x. f (f x))
(\n.\f.\x. (\f.\x. f (f x)) (n f) x)
```

**(d)** Reduce $\mathrm{succ}\, 1$ by one $\beta$-step, where
$\mathrm{succ} = \lambda n.\lambda f.\lambda x.\ f\,(n\, f\, x)$.

```
(\n.\f.\x. f (n f x)) (\f.\x. f x)
\f.\x. f ((\f.\x. f x) f x)
```

**(e)** Reduce to a Church numeral:

```
(\m.\n.\f.\x. m (n f) x) (\f.\x. f (f x)) (\f.\y. f (f y))
(\n.\f.\x. (\f.\x. f (f x)) (n f) x) (\f.\y. f (f y))     -- substituted for m
\f.\x. (\f.\x. f (f x)) ((\f.\y. f (f y)) f) x            -- substituted for n
\f.\x. (\f.\x. f (f x)) (\y. f (f y)) x                   -- substituted for third f
\f.\x. (\z. (\y. f (f y)) ((\y. f (f y)) z)) x            -- substituted for second f, renamed second x
\f.\x. (\y. f (f y)) ((\y. f (f y)) x)                    -- substituted for z
\f.\x. (\y. f (f y)) (f (f x))                            -- substituted for second y
\f.\x. f (f (f (f x)))                                    -- substituted for y
```

Same calculation, keeping the abbreviation $2=\lambda f.\lambda x.\ f\,(f\, x)$ and using $2\, g\, x = g\,(g\, x)$:

```
(\m.\n.\f.\x. m (n f) x) 2 2
(\n.\f.\x. 2 (n f) x) 2                                   -- substituted for m
\f.\x. 2 (2 f) x                                          -- substituted for n
\f.\x. (2 f) ((2 f) x)                                    -- 2 g x = g (g x) with g = 2 f
\f.\x. (2 f) (f (f x))                                    -- 2 f x = f (f x)
\f.\x. f (f (f (f x)))                                    -- 2 f (f (f x)) = f (f (f (f x)))
```

Same pattern with $2$ and $3$ (so the two numerals stay distinct). Here $3=\lambda f.\lambda x.\ f\,(f\,(f\, x))$ and $3\, g\, x = g\,(g\,(g\, x))$:

```
(\m.\n.\f.\x. m (n f) x) 2 3
(\n.\f.\x. 2 (n f) x) 3                                   -- substituted for m
\f.\x. 2 (3 f) x                                          -- substituted for n
\f.\x. (3 f) ((3 f) x)                                    -- 2 g x = g (g x) with g = 3 f
\f.\x. (3 f) (f (f (f x)))                                -- 3 f x = f (f (f x))
\f.\x. f (f (f (f (f (f x)))))                            -- 3 f (f (f (f x))) = f^6 x
```
