---
tags: programming languages
---

# HW4 solutions: Concrete Syntax Trees

The format follows `123.md`: for each string we first draw the **abstract syntax tree** that the usual rules of arithmetic suggest, and then the unique derivation tree of the grammar — the **concrete syntax tree** — that produces the string.

We use the context-free grammar

```
Exp -> Exp '+' Exp1
Exp -> Exp1
Exp1 -> Exp1 '*' Exp2
Exp1 -> Exp2
Exp2 -> Integer
Exp2 -> '(' Exp ')'
```

`Exp` is the start symbol; `Integer` produces the numerals. The three levels `Exp` / `Exp1` / `Exp2` make `*` bind tighter than `+`, and the left-recursive rules make both operators associate to the left.

## Expression: `2+1`

Using the usual arithmetic precedence, the string `2+1` corresponds to the abstract syntax tree

```mermaid
graph TD
    A["'+'"] --> B["'2'"]
    A --> C["'1'"]
```

Given the string `2+1` and the grammar, the only concrete syntax tree that produces the string is:

```mermaid
graph TD
    e0["Exp"] --> eL["Exp"]
    e0 --> plus["'+'"]
    e0 --> e1R["Exp1"]
    eL --> e1L["Exp1"]
    e1L --> e2L["Exp2"]
    e2L --> int2["Integer"]
    int2 --> n2["'2'"]
    e1R --> e2R["Exp2"]
    e2R --> int1["Integer"]
    int1 --> n1["'1'"]
```

Note that both operands are wrapped in the chain `Exp -> Exp1 -> Exp2 -> Integer`. The left operand is an `Exp`, the right operand only an `Exp1`: this asymmetry is what will make `+` associate to the left in longer expressions.

## Expression: `1+2*3`

Using the usual arithmetic precedence, the string `1+2*3` corresponds to the abstract syntax tree

```mermaid
graph TD
    A["'+'"] --> B["'1'"]
    A --> C["'*'"]
    C --> D["'2'"]
    C --> E["'3'"]
```

Given the string `1+2*3` and the grammar, the only concrete syntax tree that produces the string is:

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

The right operand of `+` must be an `Exp1`, so the `*` is forced to sit under that `Exp1`. There is no concrete syntax tree in which `+` sits under `*`: the precedence of `*` over `+` is built into the grammar.

## Expression: `1+(2*3)`

Using the usual arithmetic precedence, the string `1+(2*3)` corresponds to the same abstract syntax tree as `1+2*3`:

```mermaid
graph TD
    A["'+'"] --> B["'1'"]
    A --> C["'*'"]
    C --> D["'2'"]
    C --> E["'3'"]
```

But the *string* is different, and the concrete syntax tree must account for every symbol, including the parentheses:

```mermaid
graph TD
    e0["Exp"] --> eL["Exp"]
    e0 --> plus["'+'"]
    e0 --> e1R["Exp1"]
    eL --> e1L["Exp1"]
    e1L --> e2L["Exp2"]
    e2L --> int1["Integer"]
    int1 --> n1["'1'"]
    e1R --> e2R["Exp2"]
    e2R --> lp["'('"]
    e2R --> eIn["Exp"]
    e2R --> rp["')'"]
    eIn --> e1In["Exp1"]
    e1In --> e1InL["Exp1"]
    e1In --> star["'*'"]
    e1In --> e2c["Exp2"]
    e1InL --> e2b["Exp2"]
    e2b --> int2["Integer"]
    int2 --> n2["'2'"]
    e2c --> int3["Integer"]
    int3 --> n3["'3'"]
```

The parentheses appear in the concrete syntax tree because of the rule `Exp2 -> '(' Exp ')'`. So `1+2*3` and `1+(2*3)` have the same abstract syntax tree but different concrete syntax trees.

## Expression: `(1+2)*3`

Using the usual arithmetic precedence, the string `(1+2)*3` corresponds to the abstract syntax tree

```mermaid
graph TD
    A["'*'"] --> B["'+'"]
    A --> C["'3'"]
    B --> D["'1'"]
    B --> E["'2'"]
```

Given the string `(1+2)*3` and the grammar, the only concrete syntax tree that produces the string is:

```mermaid
graph TD
    e0["Exp"] --> e1["Exp1"]
    e1 --> e1L["Exp1"]
    e1 --> star["'*'"]
    e1 --> e2R["Exp2"]
    e1L --> e2L["Exp2"]
    e2L --> lp["'('"]
    e2L --> eIn["Exp"]
    e2L --> rp["')'"]
    eIn --> eInL["Exp"]
    eIn --> plus["'+'"]
    eIn --> e1In["Exp1"]
    eInL --> e1a["Exp1"]
    e1a --> e2a["Exp2"]
    e2a --> int1["Integer"]
    int1 --> n1["'1'"]
    e1In --> e2b["Exp2"]
    e2b --> int2["Integer"]
    int2 --> n2["'2'"]
    e2R --> int3["Integer"]
    int3 --> n3["'3'"]
```

The string starts with `'('`, so the outermost operator cannot be `+`. The start symbol must take `Exp -> Exp1`, and that `Exp1` is the product. The parentheses are what allow a `+` to appear *under* a `*`.

## Expression: `1+2*3+4*5+6`

Left-associative `+` reads the string as `((1+(2*3))+(4*5))+6`, that is, as the abstract syntax tree

```mermaid
graph TD
    p0["'+'"] --> p1["'+'"]
    p0 --> n6["'6'"]
    p1 --> p2["'+'"]
    p1 --> t45["'*'"]
    p2 --> n1["'1'"]
    p2 --> t23["'*'"]
    t23 --> n2["'2'"]
    t23 --> n3["'3'"]
    t45 --> n4["'4'"]
    t45 --> n5["'5'"]
```

Given the string `1+2*3+4*5+6` and the grammar, the only concrete syntax tree that produces the string is:

```mermaid
graph TD
    e0["Exp"] --> e1["Exp"]
    e0 --> p0["'+'"]
    e0 --> r0["Exp1"]
    e1 --> e2["Exp"]
    e1 --> p1["'+'"]
    e1 --> r1["Exp1"]
    e2 --> e3["Exp"]
    e2 --> p2["'+'"]
    e2 --> r2["Exp1"]
    e3 --> e3a["Exp1"]
    e3a --> e3b["Exp2"]
    e3b --> i1["Integer"]
    i1 --> n1["'1'"]
    r2 --> r2L["Exp1"]
    r2 --> s2["'*'"]
    r2 --> r2R["Exp2"]
    r2L --> r2b["Exp2"]
    r2b --> i2["Integer"]
    i2 --> n2["'2'"]
    r2R --> i3["Integer"]
    i3 --> n3["'3'"]
    r1 --> r1L["Exp1"]
    r1 --> s1["'*'"]
    r1 --> r1R["Exp2"]
    r1L --> r1b["Exp2"]
    r1b --> i4["Integer"]
    i4 --> n4["'4'"]
    r1R --> i5["Integer"]
    i5 --> n5["'5'"]
    r0 --> r0b["Exp2"]
    r0b --> i6["Integer"]
    i6 --> n6["'6'"]
```

The left spine is the nested `Exp -> Exp '+' Exp1` productions: the left-recursive rule is what makes `+` associate to the left. Each right-hand `Exp1` is either a product (`2*3`, `4*5`) or the final numeral (`6`).
