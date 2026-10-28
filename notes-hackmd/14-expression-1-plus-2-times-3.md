# Expression: 1 + 2 * 3

Using the usual arithmetic precedence, the string `1 + 2 * 3` corresponds to the tree

```mermaid
graph TD
    A["'+'"] --> B["'1'"]
    A --> C["'*'"]
    C --> D["'2'"]
    C --> E["'3'"]
```

In order to produce this tree algorithmically, we use the context free grammar

```
Exp -> Exp '+' Exp1
Exp -> Exp1
Exp1 -> Exp1 '*' Exp2
Exp1 -> Exp2
Exp2 -> Integer
Exp2 -> '(' Exp ')'
```

Given the string `1 + 2 * 3` and the grammar, the only tree that produces the string is:

```mermaid
graph TD
    exp0["Exp"] --> exp1["Exp"]
    exp0 --> plus["'+'"]
    exp0 --> exp10["Exp1"]
    exp1 --> exp11["Exp1"]
    exp11 --> exp20["Exp2"]
    exp20 --> int1["Integer"]
    int1 --> one["'1'"]
    exp10 --> exp12["Exp1"]
    exp10 --> star["'*'"]
    exp10 --> exp21["Exp2"]
    exp12 --> exp22["Exp2"]
    exp22 --> int2["Integer"]
    int2 --> two["'2'"]
    exp21 --> int3["Integer"]
    int3 --> three["'3'"]
```

The homework now is a bit like solving a Sudoku: Given the rules of the grammar and a string, what is the unique tree that can be fit to the string.