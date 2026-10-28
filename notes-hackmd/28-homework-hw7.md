---
tags: programming languages
---

# Homework 7 (Lean logic game)

At the start of the course you played the [Natural Number Game](https://adam.math.hhu.de/#/g/leanprover-community/nng4). 

## Introduction

Play the first two worlds of [A Lean Intro to Logic](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic):

1. **∧ Tutorial: Party Invites**
2. **→ Tutorial: Party Snacks**

A proof is evidence. Writing `a:A` means that `a` is evidence for `A`.

We can think of the evidence `a` as a term or a program or a proof. We can think of `A` as a type or a proposition.

Evidence of `A ∧ B` is a pair, evidence `a` for `A` and evidence `b` for `B`. We write `<a,b>` for evidence of `A∧B`.

Evidence of `A → B` is a function that turns evidence `a` of `A` into evidence of `B`. We write `λ a ↦ b` for a function that turns evidence of `A` into evidence for `B`.

For example, `λ c ↦ c` is evidence for `C → C`, see [Level 2 of the -> Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/ImpIntro/level/2).

Clearly, the proposition that "`C` implies `C`" (written `C → C` in Lean) should be true, and the proof of this trivial fact is the identity function `λ c ↦ c` (which we write $\lambda c.c$ in math notation).

## Homework

The following exercises ask you to either find the type (or proposition) for a given $\lambda$-expression, or a $\lambda$-expression for a given type (=proposition).

[Levels refer to the $\to$ Tutorial](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic/world/ImpIntro/level/0).

**Exercise 1 (Level 3)**: This exercise asks for a proof that "AND" is commutative, that is, for a proof of `I ∧ S → S ∧ I`.

**Exercise 2 (Level 4)**: Find a type for `λ c. h2 (h1 c)`. Assume that `c` has type `C` and find appropiate types for `h1` and `h2`.

**Exercise 3 (Level 6)**: Given input of type `C ∧ D → S`, find a function of type `C → (D → S)`.

**Exercise 4 (Level 7)**: Given input of type `C → (D → S)`, find a function of type `C ∧ D → S`.

**Exercise 5 (Level 8)**: Given a term of type `(S → C) ∧ (S → D)`, find a function of type `S → (C ∧ D)`.











