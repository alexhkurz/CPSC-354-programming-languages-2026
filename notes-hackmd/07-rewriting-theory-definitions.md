---
tags: programming languages
---
# Rewriting Theory: Definitions

**Definition:** A **(binary) relation** on a set $A$ is a subset $R \subseteq A \times A$ of the cartesian product
$$ A \times A = \{(a,a') \; | \; a, a' \in A\}.$$

**Definition:** An **abstract reduction system** or **abstract rewriting system** $(A,R)$ is a set $A$ together with a relation $R \subseteq A\times A$. [^remark]

In the context of abstract rewriting systems we write the relation $R$ often as $\to$.

[^remark]: **Remark:** "Reduction" is another word for "rewriting" and formalized here mathematically simply by a "relation". In practice, a relation is typically defined via a *finite* set of rules, the application of which requires pattern matching. The definition above aims at simplicity and abstracts from pattern matching. The price we pay for it is that our relation $R$ may be infinite in many examples (even if it is defined via a finite set of rules).

**Notation:** As is common, we write $a \to b$ for $(a,b) \in \to$. We write $\;\stackrel{\ast}{\longrightarrow}\;$ to mean the reflexive and transtitive closure of $\;\stackrel{}{\rightarrow}\;$ and $\;\stackrel{\ast}{\longleftrightarrow}\;$ (or also $\equiv$) for the symmetric, reflexive and transitive closure, that is the smallest equivalence relation containing $\;\stackrel{\ast}{\longrightarrow}\;$. 

**Definition:** Let $(A,\to)$ be an ARS and let $a,b$ range over $A$.
- $a$ and $b$ are ***equivalent*** if $a\stackrel{\ast}{\longleftrightarrow} b$, where $\stackrel{\ast}{\longleftrightarrow}$ is the reflexive, symmetric and transitive closure of $\to$.  We also write $a\equiv b$.
- $a$ is ***reducible*** if there is $b$ such that $a\to b$.
- $a$ is a ***normal form*** if $a$ is not reducible. We also say that $a$ is ***irreducible***.
- $a$ ***reduces to*** $b$ if $a\stackrel{\ast}{\longrightarrow} b$, where $\stackrel{\ast}{\longrightarrow}$ is the reflexive and transitive closure of $\to$. [^reduces]
- $a$ ***has normal form*** $b$, or $b$ is a normal form of $a$, if $a$ reduces to $b$ and $b$ is a normal form.
- If $a$ has exactly one normal form (we also say ***the element*** $a$ ***has a unique normal form***), the normal form of $a$ is denoted by $a{\downarrow}$.
- An ARS ***has unique normal forms*** if every element has a unique normal form.
- $a,b$ are ***joinable***, written as $a\downarrow b$, if both $a$ and $b$ reduce to the same element. In symbols, $a\downarrow b$ if there is $x\in A$ such that $a\stackrel{\ast}{\longrightarrow} x$ and $b\stackrel{\ast}{\longrightarrow} x$.
- $(A,\to)$ is 
  - ***Church-Rosser*** if all equivalent elements are joinable. 
  - ***confluent*** if for all $x,y,z\in A$, whenever $x$ reduces to $y$ and $z$, then $y$ and $z$ are joinable.
  - ***terminating*** if there is no infinite chain $a_0\to a_1\to\ldots$ (aka *strongly normalising*).
  - ***normalising***, or ***has normal forms***, if every element has a normal form (aka *weakly normalising*).

## References

The definitions above are standard. I used as my reference:

- Baader, Nipkow. [Term Rewriting and All That](https://zubairabid.com/Semester7/subjects/PoPL/books/TRaAT.pdf).

