# Quiz 9 solutions

## Section S1

**(a)** Expand `let z = \x. x in z a` by the definition of `let`.

\[
(\lambda z.\, z\, a)\,(\lambda x.\, x)
\]

**(b)** Expand the outer `let` only: `let m = 1 in let n = 2 in m + n`.

\[
(\lambda m.\, \text{let } n = 2 \text{ in } m + n)\, 1
\]

**(c)** Reduce $Y\, e$ by one $\beta$-step.

```
(\f. (\x. f (x x)) (\x. f (x x))) e
(\x. e (x x)) (\x. e (x x))
```

**(d)** Expand `let rec f = \x. x in f 1` by the definition of `let rec`.

```
let f = (fix (\f. \x. x)) in f 1
```

**(e)** Reduce to a number (abbreviation $S = \lambda\mathrm{sum}.\,\lambda n.\, \texttt{if } n = 0 \texttt{ then } 0 \texttt{ else } n + \mathrm{sum}\,(n-1)$):

```
let rec sum = \n. if n = 0 then 0 else n + sum (n - 1) in sum 2
let sum = (fix S) in sum 2                                      <def of let rec>
(\sum. sum 2) (fix S)                                           <def of let>
(fix S) 2                                                       <beta>
(S (fix S)) 2                                                   <def of fix>
(\n. if n = 0 then 0 else n + (fix S) (n - 1)) 2                <beta>
if 2 = 0 then 0 else 2 + (fix S) (2 - 1)                        <beta>
if False then 0 else 2 + (fix S) (2 - 1)                        <2 = 0>
2 + (fix S) (2 - 1)                                             <if False>
2 + (fix S) 1                                                   <2 - 1>
2 + ((S (fix S)) 1)                                             <def of fix>
2 + ((\n. if n = 0 then 0 else n + (fix S) (n - 1)) 1)          <beta>
2 + (if 1 = 0 then 0 else 1 + (fix S) (1 - 1))                  <beta>
2 + (if False then 0 else 1 + (fix S) (1 - 1))                  <1 = 0>
2 + (1 + (fix S) (1 - 1))                                       <if False>
2 + (1 + (fix S) 0)                                             <1 - 1>
2 + (1 + ((S (fix S)) 0))                                       <def of fix>
2 + (1 + ((\n. if n = 0 then 0 else n + (fix S) (n - 1)) 0))    <beta>
2 + (1 + (if 0 = 0 then 0 else 0 + (fix S) (0 - 1)))            <beta>
2 + (1 + (if True then 0 else 0 + (fix S) (0 - 1)))             <0 = 0>
2 + (1 + 0)                                                     <if True>
2 + 1                                                           <1 + 0>
3                                                               <2 + 1>
```

The result is $3 = 2 + 1 + 0$.

---

## Section S2

**(a)** Expand `let id = \x. x in id b` by the definition of `let`.

\[
(\lambda \mathrm{id}.\, \mathrm{id}\, b)\,(\lambda x.\, x)
\]

**(b)** Expand the outer `let` only: `let p = 3 in let q = 4 in p + q`.

\[
(\lambda p.\, \text{let } q = 4 \text{ in } p + q)\, 3
\]

**(c)** Reduce $Y\, e$ by one $\beta$-step.

```
(\f. (\x. f (x x)) (\x. f (x x))) e
(\x. e (x x)) (\x. e (x x))
```

**(d)** Expand `let rec g = \n. n in g 0` by the definition of `let rec`.

```
let g = (fix (\g. \n. n)) in g 0
```

**(e)** Reduce to a number (same `sum 2` program as S1; same abbreviation $S$):

```
let rec sum = \n. if n = 0 then 0 else n + sum (n - 1) in sum 2
let sum = (fix S) in sum 2                                      <def of let rec>
(\sum. sum 2) (fix S)                                           <def of let>
(fix S) 2                                                       <beta>
(S (fix S)) 2                                                   <def of fix>
(\n. if n = 0 then 0 else n + (fix S) (n - 1)) 2                <beta>
if 2 = 0 then 0 else 2 + (fix S) (2 - 1)                        <beta>
if False then 0 else 2 + (fix S) (2 - 1)                        <2 = 0>
2 + (fix S) (2 - 1)                                             <if False>
2 + (fix S) 1                                                   <2 - 1>
2 + ((S (fix S)) 1)                                             <def of fix>
2 + ((\n. if n = 0 then 0 else n + (fix S) (n - 1)) 1)          <beta>
2 + (if 1 = 0 then 0 else 1 + (fix S) (1 - 1))                  <beta>
2 + (if False then 0 else 1 + (fix S) (1 - 1))                  <1 = 0>
2 + (1 + (fix S) (1 - 1))                                       <if False>
2 + (1 + (fix S) 0)                                             <1 - 1>
2 + (1 + ((S (fix S)) 0))                                       <def of fix>
2 + (1 + ((\n. if n = 0 then 0 else n + (fix S) (n - 1)) 0))    <beta>
2 + (1 + (if 0 = 0 then 0 else 0 + (fix S) (0 - 1)))            <beta>
2 + (1 + (if True then 0 else 0 + (fix S) (0 - 1)))             <0 = 0>
2 + (1 + 0)                                                     <if True>
2 + 1                                                           <1 + 0>
3                                                               <2 + 1>
```

The result is $3 = 2 + 1 + 0$.

---

## Section S3

**(a)** Reduce to normal form: `let m = 2 in let n = 3 in m + n`.

```
(\m. let n = 3 in m + n) 2     <def of let>
let n = 3 in 2 + n             <beta>
(\n. 2 + n) 3                  <def of let>
2 + 3                          <beta>
5                              <arithmetic>
```

**(b)** Reduce to normal form: `let rec f = \x. x in f c`.

```
let f = (fix (\f. \x. x)) in f c     <def of let rec>
(\f. f c) (fix (\f. \x. x))           <def of let>
(fix (\f. \x. x)) c                  <beta>
((\f. \x. x) (fix (\f. \x. x))) c     <def of fix>
(\x. x) c                             <beta>
c                                     <beta>
```

**(c)** Reduce to a number (abbreviation $F = \lambda f.\,\lambda n.\, \texttt{if } n = 0 \texttt{ then } 4 \texttt{ else } f\,(n-1)$):

```
let rec f = \n. if n = 0 then 4 else f (n - 1) in f 1
let f = (fix F) in f 1                                          <def of let rec>
(\f. f 1) (fix F)                                               <def of let>
(fix F) 1                                                       <beta>
(F (fix F)) 1                                                   <def of fix>
(\n. if n = 0 then 4 else (fix F) (n - 1)) 1                    <beta>
if 1 = 0 then 4 else (fix F) (1 - 1)                            <beta>
if False then 4 else (fix F) (1 - 1)                            <1 = 0>
(fix F) (1 - 1)                                                 <if False>
(fix F) 0                                                       <1 - 1>
(F (fix F)) 0                                                   <def of fix>
(\n. if n = 0 then 4 else (fix F) (n - 1)) 0                    <beta>
if 0 = 0 then 4 else (fix F) (0 - 1)                            <beta>
if True then 4 else (fix F) (0 - 1)                             <0 = 0>
4                                                               <if True>
```

The result is $4$.
