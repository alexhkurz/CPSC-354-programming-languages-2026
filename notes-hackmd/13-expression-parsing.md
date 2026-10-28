# Expression Parsing (a background reader)

See [Padua (2000)](https://scholar.google.com/scholar?q=The+Fortran+I+Compiler+Padua+2000) and [Knuth and Pardo (1976)](https://scholar.google.com/scholar?q=Early+Development+of+Programming+Languages+Knuth+Pardo+1976), both cited in [Kegler (2023)](https://jeffreykegler.github.io/personal/timeline_v3).

---

For most of human history, mathematical notation was someone else's problem. Mathematicians wrote `1 + 2 × 3` on paper, and human readers applied learned rules — multiplication before addition — to arrive at 7. Ambiguity was handled by convention, and convention was enforced by education.

Then, around 1949, [Heinz Rutishauser](https://en.wikipedia.org/wiki/Heinz_Rutishauser) at ETH Zurich tried to make a machine do it. His compiler could handle parentheses but quietly ignored precedence — `1 + 2 × 3` came out as 9. A few years later, the IT compiler at Carnegie (1956) went right-to-left by default. Donald Knuth later recorded that this "will be the most frequent single cause of errors by the users of the IT compiler." [FORTRAN](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=THE+HISTORY+OF+FORTRAN+I%2C+II%2C+AND+III+John+Backus&btnG=) (1957) finally got it right, though by a hack. [^fortran]

[^fortran]: See [Padua (2000)](https://scholar.google.com/scholar?q=The+Fortran+I+Compiler+Padua+2000). FORTRAN handled operator precedence by a substitution trick: each operator was replaced by a parenthesised version of itself, with the number of parentheses inversely proportional to its precedence — fewer for tighter-binding operators, more for looser ones — and the whole expression wrapped in the maximum number of pairs. So `1+2*3` becomes `((1))+((2)*(3))`: the + sits at nesting depth 0, the * at depth 1, and a standard bracket-first evaluator naturally evaluates `*` before `+`, giving $1+6=7$. The trick worked but was entirely hard-coded — adding a new precedence level required redesigning the substitution table — and generated needlessly verbose token streams. [Dijkstra (1961)](https://scholar.google.com/scholar?q=Algol+60+translation+Dijkstra+1961) later showed it was an inefficient instance of the general operator-precedence algorithm he was replacing. 


## Notation

| Notation | Example | Operator position |
|---|---|---|
| **Infix** | `1 + 2` | between operands |
| **Prefix** | `+ 1 2` | before operands |
| **Postfix** | `1 2 +` | after operands |

## Big Idea: Expressions Are Trees

`1 + (2 × 3)` corresponds to the tree

```
        +
       / \
      1   ×
         / \
        2   3
```

and `(1 + 2) × 3` to the tree

```
        ×
       / \
      +   3
     / \
    1   2
```

(These trees are called abstract syntax trees.)

## Trees are Nested Lists (and vice versa)

The tree

```
       f
     / | \
    f  b  f
    |    / \
    a   b   a
```
can be written as a nested list (that is, as a list of lists).

```
(f,(f,a),b,(f,b,a))
```

**Exercise:** Show how the tree can be recovered from the list.

Dropping the parenthesis as in `(f,f,a,b,f,b,a)` does not allow one to recover the tree.

On the other hand, if every operator has a fixed known arity (number of operations / arguments / children), then one can recover the tree from the list. 

Consider the following variation


```
       f
     / | \
    g  b  h
    |    / \
    a   b   a
```

which corresponds to the (nested) list:

```
(f,(g,a),b,(h,b,a))
```

**Remark**: In math this is often written as $f(g(a),b,h(b,a))$, which is really the same, up to a slightly different convention of where to put the parentheses.

Looking at the tree, we see that f has arity 3, g has arity 1, and h has arity 2 (and we can say that a,b have arity 0).

**Exercise:** Show that the tree can be recovered from the list `(f,g,a,b,h,b,a)`, using the information we have of the arities of f, g, and h.

The process of turning a tree to a nested list of just a string is called linearization. For example, the tree from the previous section was linearized to the list `(f,g,a,b,h,b,a)` which can be also written as the string `fgabhba`.

## Prefix, Infix, Postfix

In the previous section, we used the so-called prefix order to linearize the tree. In fact,  thereare three different ways to do this:

| Walk order | Visits nodes | Produces |
|---|---|---|
| **Pre-order** (node, left, right) | `+`, `1`, `×`, `2`, `3` | `+ 1 × 2 3` (prefix) |
| **In-order** (left, node, right) | `1`, `+`, `2`, `×`, `3` | `1 + 2 × 3` (infix) |
| **Post-order** (left, right, node) | `1`, `2`, `3`, `×`, `+` | `1 2 3 × +` (postfix) |

Postfix is useful in conjunction with a stack machine. 

## A Stackmachine Processing Postfix

Dijkstra's [shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) uses postfix notation together with a stack to evaluate an expression. See [Dijkstra (1961)](https://scholar.google.com/scholar?q=Algol+60+translation+Dijkstra+1961).

A stack is a last-in-first-out structure. You push things onto the top; you pop from the top. You never need to reach deeper.

Evaluating `1 2 3 × +` on a stack (top shown left):

```
Token   Action              Stack
  1     push 1              [1]
  2     push 2              [2, 1]
  3     push 3              [3, 2, 1]
  ×     pop 3 and 2         
        push 3×2=6          [6, 1]
  +     pop 6 and 1         
        push 6+1=7          [7]
```
