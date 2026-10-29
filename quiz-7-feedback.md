# Quiz 7 feedback

We start with general remarks about problem solving, followed by the solutions.

## Problem-solving techniques

Three ideas from the principles of programming languages are also general problem-solving techniques.

We illustrate all three with **Section 3, Question (d)**: 

> Given $f : A \to B$, write a program of type $A \to A \land B$.

### 1. Use all available data

Every given assumption should be there for a reason. If a function $f$ is among the givens, a correct answer almost always mentions $f$.

For example in Section 3, Question (d), the answer

$$
\lambda a \mapsto \langle a, b \rangle
$$

should look suspicious because it does not use $f$.

### 2. Be careful about free variables

A finished answer should not mention names that were never bound or given. Free variables are a signal that something is missing.


For example in Section 3, Question (d), the answer

$$
\lambda a \mapsto \langle a, b \rangle
$$

should look suspicious because it has a free variable $b$.

### 3. Typechecking at the meta-level

In most real-world problem solving each relevant data item has a type. Performing mental type-checking before writing can catch many errors (for example in science one always checks whether the units come out correctly; [checking units is a form of typechecking](https://dl.acm.org/doi/10.1145/2887747.2804305)).

For example, for this quiz it was important to not confuse programs and types.

| Programs | Types |
|:---------|:------|
| $\langle{-},{-}\rangle$ | $\land$ |
| $\lambda a\mapsto b$ | $A\to B$ |
| lowercase $a$ | uppercase $A$ |

A common mistake was to mix up the two sides.

For example in Section 3, Question (d), 

the answer

$$
\lambda A \to \langle A , f A\rangle
$$

should look suspicious because it uses type-level notation ($A$ and $\to$) where one would expect term-level notation ($a$ and $\mapsto$).

For another example, $\langle a,b\rangle =A\wedge B$ expresses the right idea, but it doesn't type-check on the meta-level: the term on the left is of a different type than the type of the right. 

---

## Section S1

**(a)** Find the type of $\lambda x \mapsto \lambda y \mapsto x$, assuming $x : A$ and $y : B$.

$$A \to B \to A$$

**(b)** Given $a : A$ and $b : B$, write a proof of $B \land A$.

$$\langle b, a \rangle$$

**(c)** Find the type of $\lambda p \mapsto \langle p.\mathrm{right}, p.\mathrm{left} \rangle$, assuming $p : A \land B$.

$$A \land B \to B \land A$$

**(d)** Given $f : A \to B$ and $g : B \to C$, write a $\lambda$-term of type $A \to C$.

$$\lambda a \mapsto g (f a)$$

**(e)** Given $h : A \land B \to C$, write a $\lambda$-term of type $A \to B \to C$.

$$\lambda a \mapsto \lambda b \mapsto h \langle a, b \rangle$$

**(f)** Given $h : A \to B \to C$, write a $\lambda$-term of type $A \land B \to C$.

$$\lambda p \mapsto h (p.\mathrm{left}) (p.\mathrm{right})$$

---

## Section S2

**(a)** Find the type of $\lambda x \mapsto \lambda y \mapsto y$, assuming $x : A$ and $y : B$.

$$A \to B \to B$$

**(b)** Given $a : A$ and $b : B$, write a proof of $A \land (B \land A)$.

$$\langle a, \langle b, a \rangle \rangle$$

**(c)** Find the type of $\lambda p \mapsto \langle p.\mathrm{left}, p.\mathrm{left} \rangle$, assuming $p : A \land B$.

$$A \land B \to A \land A$$

**(d)** Given $f : B \to C$ and $g : A \to B$, write a $\lambda$-term of type $A \to C$.

$$\lambda a \mapsto f (g a)$$

**(e)** Given $h : A \land B \to C$, write a $\lambda$-term of type $B \to A \to C$.

$$\lambda b \mapsto \lambda a \mapsto h \langle a, b \rangle$$

**(f)** Given $h : A \to B \to C$, write a $\lambda$-term of type $B \land A \to C$.

$$\lambda p \mapsto h (p.\mathrm{right}) (p.\mathrm{left})$$

---

## Section S3

**(a)** Find the type of $\lambda x \mapsto \lambda y \mapsto \langle y, x \rangle$, assuming $x : A$ and $y : B$.

$$A \to B \to B \land A$$

**(b)** Given $a : A$ and $b : B$, write a program of type $(A \land B) \land A$.

$$\langle \langle a, b \rangle, a \rangle$$

**(c)** Find the type of $\lambda p \mapsto \langle p.\mathrm{right}, p \rangle$, assuming $p : A \land B$.

$$A \land B \to B \land (A \land B)$$

**(d)** Given $f : A \to B$, write a program of type $A \to A \land B$.

$$\lambda a \mapsto \langle a, f a \rangle$$

**(e)** Given $h : A \land B \to C$, write a program of type $A \to B \to C$.

$$\lambda a \mapsto \lambda b \mapsto h \langle a, b \rangle$$

**(f)** Given $h : (A \to B) \land (A \to C)$, write a program of type $A \to B \land C$.

$$\lambda a \mapsto \langle h.\mathrm{left} a, h.\mathrm{right} a \rangle$$
