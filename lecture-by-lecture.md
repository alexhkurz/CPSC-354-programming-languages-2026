# Lecture by Lecture (PL 2026)

LNDM (Lecture Notes on Discrete Mathematics) refers to Dr Moshier's book  and is available on Canvas for Chapman students.

For background reading: [resources/introtcs.md](resources/introtcs.md) maps each course topic to the matching chapter of Boaz Barak's [Introduction to Theoretical Computer Science](https://introtcs.org/public/), and [resources/geb.md](resources/geb.md) does the same for Hofstadter's *Gödel, Escher, Bach*.

**Week 1 — NNG (proofs by induction)**

- **L1.1**: General introduction.
- **L1.2**: [Lean Natural Number Game (NNG)](https://adam.math.hhu.de/#/g/leanprover-community/nng4) (Tutorial World, Addition World).
  - [How to Write Proofs in Math and in Lean](https://hackmd.io/@alexhkurz/HJdkuFnDzl) (Tutorial Level 8); LNDM, Example 1, pp. 21.  
  - LNDM, Appendix A pp. 230–235 (proof structure).
  - [An Example Proof by Induction](https://hackmd.io/@alexhkurz/BkZ4h76hA) (NNG Addition World Level 1); LNDM pp. 30–35.
  - Homework 1: Finish Addition World. Write out Level 5 in Math and line up the Lean proof against the Math proof.

**Week 2 — RT1 (confluence, termination, normal forms)**

- **L2.1**: Solution hw1. Rewriting Theory.
  - [Solution HW1 (NNG)](https://hackmd.io/@jweinberger/HkdP-EG_fg)
  - Background: [Discrete Mathematics: Logic and Relations](https://hackmd.io/@alexhkurz/S1E449agkg)
 
- **L2.2**: Rewriting Theory. 
  - [hw2 (RT1)](https://hackmd.io/@jweinberger/SJoCCbLufe).
  - Rewriting: 
    - [Introduction](https://hackmd.io/n8zklJ_JSOS04QE6NNygBQ?view), 
    - [Examples](https://hackmd.io/@jweinberger/rJ3JhYfuGx), 
    - [Definitions](https://hackmd.io/@jweinberger/H1Pr6tzOGe)
  
**Week 3 — RT2 (equivalence relations, invariants)**

- **L3.1**: Quiz 1 (NNG). 
  - [Solution hw2](https://hackmd.io/89uIvsBBSlCF6VOpS7ultQ).  (**Due to Labor Day, for Section 1 and 2, this will be merged with L3.2 on Wednesday.**)

- **L3.2**: Rewriting Theory. 
  - [hw3 (RT2)](https://hackmd.io/@jweinberger/r1q6RMyKMx).

**Week 4 — Parsing (concrete syntax trees)**

- **L4.1**: Quiz 2 (RT1) on [hw2 (RT1)](https://hackmd.io/@jweinberger/SJoCCbLufe). 
  - [Solution hw3](https://hackmd.io/@alexhkurz/SJ0NUotFfg).
  - [Equivalence Relations](https://hackmd.io/@alexhkurz/S1E449agkg#Equivalence-Relations)
  - [Equivalence Classes](https://hackmd.io/@alexhkurz/S1E449agkg#Equivalence-Classes)
  
- **L4.2**: 
  - [Parsing](https://hackmd.io/@jweinberger/ByEfEFdFzl) ... [a background reader](https://hackmd.io/@alexhkurz/Bk9IzRYKzg)
  - [123.md](https://hackmd.io/@alexhkurz/SkPLtk9Kze)
  - [hw4](https://hackmd.io/7Z1tR6TPSDaOBPMylhuicA?view#Homework-preparation-for-Quiz-4).

**Week 5 — Programming Assignment 1 (abstract sytax trees)**

- **L5.1**: Quiz 3 (RT2) on [hw3 (RT2)](https://hackmd.io/@jweinberger/r1q6RMyKMx). 
  - [Solution hw4](https://hackmd.io/@alexhkurz/SkOJDqeqfx).
  
- **L5.2**: 
  - Comments on Quiz 2: [Section 3](https://hackmd.io/@alexhkurz/HJ3X01f5Gg)
  - Homework: [hw5](https://hackmd.io/@alexhkurz/BkX02zfcfx) (ASTs and PA1).
  - [Programming Assignment 1](https://hackmd.io/@alexhkurz/HJIOalf5fg) (calculator). On Git: [calculator-2024](https://codeberg.org/alexhkurz/calculator-2024/). 
  - Optional challenge: [A Calculator From Scratch with a Coding Assistant](https://hackmd.io/@alexhkurz/SyeFTlG9Ml). 

**Week 6 — Lambda Calculus (LC) (capture avoiding substitution ($\beta$-rule))**

- **L6.1**: Quiz 4 (parsing) on [hw4](https://hackmd.io/7Z1tR6TPSDaOBPMylhuicA?view#Homework-preparation-for-Quiz-4). 
  - [Solution hw5](https://hackmd.io/@jweinberger/BkFor__9Gl). [LALR](https://en.wikipedia.org/wiki/LALR_parser)
- **L6.2**:
  - Comments on Quiz 3: [Section 3](https://hackmd.io/@alexhkurz/ByAgibhqfl)
  - [Lambda calculus: syntax and semantics](https://hackmd.io/@alexhkurz/rJR2H3YCR). [Blockly Lambda Calculus](https://alexhkurz.github.io/BlocklyLambdaCalculus/lc-with-arithmetic/).
  - Homework: [hw6](https://hackmd.io/@alexhkurz/SJL8qlocze).

**Week 7 — Lean Logic Game (LG) (Curry-Howard Correspondence)**

- **L7.1**: Quiz 5 (PA1) on [hw5](https://hackmd.io/@alexhkurz/BkX02zfcfx). 
  - [Solution hw6.](https://hackmd.io/@jweinberger/By1_4H-iMg)
- **L7.2**: 
  - [Lean Logic Game](https://adam.math.hhu.de/#/g/trequetrum/lean4game-logic). The `->` Tutorial is an independent introduction to lambda calculus. What is the same and what is different? For some tasks you need to have done the `/\` Tutorial first. 
  - The rules of constructive logic for these two tutorials: [Natural Deduction: AND and IMPLIES](notes/natural-deduction-and-implication.md).
  - Optional:
      - [Natural Deduction](https://hackmd.io/@alexhkurz/r1bYDpMybx) — the full calculus, including `\/` and `¬`.
      - [Negation in Classical and Intuitionistic Logic](https://hackmd.io/@alexhkurz/Bkn5Q_Pfgl) — companion to the `¬` Tutorial.
  - [Homework: hw7](https://hackmd.io/@alexhkurz/rkw5mVXozx). 
  - **Deadline: PA1 (Sunday, 11:59 PM)**.

**Week 8 — Church Encodings**

- **L8.1**: Quiz 6 (LC) on [hw6](https://hackmd.io/@alexhkurz/SJL8qlocze). Solution hw7.
- **L8.2**: Church encodings. hw8.

**Week 9 — Fixed Point Combinator (Y)**

- **L9.1**: Quiz 7 (LG) on [hw7](https://hackmd.io/@alexhkurz/rkw5mVXozx). Solution hw8.
- **L9.2**: Fixed Point Combinator. hw9.

**Week 10 — Programming Assignment 2**

- **L10.1**: Quiz 8 (Church). Solution hw9.
- **L10.2**: Lab on PA2 (lambda calculus). 
  - [Lambda Calculus in Python](https://hackmd.io/@alexhkurz/B1FMhwc1bg) 
  - [lambdaC](https://codeberg.org/alexhkurz/lambdaC-2024). 
  - hw10.

**Week 11 — Recursion**

- **L11.1**: Quiz 9 (Y). Solution hw10.
- **L11.2**: Recursion. hw11.

**Week 12 — Invariants**

- **L12.1**: Quiz 10 (PA2). Solution hw11.
- **L12.2**: Invariants. hw12. **Deadline: PA2**.

**Week 13 — Programming Assignment 3**

- **L13.1**: Quiz 11 (Recursion). Solution hw12.
- **L13.2**: Lab PA3. 
  - [Programming Assignment 3](https://hackmd.io/@jweinberger/rkQ8qGMWZx)
  - [lambdaF](https://codeberg.org/alexhkurz/lambdaF-2024).
  

**Thanksgiving Week**. No classes.

**Week 14 — Taking Stock**

- **L14.1**: Q&A PA3. Quiz 12 (Invariants).
- **L14.2**: Collective puzzle solving; student evaluations.

**Finals Week**

- **Deadline: PA3**.
