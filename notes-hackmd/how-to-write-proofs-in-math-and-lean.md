# How to Write Proofs in Math and in Lean

This brief note shows how to translate between formal Lean  proofs and ordinary mathematics proofs at the hand of an example from the Lean Natural Number Game.

## Tutorial World Level 8/8

https://adam.math.hhu.de/#/g/leanprover-community/nng4/world/Tutorial/level/8

![image](https://hackmd.io/_uploads/HyLan55s6.png =200x)

How do we find a proof in Lean for this? 

Here is a method.

### Step 1: Write out the proof in Math

Let us forget about Lean first. How would we write that out in Math[^math]?

There are several ways to do this. Here is one: [^latex1]

$$
\begin{align*}
2+2 &= SSO + SSO & \text{ def of } 2\\
&= S(SSO + SO) & \text{ def of } + \\
&= SS(SSO + O) & \text{ def of } + \\
&= SSSSO & \text{ def of } + \\
&= SSS1 & \text{ def of } 1 \\
&= SS2 & \text{ def of } 2 \\
&= S3 & \text{ def of } 3 \\
&= 4 & \text{ def of } 4 \\
\end{align*}
$$

Here $S$ is successor (Lean: `succ`).[^successor]

### Step 2: Mapping Math to Lean

| Math | Lean | 
|:---:|:---:|
|def of 1 | `one_eq_succ_zero`
|def of 2 | `two_eq_succ_one`
|def of 3 | `three_eq_succ_two`
|def of 4 | `four_eq_succ_three`
|def of + | `add_zero`
|def of + | `add_succ`

### Step 3: Translate from Math to Lean

The aim is to translate Step 1 using the dictionary in Step 2.

```{Lean}
repeat rw [two_eq_succ_one]
repeat rw [one_eq_succ_zero]
repeat rw [add_succ]
rw [add_zero]
rw [four_eq_succ_three]
rw [three_eq_succ_two]
rw [two_eq_succ_one]
rw [one_eq_succ_zero]
rfl
```

### Step 4: Translate from Lean to Math

This step is optional, but for a full understanding of Lean one needs to be able to perform it.[^latex2]

$$
\begin{align*}
SSSS0&=SSSS0 & \text{rfl} \\
SSSS0&=SSS1 & \text{rw [one eq succ zero]} \\
SSSS0&=SS2 & \text{rw [two eq succ one]} \\
SSSS0&=S3 & \text{rw [three eq succ two]} \\
SSSS0&=4 & \text{rw [four eq succ three]} \\
SSS(S0+0) &= 4 & \text{rw [add succ]}\\
SS0 + SS0 &= 4 & \text{rw [add succ]}\\
S1 + S1 & = 4 & \text{repeat rw [one eq succ zero]}\\
2+2 &= 4 & \text{repeat rw [two eq succ one]}\\
\end{align*}
$$

This now matches the proof from Step 3 line by line, but you need to reverse the order as Lean works from the goal to the axioms whereas Math is usually written from the axioms (assumptions) to the conclusion.

### Questions

- Why do we work in Lean backwards from the goal instead of forwards like in Math?
- Could one mechanize Step 3, the translation from Math to Lean? What are the possibilities for this? What do you think would be the main hurdle?
- When is it useful to think of Math as a programming language? What are the main differences between Math and a programming language?

[^copying]: Of course, sometimes it is appropriate to copy small amounts of material and then one needs to give a reference. In particular, uses of LLMs need to be acknowledged.

[^math]: "Math" is capitalized to emaphasize that both Math and Lean are languages. Lean is a programming language. Math is not a programming language, but it is insightful to think about Math as a programming language (or specification language) whenever that makes sense.

[^successor]: Notation for successor varies. Lean and NNG use `succ`. We (and Hofstadters GEB) use `S`. Moshier’s LNDM (*Contemporary Discrete Mathematics*, Canvas) writes the successor of \(n\) as \(n↷\), and notes that \(S(n)\) or \(Sn\) are also common (see LNDM pp. 16–21). The addition rules are the same in all three: \(m+0=m\) and \(m+\mathrm{succ}(k)=\mathrm{succ}(m+k)\).

[^latex1]: To typset this in markdown latex use:
	```
	\begin{align*}
	2+2 &= SSO + SSO & \text{ def of } 2\\
	&= S(SSO + SO) & \text{ def of } + \\
	&= SS(SSO + O) & \text{ def of } + \\
	&= SSSSO & \text{ def of } + \\
	&= SSS1 & \text{ def of } 1 \\
	&= SS2 & \text{ def of } 2 \\
	&= S3 & \text{ def of } 3 \\
	&= 4 & \text{ def of } 4 \\
	\end{align*}
	```

[^latex2]: Spaces instead of underscores in the Lean names here so the display works in both HackMD and Markdown preview (KaTeX); the real identifiers are as in Steps 2–3 (e.g. `one_eq_succ_zero`).

