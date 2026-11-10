---
tags: programming languages
---

# HW11 solutions: Recursion

Throughout, each line arises from the previous one by a single labeled step. Stacks grow downward.

## Exercise 1: Recursion via rewriting

(i)

```text
fib 4
= fib 2 + fib 3                 <fib (n+2)>
= (fib 0 + fib 1) + fib 3       <fib (n+2)>
= (0 + fib 1) + fib 3           <fib 0>
= (0 + 1) + fib 3               <fib 1>
= 1 + fib 3                     <+>
= 1 + (fib 1 + fib 2)           <fib (n+2)>
= 1 + (1 + fib 2)               <fib 1>
= 2 + fib 2                     <+>
= 2 + (fib 0 + fib 1)           <fib (n+2)>
= 2 + (0 + fib 1)               <fib 0>
= 2 + (0 + 1)                   <fib 1>
= 3                             <+>
```

(ii) The call tree is

```text
              fib 4
             /     \
        fib 2       fib 3
        /   \       /    \
    fib 0 fib 1  fib 1  fib 2
                        /   \
                    fib 0 fib 1
```

The node `fib 2` appears twice. Naive rewriting therefore duplicates work: the size of the tree (hence the running time) grows exponentially in `n`, even though there are only `n+1` distinct arguments `0, …, n`.

## Exercise 2: Towers of Hanoi

(i)

```text
hanoi 5 0 2
    hanoi 4 0 1
        hanoi 3 0 2
            hanoi 2 0 1
                hanoi 1 0 2 = move 0 2
                move 0 1
                hanoi 1 2 1 = move 2 1
            move 0 2
            hanoi 2 1 2
                hanoi 1 1 0 = move 1 0
                move 1 2
                hanoi 1 0 2 = move 0 2
        move 0 1
        hanoi 3 2 1
            hanoi 2 2 0
                hanoi 1 2 1 = move 2 1
                move 2 0
                hanoi 1 1 0 = move 1 0
            move 2 1
            hanoi 2 0 1
                hanoi 1 0 2 = move 0 2
                move 0 1
                hanoi 1 2 1 = move 2 1
    move 0 2
    hanoi 4 1 2
        hanoi 3 1 0
            hanoi 2 1 2
                hanoi 1 1 0 = move 1 0
                move 1 2
                hanoi 1 0 2 = move 0 2
            move 1 0
            hanoi 2 2 0
                hanoi 1 2 1 = move 2 1
                move 2 0
                hanoi 1 1 0 = move 1 0
        move 1 2
        hanoi 3 0 2
            hanoi 2 0 1
                hanoi 1 0 2 = move 0 2
                move 0 1
                hanoi 1 2 1 = move 2 1
            move 0 2
            hanoi 2 1 2
                hanoi 1 1 0 = move 1 0
                move 1 2
                hanoi 1 0 2 = move 0 2
```

(ii) The 31 moves are

```text
0 -> 2
0 -> 1
2 -> 1
0 -> 2
1 -> 0
1 -> 2
0 -> 2
0 -> 1
2 -> 1
2 -> 0
1 -> 0
2 -> 1
0 -> 2
0 -> 1
2 -> 1
0 -> 2
1 -> 0
1 -> 2
0 -> 2
1 -> 0
2 -> 1
2 -> 0
1 -> 0
1 -> 2
0 -> 2
0 -> 1
2 -> 1
0 -> 2
1 -> 0
1 -> 2
0 -> 2
```

(iii) Let `P(n)` be the claim: for every pair of distinct pegs `x`,`y`, the call `hanoi n x y` performs exactly $2^n - 1$ moves.

**Base case** `n = 1`: `hanoi 1 x y = move x y` is one move, and $2^1 - 1 = 1$.

**Inductive step.** Assume `P(n)`: every call `hanoi n …` performs $2^n - 1$ moves. By definition,

```text
hanoi (n+1) x y =
  hanoi n x (other x y)
  move x y
  hanoi n (other x y) y
```

so the number of moves is $(2^n - 1) + 1 + (2^n - 1) = 2\cdot 2^n - 1 = 2^{n+1} - 1$. Hence `P(n+1)`. By induction, `P(n)` holds for every $n \ge 1$. (In particular, `hanoi 5 0 2` has $2^5 - 1 = 31$ moves.)
