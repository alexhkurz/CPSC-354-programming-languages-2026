# Quiz 3, Section 3, Feedback Form

The most important takeaway from this quiz: Revise again the notions of equivalence relation, eqivalence class, and how they relate to the property UNF.

## Model this process as an ARS

Remark: To answer you have to remember that an ARS is of the form $(A,R)$ and you have to specify $A$ and $R$ in the form we learned in class.

## Why does the ARS terminate

Answer: Because the length of the string deacreases with each reduction.

Remark: Remember my excursion on the difference between definition and explanation? Here you are asked to give an explanation. It is ok to repeat the definition of termination, but a definition on its own does not answer the question.

Remark: Remember from the table from week 2 that an ARS can have normal forms without terminating.

## What is the definition of a normal form

Remark: See lecture notes.

Remark: It is important to distinguish language that has been defined (such as "reducible") from language that has not (such as "simplified"). You may think that this is pedantic, and it is, but knowing when to be pedantic is important for solid engineering.

## What are the normal forms in this example

Remark: I think everybody got this right

## Find an invariant

Answer:

- (number of b plus two times the number of c) mod 3
- then check that for all rules this number is the same on the left and the right of the arrow (that is, the number is the same before and after the reduction)

Remark: The definition of an invariant $I$ does not mention reductions. $I$ maps words to values. The reductions only enter when one shows that the value of $I$ doesnt change when a reduction takes place.

## Describe the equivalence classes

Answer: The equivalence classes are given by 

- (number of b plus two times the number of c) mod 3

that is, there is one equivalence class for 0, one for 1, and one for 2

## Why does the ARS have UNF

Short Answer: All normal forms are in different equivalence classes.

long Answer:
- We know from above that every word has a normal form.
- It remains to show that these normal forms are unique.
    - the empty word is in the euqivalence class of 0
    - b is in the equivalence class of 1
    - c is in the equivalence class of 2
    - now uniqueness follows from the fact that every equivalence class has only one normal form