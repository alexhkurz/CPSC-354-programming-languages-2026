# CPSC-354 2026: Homework 3, Solution

https://hackmd.io/@jweinberger/r1q6RMyKMx#Exercise-3

We interleave the answers into the questions.

### Exercise 3

Rewrite rules are

        aa -> a
        bb -> b
        ba -> ab
        ab -> ba
        
- Why does the ARS not terminate?

    > Answer: Due to the two rules `ba -> ab` and `ab -> ba`, there is an infinite computation `ba -> ab -> ba -> ab -> ...`

    > Comment: The two rules `ba -> ab` and `ab -> ba` can be memorized in English as saying "the order of the letters doesnt matter".

    > Bonus Questions: What are the equivalence classes of the ARS that only has the two rules `ba -> ab` and `ab -> ba`? What are its normal forms?
- What are the normal forms?
    > Answer: $a$, $b$, $\varepsilon$.

    > Comment: Don't forget https://hackmd.io/@jweinberger/r1q6RMyKMx#The-Empty-Word 
- What are the equivalence classes?
    > Answer: There are four equivalence classes.
    >
    > | Equivalence class | Normal form | Characterization | Examples |
    > |:---:|:---:|:---|:---|
    > | $[\varepsilon]$ | $\varepsilon$ | the empty word | $\varepsilon$ |
    > | $[a]$ | $a$ | non-empty words of only $a$'s | $a, aa, aaa, \ldots$ |
    > | $[b]$ | $b$ | non-empty words of only $b$'s | $b, bb, bbb, \ldots$ |
    > | $[ab]$ | none | words with at least one $a$ and one $b$ | $ab, ba, aab, abb, \ldots$ |
    >

    > Comment:   
    > - [Equivalence Relations](https://hackmd.io/@alexhkurz/S1E449agkg#Equivalence-Relations)
    > - [Equivalence Classes](https://hackmd.io/@alexhkurz/S1E449agkg#Equivalence-Classes)

- Modify the ARS so that it is terminating, has unique normal forms (and still the same equivalence relation).
  > Answer: Drop the rule `ab -> ba` but keep `ba->ba` and the other two.
  > Now `ab` is also a normal form.
- Describe the specification implemented by the ARS. 
   > Answer: The algorithm decides the question which of the following properties holds of any given input word: Is the word empty, or does it have only `a`s or does it have only `b`s or does it have both `a`s and `b`s? 
 