# Negation in Classical and Intuitionistic Logic

This note is a companion to the [$\neg$ Tutorial of the Lean Intro to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/NotIntro/level/0). 

It can also be read independently as an introduction to intuitionistic logic and/or as an introduction to the proof system of Natural Deduction

The rules of intuitionstic logic are summarized in our note on [Natural Deduction](https://hackmd.io/@alexhkurz/r1bYDpMybx).

## Constructive vs Non-Constructive

One often says that classical logic is not constructive. What do we mean by this? Here is an example.

Let $S$ be the sentence "The program halts on all inputs". Is

$$
\text{$S$ OR NOT $S$}
$$

true?

There is not one answer, in fact, we have a choice here of how to define the logic we want to work in.

In **classical logic**, the law of excluded middle (tertium non datur) 

$$
P\vee\neg P
$$

holds and one can prove statements of the form $A\vee B$ without having a proof of either $A$ or of $B$, see the halting problem above for an example. 

In **inuitionistic logic**, the law of excluded middle $P\vee\neg P$ does not hold. If you want to learn how to reason constructively with OR using the two rules in the footnote [^OrInt] follow the [$\vee$-Tutorial of the Lean Introduction to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/OrIntro/level/0).

[^OrInt]: The main idea is the following. To reason constructively with OR, we use the following introduction and elimination rules:

    **$\vee$-introduction**

    $$
\frac{A}{A\vee B}
\quad\quad\quad\quad
\frac{B}{A\vee B}
$$

    **$\vee$-elimination**

    $$
\frac{A\vee B \quad\quad A\to C \quad\quad B\to C}{C}
$$

    The introduction rules ("how to make a $\vee$") just say that if I know $A$ then I know $A$ OR $B$.

    The elimination rule ("how to use a $\vee$") is more difficult to understand but it does capture reasoning by case distinction. 

 

For us, right now, the take away is only that 

1. Classical Logic is not constructive
2. Intuitionistic Logic rejects some non-constructive principles such as the law of excluded middle.

## The Proof System of Natural Deduction

All the principles of intiutionistic reasoning are acceptable to classical reasoning, but intuitionistic logic rejects some non-constructive principle. Before coming to the main topic of this note, negation, let us look at the proof system of Natural Deduction for AND and IMPLIES, principles on which classical logic and intuitionistic logic agree:

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

To practice reasoning with these rules do the [$\wedge$ Tutorial of the Lean Introduction to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/AndIntro/level/0)

#### $\to$-introduction

$$
\frac{\text{Assume $A$ ... prove $B$}}{A\to B}
$$

#### $\to$-elimination

$$
\frac{A \quad\quad A\to B}{B}
$$

To practice reasoning with these rules do the [$\to$ Tutorial of the Lean Introduction to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/ImpIntro/level/0)


## Negation

Now we come to the main question of this note. How should one reason constructively with negation?

There are two main ideas. The first one is to introduce a symbol

$$
\bot
$$

for contradiction (aka absurdity) and to define negation as

$$
\neg P = P\to \bot
$$

**Discussion:** This may look unfamiliar. Why does it make sense?

The second main idea is what is known as the prinicple of explosion, aka "Ex falso quod libet" (from falsehood, anything follows). 

**Proof of "from falsehood, anything follows"**
- From P ∧ ¬P, we get P
- From P, we can derive P ∨ Q (for any Q)
- From P ∧ ¬P, we also get ¬P
- From P ∨ Q and ¬P, we derive Q

We now apply a standard move in mathematics and turn a theorem into a definition. We define the introduction rule and elimination rule for negation as follows. Obviously (why?) there will be no introduction rule for $\bot$. The elimination rule for $\bot$ is

#### $\bot$-elimination

$$
\frac{\bot}{B}
$$
