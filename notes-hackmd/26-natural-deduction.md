# Natural Deduction

We present the calculus of natural deduction for intuitionstic propositional logic twice.

The first version only concerns the logic and allows us to do pen-and-paper proofs.

The second version is an exercise where the reader is asked to add proof terms (=programs) to the rules. These proof terms should be the same as used in the proof assistant Lean.

The [Lean Intro to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic) offers a practical introduction. The most relevant exercises are in the [$\wedge$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/AndIntro/level/0) and the [$\to$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/AndIntro/level/0) and the [$\vee$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/OrIntro/level/0) and the [$\neg$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/NotIntro/level/0).


## Propositions / Types

The calculus of natural deduction of intuitionistic logic.

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

#### $\vee$-introduction

$$
\frac{A}{A\vee B}
\quad\quad\quad\quad
\frac{B}{A\vee B}
$$

#### $\vee$-elimination

$$
\frac{A\vee B \quad\quad A\to C \quad\quad B\to C}{C}
$$

#### $\bot$-elimination

$$
\frac{\bot}{A}
$$

#### negation

$$
\text{$\neg A$ is an abbreviation for $A\to\bot$}
$$


## With Proofs / Programs

Below, $x$ is a variable and $a,b,f,p$ are expressions (programs, proofs).

**$\wedge$-introduction** [^andIntro]

$$
\frac{a:A\quad\quad b:B}{\langle a,b \rangle: A\wedge B}
$$

[^andIntro]: Write $\langle a,b\rangle$ as `\langle a, b\rangle` and $\wedge$ as `\wedge`

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

[^toIntro]: Written as $\lambda a.b$ in Latex and as `\lambda a \mapsto b` in Lean.

$$
\frac{x:A \quad\quad e:B}{\lambda a.b: A\to B}
$$

**$\to$-elimination** [^toElim]

[^toElim]: Aka modus ponens.

$$
\frac{a:A \quad\quad f:A\to B}{f\,a :B}
$$

#### $\vee$-introduction

$$
\frac{a:A}{\text{or_inl } a : A\vee B}
\quad\quad\quad\quad
\frac{b:B}{\text{or_inl } b : A\vee B}
$$

#### $\vee$-elimination

$$
\frac{o:A\vee B \quad\quad a: A\to C \quad\quad b:B\to C}{\text{or_elim } o\ a\ b : C}
$$

#### $\bot$-elimination

$$
\frac{p:\bot}{\text{false_elim } p:A}
$$

#### negation

$$
\text{$\neg A$ is an abbreviation for $A\to\bot$}
$$

## References

- Gentzen, [Untersuchungen über das logische Schließen. I](https://gdz.sub.uni-goettingen.de/id/PPN266833020_0039?tify=%7B%22pages%22%3A%5B190%5D%2C%22pan%22%3A%7B%22x%22%3A0.493%2C%22y%22%3A0.818%7D%2C%22view%22%3A%22info%22%2C%22zoom%22%3A0.434%7D). Mathematische Zeitschrift. 39 (2): 176–210. 1935 ...
- Online: [SEP](https://plato.stanford.edu/entries/natural-deduction/) ... [Wikipedia](https://en.wikipedia.org/wiki/Natural_deduction) ... [nLab](https://ncatlab.org/nlab/show/natural+deduction) ...
- Textbooks: 
    - Avigad et al, [Logic and Proof (Ch.3)](https://leanprover-community.github.io/logic_and_proof/natural_deduction_for_propositional_logic.html)
    - Thompson, [Type Theory and Functional Programming (Ch.1)](https://www.cs.kent.ac.uk/people/staff/sjt/TTFP/)
    - Girard, [Proofs and Types](http://www.paultaylor.eu/stable/prot.pdf)
    - Harper, [Practical Foundations for Programming Languages](http://profs.sci.univr.it/~merro/files/harper.pdf)
    - Magnus, [Forall X (Ch.6)](https://www.fecundity.com/logic/download.html)
