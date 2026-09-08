---
tags: programming languages
---
# CPSC-354 -- Solution Homework 1 (Natural Number Game)

:::warning
**Homework 1 (Natural Number Game).** Solve [Addition World](https://adam.math.hhu.de/#/g/leanprover-community/nng4/) of the Natural Number Game (Lvl 1--5).

For the final level (Lvl 5), in addition, write up a pen-and-paper mathematics proof, illustrating the connection to the corresponding steps in Lean side by side. 
:::


## Solution 1 (using associativity and commutativity)

We show a possible solution for the second part, following the [Math vs. Lean tutorial](https://hackmd.io/@alexhkurz/HJdkuFnDzl).

**NB.** Lean follows the convention $a+b+c := (a+b)+c$. We will write the latter for clarity.

We want to to prove:

**Theorem.** If $a$, $b$ and $c$ are arbitrary natural numbers, we have $(a+b)+c=(a+c)+b$.

1. **Write out the proof in Math:**

Let $a$, $b$ and $c$ be natural numbers. Then:

\begin{align*}
(a+b) + c & = a + (b + c)& \text{(associativity of +)} \\
& = a + (c + b) & \text{(commutativity of +, for $c$ and $b$)} \\
& = (a + c) + b & \text{(associativity of +)}
\end{align*}

2. **Mapping Math to Lean:**


| **Math** | **Lean** | 
| -------- | -------- |
| associativity of $+$    | `add_assoc`     
| commutativity of $+$, for $b$ and $c$ | `add_comm b c`

3. **Translate from Math to Lean**
A possible translation is as follows:
```
rw [add_assoc]
rw [add_comm b c]
rw [add_assoc]
rfl
```

A slightly shorter variant is as follows:

```
repeat rw [add_assoc]
rw [add_comm b c]
rfl
```

4. **Translate from Lean to Math**
A "back translation" is as follows:

\begin{align*}
a+(c+b) &= a+(c+b) & \text{rfl} \\
a+(c+b) &= (a+c)+b & \text{rw [add_assoc]} \\
a+(b + c) &= (a+c)+b & \text{rw [add_comm b c]} \\
(a+b) + c &= (a+c)+b & \text{rw [add_assoc]} 
\end{align*}


Can you see how the structure changed?

## Solution 2 (by induction)

Let us repeat the theorem.

**Theorem.** If $a$, $b$ and $c$ are arbitrary natural numbers, we have $(a+b)+c=(a+c)+b$.


#### 1. In Math

We do induction on $b$.

**Case $b=0$**:

\begin{align*}
(a+0) + c & = a + c & \text{(def $+$)} \\
& = (a + c) + 0 & \text{(def of $+$)} \\
\end{align*}

**Case $b=Sn$**:


\begin{align*}
(a+Sn) + c & = S (a + n) + c & \text{(def of $+$)} \\
& = S ((a + n) + c) & \text{(property of S and $+$)} \\
& = S ((a + c) + n) & \text{ind hyp} \\
& = (a + c) + Sn & \text{def $+$} \\
\end{align*}

#### 2. Mapping Math to Lean


| **Math** | **Lean** | 
| -------- | -------- |
| def $+$    | `add_zero`, `add_succ`
| property of $S$ and $+$| `succ_add`
| induction hypothesis | `n_ih`

#### 3. Proof in Lean

```
induction b
rw [add_zero,add_zero]
rfl
rw [add_succ,add_succ,succ_add,n_ih]
rfl
```

#### 4. Translate from Lean to Math

Here we follow the goals, for each case, as given by the Lean interface, bottom up.

**Case $b=0$**:

\begin{align*}
a + c & = a + c & \text{rfl} \\
a + c &= (a + c) + 0 & \text{(add_zero)} \\
(a + 0) + c &= (a + c) + 0 & \text{(add_zero)} \\
\end{align*}

**Case $b=0$**:

\begin{align*}
S ((a + c) + n) &= S ((a + c) + n) & \text{rfl} \\
S ((a + n) + c) &= S ((a + c) + n) & \text{ind hyp} \\
S(a + n) + c &= S ((a + c) + n) & \text{succ_add} \\
S(a + n) + c &= (a + c) + Sn & \text{succ_add} \\
(a + Sn) + c &= (a + c) + Sn & \text{succ_add} \\
\end{align*}