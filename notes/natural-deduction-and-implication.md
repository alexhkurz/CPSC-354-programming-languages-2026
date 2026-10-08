# Natural Deduction: AND and IMPLIES

We present the calculus of natural deduction for the $\wedge$ and $\to$ fragment of intuitionistic propositional logic twice.

The first version only concerns the logic and allows us to do pen-and-paper proofs.

The second version is an exercise where the reader is asked to add proof terms (=programs) to the rules. These proof terms should be the same as used in the proof assistant Lean.

The [Lean Intro to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic) offers a practical introduction. The most relevant exercises are in the [$\wedge$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/AndIntro/level/0) and the [$\to$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/ImpIntro/level/0).

## Propositions / Types

The calculus of natural deduction for AND and IMPLIES.

#### $\wedge$-introduction

$$
\frac{A\quad\quad B}{A\wedge B}
$$

#### $\wedge$-elimination

$$
\frac{A\wedge B}{A}
\quad\quad\quad\quad
\frac{A\wedge B}{B}
$$

#### $\to$-introduction

$$
\frac{\text{Assume $A$ ... prove $B$}}{A\to B}
$$

#### $\to$-elimination

$$
\frac{A \quad\quad A\to B}{B}
$$

## With Proofs / Programs

Below, $x$ is a variable and $a,b,f,p$ are expressions (programs, proofs).

**$\wedge$-introduction** [^andIntro]

$$
\frac{a:A\quad\quad b:B}{\langle a,b \rangle: A\wedge B}
$$

[^andIntro]: Write $\langle a,b\rangle$ as `\langle a, b\rangle` and $\wedge$ as `\wedge`. In Lean, $\langle a,b\rangle$ is written `⟨a, b⟩` or `and_intro a b`.

**$\wedge$-elimination** [^andElim]

$$
\frac{\langle a,b\rangle :A\wedge B}{a:A}
\quad\quad\quad\quad
\frac{\langle a,b\rangle :A\wedge B}{b:B}
$$


[^andElim]: We write the elimination using the constructor $\langle -,-\rangle$ and pattern matching. But it is worth noting that elimination rules do come with eliminators or deconstructors and the elimination rules can also be written as 
$$
\frac{p:A\wedge B}{p\text{.left}:A}
\quad\quad\quad\quad
\frac{p:A\wedge B}{p\text{.right}:B}
$$


**$\to$-introduction** [^toIntro]

[^toIntro]: Written as $\lambda x.b$ in Latex and as `fun x => b` or `λ x ↦ b` in Lean.

$$
\frac{x:A \quad\quad b:B}{\lambda x.b: A\to B}
$$

**$\to$-elimination** [^toElim]

[^toElim]: Aka modus ponens.

$$
\frac{a:A \quad\quad f:A\to B}{f\,a :B}
$$

## References

- The full calculus including $\vee$, $\bot$ and $\neg$: [Natural Deduction](https://hackmd.io/@alexhkurz/r1bYDpMybx).
- Textbooks:
    - Avigad et al, [Logic and Proof (Ch.3)](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_propositional_logic.html)
    - Thompson, [Type Theory and Functional Programming (Ch.1)](https://www.cs.kent.ac.uk/people/staff/sjt/TTFP/)
