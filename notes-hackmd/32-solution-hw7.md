---
tags: programming languages
---

# HW7 solutions: Lean logic game

Throughout, `p.left` and `p.right` (in Lean also `p.1`, `p.2`) extract the two components of evidence `p : A ∧ B`, and `⟨a,b⟩` builds evidence of `A ∧ B` from `a : A` and `b : B`. In Lean, a function is written `λ x ↦ e` (Lean also accepts `λ x => e`, `fun x ↦ e`, and `fun x => e`).

## Exercise 1 (Level 3): `I ∧ S → S ∧ I`

$$\lambda p.\ \langle p.\text{right},\ p.\text{left}\rangle$$

```lean
exact λ p ↦ ⟨p.right, p.left⟩
```

Given evidence `p : I ∧ S`, we have `p.left : I` and `p.right : S`, so `⟨p.right, p.left⟩ : S ∧ I`. As a program, this is the function `swap` that exchanges the components of a pair.

## Exercise 2 (Level 4): the type of `λ c. h2 (h1 c)`

Assume `c : C`. Since `h1` is applied to `c`, it must be a function out of `C`, say `h1 : C → A`. Then `h1 c : A`, and since `h2` is applied to `h1 c`, it must be a function out of `A`, say `h2 : A → S`. Then `h2 (h1 c) : S`, so

$$\lambda c.\ h_2\,(h_1\,c)\ :\ C \to S \qquad \text{given } h_1 : C \to A,\ h_2 : A \to S.$$

```lean
exact λ c ↦ h2 (h1 c)
```

(`A` and `S` can be any propositions; these are the names used in the game.) As a program, this is function composition `h2 ∘ h1`; as logic, it is the transitivity of implication: from `C → A` and `A → S` conclude `C → S`.

## Exercise 3 (Level 6): from `C ∧ D → S` to `C → (D → S)`

Given `h : C ∧ D → S`:

$$\lambda c.\ \lambda d.\ h\,\langle c, d\rangle$$

```lean
exact λ c ↦ λ d ↦ h ⟨c, d⟩
```

With `c : C` and `d : D` we can build the pair `⟨c, d⟩ : C ∧ D`, and then `h ⟨c, d⟩ : S`. Abstracting over `d` gives `D → S`, and abstracting over `c` gives `C → (D → S)`. (Lean also accepts `λ c d ↦ h ⟨c, d⟩`.) As a program, this is **currying**: turning a function of a pair into a function that takes its arguments one at a time.

## Exercise 4 (Level 7): from `C → (D → S)` to `C ∧ D → S`

Given `h : C → (D → S)`:

$$\lambda p.\ h\ (p.\text{left})\ (p.\text{right})$$

```lean
exact λ p ↦ h p.left p.right
```

With `p : C ∧ D`, we have `p.left : C`, so `h p.left : D → S`; and `p.right : D`, so `h p.left p.right : S`. (Recall that application associates to the left: `h p.left p.right` means `(h p.left) p.right`.) Equivalently, one can pattern-match on the pair: `λ ⟨c, d⟩ ↦ h c d`. As a program, this is **uncurrying**, the inverse of Exercise 3.

Together, Exercises 3 and 4 show that `C ∧ D → S` and `C → (D → S)` are logically equivalent. This is why in Lean (and Haskell) a function of "two arguments" is usually given the curried type `C → D → S` (the arrow associates to the right).

## Exercise 5 (Level 8): from `(S → C) ∧ (S → D)` to `S → (C ∧ D)`

Given `h : (S → C) ∧ (S → D)`:

$$\lambda s.\ \langle h.\text{left}\ s,\ h.\text{right}\ s\rangle$$

```lean
exact λ s ↦ ⟨h.left s, h.right s⟩
```

We have `h.left : S → C` and `h.right : S → D`. Given `s : S`, applying both functions to the same `s` yields `h.left s : C` and `h.right s : D`, which we pair up to get evidence of `C ∧ D`. As a program, this takes a pair of functions with a common input and returns a single function that runs both and returns the pair of outputs.
