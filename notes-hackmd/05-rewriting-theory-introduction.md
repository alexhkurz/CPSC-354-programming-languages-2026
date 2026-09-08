---
tags: programming languages
---
# Rewriting Theory: Introduction

In the [Lean Natural Number Game](https://adam.math.hhu.de/#/g/leanprover-community/nng4/), have seen a number of examples in which computation proceeds by rewriting expressions. 

The basic mechanism is quite general: It involves the application of a finite number of rules to a finite expression using pattern matching.

Now we are going to abstract even more. We simplify the mechanism by dropping the pattern matching. The price we have to pay is that we need to admit the possibility of an infinite set of rules.

**Definition:** An abstract reduction system[^ars] $(A,R)$ is a set $A$ together with a relation ${R}\subseteq A\times A$.

[^ars]: Or also abstract rewriting system. The qualifier "abstract" indicates that the elements of $A$ are not required to have further structure. One talks about string rewriting if the elements of $A$ are strings, about graph rewriting if the elements of $A$ are graphs, etc.

**Remark:** The notation ${R}\subseteq A\times A$ means that $R$ is a set of pairs $(a,b)$ with $a,b\in A$. There is a revision guide on [Discrete Math: Logic and Relations](https://hackmd.io/@alexhkurz/S1E449agkg).

**Terminology:** I am going to abbreviate "abstraction reduction system" by **ARS**. An element of $R$ is called a **reduction**, or a *computation step* or a *one-step computation*. A **computation** is a sequence $(a_1,a_2,a_3 \ldots)$ such that all pairs $(a_1,a_2), (a_2,a_3),\ldots$ are reductions.

**Activity:** Instantiate the definition of an ARS with some of the 
from [Rewriting: Examples](https://hackmd.io/3Zecca-ERnmxSjOdurvrvA?view).

**Remark:** An ARS is the same mathematical structure as a [directed graph](https://algs4.cs.princeton.edu/42digraph/). Closely related mathematical models are [networks](https://web.stanford.edu/~jacksonm/netbook.pdf), [automata](https://en.wikipedia.org/wiki/Finite-state_machine), [transition systems](https://en.wikipedia.org/wiki/Transition_system) and even [argumentation frameworks](https://en.wikipedia.org/wiki/Argumentation_framework). The reason that the same mathematical structure comes under different names is that it is used in different areas to model different phenomena.

We are interested in analysing non-deterministic computations specified by a set of rules. The theory we will show the beginnings of is motivated by the question: 

**When can a binary relation $R$ be interestingly considered as the computation relation executing an algorithm?**

In other words, under which circumstances does it make sense to consider an ARS $(A,R)$ as a model of computation?

Abstractly, $A$ is any set and $R$ is any binary relation on $A$. In examples, $A$ will be a set of data and $R$ will be a computation relation operating on data in $A$.

Two important questions we are interested in is whether a given ARS is confluent and whether it is terminating.

We will make these notions precise in the next lecture, for now the aim is to get an intuitive understanding. 

<!--
An ARS is **confluent** if for every "peak" 
![rw1](https://hackmd.io/_uploads/rkCTxsax1e.jpg =200x)
there is a "valley" (in red) 
![rw2](https://hackmd.io/_uploads/rJbxWiTxkx.jpg =200x)
that joins the two computations diverging from the peak.
-->

An ARS is **confluent** if for every "peak" 
![image](https://hackmd.io/_uploads/HJbB1wb-kx.png =300x)
tere is a "valley" (dashed arrows)
![image](https://hackmd.io/_uploads/ByCWkv-bkl.png =300x)

Here the $\stackrel \ast \longrightarrow$ indicates zero or more computation steps.

**Remark:** Confluence is practically important because it guarantees that a program's outcome is predictable regardless of the order in which rules are applied (the so-called reduction strategy or evaluation strategy). For the precise definition of confluence see the next lecture.

**Example:** Arithmetic is confluent, for example,
![rw3](https://hackmd.io/_uploads/H10g-o6xJl.jpg =200x)

**Question:** Which law of arithmetic is behind the fact that the two computations of $1+2+3$ yield the same result?

Is arithmetic terminating?

An ARS is **terminating** if it does not admit an infinite computation (=sequence of reductions). 

**Example:** 
- Arithmetic, if defined via the high-shool algebra equations (see Examples linked above) is not terminating, because equations can be applied both left-to-right and right-to-left.
- Arithmetic, if defined as in this [calculator](https://hackmd.io/3Zecca-ERnmxSjOdurvrvA?view) is terminating. 

**Exercise:** Explain why (or why not) your solutions to Assignment 1 are terminating.

What is the result of a computation? The idea is that we reached a result if no further rule applies. The technical term for this is "normal form".

$b\in A$ is a **normal form** if there is no reduction $(b,c)\in R$. $b$ is a normal form of $a$ if $b$ is a normal form and there is a computation from $a$ to $b$. $b$ is the unique normal form of $a$ if $b$ is the only normal form of $a$.

An ARS **has unique normal forms** if all elements have a unique normal form.

## Appendix: Link to Diagrams

[q.uiver](https://q.uiver.app/#q=WzAsMTAsWzIsMCwiXFxidWxsZXQiXSxbMCwyLCJcXGJ1bGxldCJdLFs0LDIsIlxcYnVsbGV0Il0sWzAsMywiXFxidWxsZXQiXSxbNCwzLCJcXGJ1bGxldCJdLFsyLDUsIlxcYnVsbGV0Il0sWzgsMCwiXFxidWxsZXQiXSxbNiwyLCJcXGJ1bGxldCJdLFs4LDQsIlxcYnVsbGV0Il0sWzEwLDIsIlxcYnVsbGV0Il0sWzAsMSwiXFxhc3QiLDJdLFswLDIsIlxcYXN0Il0sWzMsNSwiXFxhc3QiLDJdLFs0LDUsIlxcYXN0Il0sWzYsNywiXFxhc3QiLDJdLFs2LDksIlxcYXN0Il0sWzcsOCwiXFxhc3QiLDIseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbOSw4LCJcXGFzdCIsMCx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==)