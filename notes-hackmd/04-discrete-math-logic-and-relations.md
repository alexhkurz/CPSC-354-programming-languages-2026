$\newcommand{\sem}[1]{[\![#1]\!]}$ 

# Discrete Mathematics: Logic and Relations

A revision guide for some elements of discrete mathematics. See eg Moshier, Lecture Notes on Discrete Mathematics, 

- Chapter 8.3, Relations
- Chapter 9, Injections, Surjections, Bijections
- Chapter 11, Cartesian Products and Binary Relations, 
- Chapter 12, Equivalence Relations, Partitions, Quotients

The aim of this note is to review just enough discrete mathematics in order to be able to understand the concepts of 
- "abstraction as a quotient by an equivalence relation" [^abstraction] and 
- "rewriting to normal form" [^rewriting] as a model of computation. 
- "meaning of a formal languages as a mapping  to a semantic domain". [^semantics] 

All these notions can be connected, clarified and formalised with the help of a little discrete maths, which we will review now.  [^discretemath]

[^abstraction]: [What is Abstraction?](https://hackmd.io/@alexhkurz/HJONiNfCw)

[^rewriting]: [Rewriting and the Call Stack](https://hackmd.io/@alexhkurz/HJiulVg0U).

[^semantics]: [Operational and Denotational Semantics](https://hackmd.io/@alexhkurz/Hkf6BTL6P).

For the main part, we only need to understand the concept of  reflexive and transitive (and symmetric) closure of a relation. But let us get started with a review of some helpful notation from set theory and logic.

[Logic](https://hackmd.io/@alexhkurz/SkIp4pL3w)

[Set Theory](https://hackmd.io/@alexhkurz/B1QX46L3P)


## Relations

If you are familiar with databases then a (finite) relation is really very much the same as a table in a database. For our purposes, we actually only need binary relations, that is, tables that have two columns (attributes).

Anyway, we don't need to think about databases. The mathematical definition is that a **relation**[^relation] $R$ on a set $A$ is a subset of $A\times A$, in symbols

$$R\subseteq A\times A.$$

**Notation:** By convention, we also write $aRb$ instead of $(a,b)\in R$, or also $R(a,b)$, which in turn may be abbreviated to $Rab$. When drawing pictures we also write this as

$$a\stackrel{R}{\longrightarrow} b$$
 
which we abbreviate to 

$$a\stackrel{}{\longrightarrow} b$$

if there is only one relation around anyway.

**Remark:** Later we will take $R$ to be the relation of "one-step computation", or rewriting, as we called it, but for now we make no assumptions on $A$ and $R$.

We need to know what it means for a relation to be reflexive, symmetric, and transitive.

**Defininition:** Assume $R\subseteq A\times A$.  The relation $R$ is said to be

- ***reflexive*** if 
$$ xRx $$
for all $x\in A$.

- ***symmetric*** if 
$$ xRy  \ \Rightarrow \ yRx$$
for all $x,y\in A$.

- ***transitive*** if 
$$ xRy  \ \& \ yRz \ \Rightarrow \ xRz$$
for all $x,y,z\in A$.

**Example:** 
- The $<$-relation on numbers is transitivie but neither reflexive nor symmetric.
- The $\le$-relation on numbers is reflexive and transitive but not symmetric.
- A relation that is symmetric and transitive but not necessarily reflexive is called a [partial equivalence relation](https://en.wikipedia.org/wiki/Partial_equivalence_relation). The linked article contains some references to applications to the semantics of programming languages.
- The relation $a\equiv b\ ({\rm mod} \  n)$ of [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic) is reflexive, transitive and symmetric.
- The relation of "being siblings" is symmetric but not reflexive (hence also not transitive).

**Homework:** 
- Family relationships and social networks: Check parent, ancestor, sibling, having the same parents, friend, following, being a member of the same group, etc for reflexivity, transtivity and symmetry.

**Exercise:**
- Is it true that a relation which is symmetric and transitive is also reflexive?
- Is the empty relation symmetric and transitive? Is it reflexive?

## Transitive Closure

We have seen examples of transitive closure above.

- Ancestor is the transitive closure of parent.
- On natural numbers (or integers), "greater than" is the transtive closure of the successor relation. [^gtfrac]:

[^gtfrac]: What about fractions?

More generally, given a relation $R$, two elements $a,b$ are in the transitive closure $R^+$ of $R$ if there is a sequence of elements $a_1,\ldots a_n$ such that

$$ aRa_1, a_1Ra_2,\ldots a_n R b$$

or, shorter,

$$ aRa_1Ra_2\ldots a_n R b.$$

**Remark:** $R^+$ can be defined recursively as follows.
- $aR^+b$ if $aRb$,
- $aR^+b$ if there is $c$ such that $aRc$ and $cR^+b$.

Note how this is similar to a recursive definition in, say, Haskell.

Another way of expressing the same idea is as follows.

**Definition:** Let $R\subseteq A×A$. 
- The transitive closure $R^+$ of $R$ is the smallest transitive relation containing $R$.
- The reflexive and transitive closure $R^*$ of $R$ is the smallest reflexive and transitive relation containing $R$.

**Remark:** If $R$ is a relation of "one-step computation" we often write $\to$ instead of $R$ and $\stackrel{\ast}{\to}$ for the reflexive and transitive closure. 

**Homework:** Let $(A,R)$ be an ARS. The relation $R$ can be represented by an [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix) $M$ defined as
$$M_{ab}=\left\{\begin{array}{lr}
1 & \textrm{if $(a,b)\in R$}\\ 
0 & \textrm{if $(a,b)\notin R$} 
\end{array}\right.$$
Describe an algorithm that computes the transitive closure of $R$ via matrix multiplication.

## Equivalence Relations

Equivalence relations and equivalence classes are one of the most important concepts in mathematics and computer science. It was discovered surprisingly late, as far as I know by Dedekind around 1880. [^Dedekind] For a general introduction see my notes on [What is Abstraction?](https://hackmd.io/@alexhkurz/HJONiNfCw)

**Definition:** An  ***equivalence relation*** is a relation that is reflexive, transitive and symmetric. The **equivalence closure** $\equiv_R$ of $R$ is the smallest reflexive, symmetric, transitive relation containing $R$.

**Remark:** We will be interested in the situation where $\equiv_R$ specifies the  equational properties of a computational problem and $R$ describes a non-determinstic algorithm solving the problem. 

**Notation and Terminology:** If $R$ is an equivalence relation it is often written as $\equiv$ or $\approx$ or any other symbol that emphasises the analogy with equality.  If we write $\to$ instead of $R$, we write $\stackrel{\ast}{\leftrightarrow}$ for the equivalence closure

Equivalence relations solve the problem of how to account for the fact that two things can be considered equal and different at the same time.

For example, $2+3$ and $1+4$ are different as expressions, but they are equal as numbers. Now we can just say they are equivalent wrt an appropriate equivalence relation.

**Example (fractions):** Define $\frac a b\equiv \frac c d$ if $a\cdot d = b\cdot c$. Show that every fraction is equivalent to its simplified fraction.

**Example (modular arithmetic):** Let $n\ge 2$ be a natural number. Define $a\equiv b$ if there is an integer $i$ such that $b-a=i \cdot n$. Show that 
$$
\frac{a\equiv b\quad\quad c\equiv d}{a+c\equiv b+d}
\quad\quad
\quad\quad
\frac{a\equiv b\quad\quad c\equiv d}{a\cdot c\equiv b\cdot d}
$$ 
The relation $\equiv$ is often called *congruence* modulo $n$. Congruence relations are equivalence relations that satisfy additional compatibility properties with operations such as the two above for addition and multiplication.

**Example (integers):** Define an INTEGER as a pair $(n,m)$ of natural numbers. Define $(n,m)\equiv(n',m')$ if $n+m'=n'+m$. Define zero as $(0,0)$ and $(n,m)+(n',m')=(n+n',m+m')$. Show how to define negation on INTEGERs and show that it satisfies the usual equations one would expect from integers.

## Quotienting by an Equivalence Relation

The purpose of an equivalence relation is that it makes precise when it is safe to consider two different things equal. In one of the examples above, we defined an equivalence relation $\equiv$ such that $\frac 3 2 \equiv \frac 6 4$. It is more common to write $\frac 3 2 = \frac 6 4$. In this section we will see how to give this notation a rigorous mathematical foundation.

If $\equiv$ is an equivalence relation on $A$, then $\equiv$ partitions $A$ into equivalence classes. For $a\in A$, the **equivalence class** of $a$ is denoted by $[a]$ or $[a]_\equiv$ and defined as 

$$[a]_\equiv = \{b\in A \mid a\equiv b\}$$

To say that the equivalence classes partition $A$ is to say that equivalences classes are disjoint and cover all of $A$. We will come back to this below.

We can now form the set of equivalence classes which is written as $A/R$ and defined as

$$A/{\equiv} \ \stackrel{\rm def}{=} \ \{[a]_\equiv \mid a\in A \}$$

**Remark (Partition):** Equivalence relations on $A$ are in bijective correspondence with partitions of $A$. A ***partition*** of $A$ is a set of subsets of $A$ that are pairwise disjoint and cover all of $A$.[^partition] Given an equivalence relation, its equivalence classes form a partition. Conversely, every partition defines the equivalence relation of "being in the same part".

**Remark (Equivalence relation/partition of a function):** Every function $f:A\to B$ defines an equivalence relation via $a\equiv a' \Leftrightarrow f(a)=f(a')$. In other words, $f$ partitions $A$ into the subsets of elements that are identified by $f$.  

**Example:** Equality is an equivalence relation. In fact, equality is the smallest equivalence relation. There is also a largest equivalence relation (which is it?).

**Notation and Terminology:** The set $A/{\equiv}$ is also called $A$ ***modulo*** $\equiv$ or *$A$ quotiented by $\equiv$* or ****the quotient of*** $A$ by $\equiv$*. 

Let us review the examples above.

**Example (fractions):** The set of non-negative fractions $\mathbb Q$ can be implemented as a set of equivalence classes. The set $A$ is $\mathbb N\times\mathbb N_+$ where $N_+$ is the positive integers and the equivalence relation in question is the one (defined above) which takes care of the fact that, eg, 1/2 = 2/4.

**Example (modular arithmetic):** On the integers $\mathbb Z$, the relation $a\equiv b$ of congruence modulo $n$ is an equivalence relation. The set of equivalence classes is denoted by $\mathbb Z/n\mathbb Z$. The operation of "dividing by $n\mathbb Z$" has some properties similar to division on numbers, see eg the [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)  which explains some of the terminology just introduced.


**Example (integers):** The set of integers can be represented as a quotient of $\mathbb N\times\mathbb N$ by an equivalence reation (defined above).





The following exercise is crucial to understand equivalence classes.

**Exercise:** Show that every equivalence relation $\equiv$ on $A$ partitions $A$, that is,
- A is the union of its equivalence classes, symbolically, $A = \bigcup_{a\in A} A/R$
- any two different equivalence classes are disjoint, ie, $[a]\not=[b] \Rightarrow [a]\cap[b]=\emptyset$


## Functions

As I said, I assume that the notion of a function is familiar, either form high-school or from a first semester discrete maths course. But we can review some terminology quickly.

To begin at the beginning, a function $f:A\to B$ is often defined to be a relation $f\subseteq A\times B = \{(a,b)\mid a\in A,b\in B\}$, which, moreover, is 
- *single-valued*, that is, $(a,b)\in f$ and $(a,b')\in f$ implies $b=b'$ and is 
- *total*, that is, for all $a\in A$ there is $b\in B$ such that $(a,b)\in f$. 

These two properties together say that for all $a\in A$ there is one and only one related $b\in B$ and this is the element that is, by convention, written as $f(a)$. 

We will also need further properties that functions may have. A function is called
- ***injective***, or *one-to-one*, if $f(a)=f(a')$ implies that $a=a'$,
- ***surjective***, or *onto*, if for all $b\in B$ there is $a\in A$ such that $f(a)=b$,
- ***bijective***, if it is injective and surjective.

If we have a bijection between two sets, then the two sets can be considered equal up to the names of their elements. Intuitively, a bijection is like a dictionary that relates every word in one language to exactly one corresponding word in the other.

We will also need that a function 
$$f:A\to B$$ 

can be extended to subsets of $A$ and $B$. We define
- the ***direct image of $X\subseteq A$ under $f$*** as $\ \ f[X]\ \stackrel{\rm def}{=}\ \{f(x) \mid x\in X\}$
- the ***inverse image of $Y\subseteq B$ under $f$*** as $\ \ f^{-1}(Y)\ \stackrel{\rm def}{=}\ \{a\in A \mid f(a)\in Y\}$ 

**Remark (Partition of a function):** Every function $f:A\to B$ defines a partition $f^{-1}(b)_{b\in B}$ on $A$. The sets $f^{-1}(b)$ are sometimes known as the fibres over $b$.

## Isomorphisms

Finally, we bring everything together. First a definition.

**Definition (isomorphism):** An isomorphism is a function $f$ which has an inverse, that is, there is a function $g$ such that $f(g(y))=y$ and $g(f(x))=x$. 

**Exercise:** Show that a function is an isomorphism if and only if it is bijective.

The reason we prefer the definition of isomorphism as a map that has an inverse is that it is more abstract and also applies to situations other than sets and functions.

Each of the examples above (fractions, modulo arithmetic, integers) fits into the following picture, where the equivalence $\equiv$ and $[-]_\equiv$ have been defined above, the horizontal arrow is an isomorphism, $\mathcal L$ and $\mathcal D$ are indicated in the table below and $\sem{-}$ is left as an exercise.

![](https://i.imgur.com/tjuD3fF.png =400x200)

||$\mathcal L$|$\mathcal D$
|:---:|:---:|:---:
| fractions | $\mathbb N\times \mathbb N_+$ | $\mathbb Q$
|modulo arithmetic | $\mathbb Z$ | $\mathbb Z/n\mathbb Z$
|integers | $\mathbb N\times \mathbb N$ | $\mathbb Z$

In the case of fractions, $\mathbb Q$ is often defined to coincide with $\mathcal L/{\equiv}$. In the other cases the domain $\mathcal D$ has an independent definition and the horizontal ismorphism is not an identity, formally speaking. But we can treat it as an identity as all the structure is preserved and only the data is represented in a different way. 

[^discretemath]: I assume that students had a one semester course on discrete maths. But in many discrete-maths-texts relations only appear in the "second semester" part. For example in the widely used book "Discrete Mathematics and Its Application" by Rosen, relations only start on page 374. Btw, the book could be a good place to review some discrete maths.


[^relation]: It is common to abbreviate $A\times A$ by $A^2$. If we need to emphasise that $R$ is a susbset of  $A^2$ as opposed to a subset of $A^n$ for some other $n\in\mathbb N$, we call $R$ a "2-ary" relation or a **binary relation**.

[^Dedekind]: More information is available in this article on [The Early Development of Set Theory](https://plato.stanford.edu/entries/settheory-early/#Emer). By the way, Dedekind was also the guy who defined integers and rationals as equivalence classes. You are asked to work on this in [this exercise](https://hackmd.io/@alexhkurz/HJQNfRbtX#Exercise-Fractions).

[^partition]: In symbolic notaion, a partition of $A$ is a collection $(A_i)_{i\in I}$ of subsets of $A$ such that $i\not=j \ \Rightarrow A_i\cap A_j=\emptyset$ and $\bigcup_{i\in I} A_i = A$.

