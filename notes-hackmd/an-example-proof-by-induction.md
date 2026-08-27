---
tags: Lean
---

# An Example Proof by Induction

This is the Math [^Math] proof corresponding to [this](https://adam.math.hhu.de/#/g/leanprover-community/nng4/world/Addition/level/1) Lean example. In particular, for the proof to make sense, one needs to know that $+$ is defined as follows in Lean. 

$$
\begin{gather*}
a+0=a\\
a + Sb = S(a+b)
\end{gather*}
$$

One also needs to know that at this stage, we have not proved yet that $+$ is commutative, so we do not know that $0+n=n+0$. In other words, while $n+0=n$ follows immediately from the definition of $+$, the equation $0+n=n$ does not.

Now the claim and the proof:

**Claim:** $0+n=n$ for all $n\in \mathbb N$.

*Proof:* We prove $0+n=n$ for all $n\in\mathbb N$ by induction on $n$. [^latex]

Case $n=0$: 

$$
\begin{align*}
0+0 &= 0 & \text{def of +}
\end{align*}
$$

Case $n=S\,k$: The induction hypothesis is $0+k=k$. 

$$
\begin{align*}
0+ Sk &= S(0+k) & \text{def of +}\\
&= Sk & \text{induction hypothesis}\\
\end{align*}
$$

QED

[^Math]: I capitalize here, to make an analogy between (traditional) Math and Lean as languages to write proofs. One shouldn't push this analogy too far though as there are also important differences (which?).

[^latex]: Here is the Latex code for this example:
	```latex
	Case $n=0$: 
	\begin{align*}
	0+0 &= 0 & \text{def of $+$}
	\end{align*}
	
	Case $n=S\,k$: 
	\begin{align*}
	0+ Sk &= S(0+k) & \text{def of $+$}\\
	&= Sk & \text{induction hypothesis}\\
	\end{align*}
	```
    Markdown Latex may need dollars around the math as in
    ```latex
	Case $n=0$: 
    
    $$
	\begin{align*}
	0+0 &= 0 & \text{def of $+$}
	\end{align*}
    $$
	
	Case $n=S\,k$: 
    
    $$
	\begin{align*}
	0+ Sk &= S(0+k) & \text{def of $+$}\\
	&= Sk & \text{induction hypothesis}\\
	\end{align*}
    $$
	```