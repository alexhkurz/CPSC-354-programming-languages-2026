# Quiz 2, Section 3, Feedback Form

I try to answer some questions I anticipate that will come up wrt to grading of Quiz 2. By all means, do ask me if sth is not clear. And make use of the office hours if you are in doubt about why you lost points or what some of my comments are referring to.

## Q1

Grading scheme:

- 2pt: correct answer
- 1.5pt: sth is missing in one or more [definitions](https://hackmd.io/@jweinberger/H1Pr6tzOGe)
- 1pt: answer does not show a clear understanding of what a definition is (or a lot is missing)
- 0.5pt: major problems

Some things that were missing:

- it is not enough to say that "a system is terminating if there is no loop". The system defined by the rule `a->aa` has no loop and does not terminate. (But note that the other direction is true: If a system loops then it does not terminate.)
- it is not enough to say that "a system is confluent if every peak has a valley" (without also saying what a peak is and what a valley is)
- it is not enough to say "a system has unique normal forms if all normal forms of the same element are equal" (without also saying that every element has a normal form)
- it is not enough to say that "if an ARS has UNF, then ...", the implication needs to go the other way round (or, rather, be an "if and only if")

Some common misconceptions:

- The definition of termination has nothing to do with whether the ARS is finite.
- Some terms (such as normal form, reduces, joinable) have definitions in the lecture notes, others are metaphors without technical definition (peak, valley). A definition needs to use technical terms, not metaphors. 
- More is not better. Once you write down the definition (of eg termintation), it does not improve the definition when adding more to it (such as saying "no loops" which is not wrong but is a consequence of the definition, not part of the definition (and btw, has loop been defined)).
- When asked to write a definitions, explanations are not needed. If explanations are added, it should be clear that they are not part of the definition. (Here is a metaphor that may be useful: Explanation is to Comment what Definition is to Code)

Major problems:
- Introducing your own (undefined) metaphors in what is meant to be a definition.
- Words like "basically" and "essentially" can be warning signs that the aim to write a definition will not be achieved. 

## Q2

half a point per row

## Q3

The correct answer is:

- The row claims that "there is no example that has UNF and not C". This is logically equivalent to saying that "UNF implies C".

You got full points if you stated one side of the equivalence. For example, "the row asked for a counterexample to the theorem" got full points.

You didnt get full points if you answer addressed Q4 instead.

If you think I misunderstood your answer to Q3 or Q4, feel free to come to office hours. It was not always easy to read and understand what you were trying to express.

## Q4

The easiest proof uses contradiction.

Assume your ARS has UNF but is not confluent. 
Then you can find an $a$ the reduces to both $b$ and $c$ with $b\not=c$. 
By UNF, $b$ and $c$ have normal forms and because these normal forms are normal forms of $a$, these normal forms must (by uniqueness) be equal, contradicting non-confluence.

**Remark:** When you argue for sth, you need to make sure to not confuse

$A\Rightarrow B$

and

$B\Rightarrow A$

Our human brains do associative memory and are really bad at this ... they require constant scrutiny.

To see how bad it can get consider the law of contraposition.

$A\Rightarrow B$ is equivalent to $\neg B\Rightarrow  \neg A$.

Here is a famous example:

"What doesnt kill me makes me stronger" is logically equivalent to "What doesnt make me stronger kills me."

Contraposition is one of the most powerful tools to unmask reasoning mistakes. 

It can be fun to play with examples and slightly rephrase them. Here are a few:

| Original | Contrapositive |
|---|---|
| "What doesn't kill you makes you stronger" | "What weakens you kills you" |
| "If you have nothing to hide, you have nothing to fear" | "If you have something to fear, you have something to hide" |
| "Hard work leads to success" | "If you fail, you didn't work hard" |
| "Only the good die young" | "If you die old, you are bad" |
| "If you're smart you'll agree with me" | "If you don't agree with me, you're not smart" |

It is interesting to think about why the meaning seems to shift even if the logical content doesn't.