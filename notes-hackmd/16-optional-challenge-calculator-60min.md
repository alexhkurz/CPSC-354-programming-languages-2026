---
tags: programming languages
---

# Optional Challenge: A Calculator in 60 Minutes (PL 2026)

## Introduction

In this course we want to learn how to create our own programming language.

- In Programming Assignment 1 we develop a calculator using a [context free grammar](https://hackmd.io/@jweinberger/ByEfEFdFzl),
- starting from [this calculator implementation](https://codeberg.org/alexhkurz/calculator-2024).
    
This optional challenge is a guided tour on how to use a coding assistant in order to recreate our starting point.

It is recommended to do this exercise using standard tools, but **without copying code from the internet**.

We allow ourselves to use standard libraries (such as [Lark](https://github.com/lark-parser/lark)) and standard tools (such as Python, Google search, stackoverflow, LLMs, coding assistant), but we will not copy code from other sources.

An important learning outcome will be the following. 

- **How to use LLMs to create your own tutorial while working on a project.**
- Never use an LLMs to only generate code. Always **prioritize your own learning over the quality of the product**.

Ok, now let's get started.

## A Calculator with Parser Generator in 60 min

(Times are estimates and don't take time for tangents into account.)

**Activity (10 min):** Start with the [Lark documentation](https://lark-parser.readthedocs.io/en/stable/) and try to get an idea of how to implement in Lark the grammar from hw4. Start from the ambiguous grammar that doesn't have order of precedence.

```grammar
Exp -> Exp '+' Exp
Exp -> Exp '*' Exp
Exp -> Integer
```

**Activity (10 min):** Create a file `calculator.py`, use an LLM (e.g. through Cursor or Copilot or Devin etc.) for the grammar above and ask it to create a parser/calculator for the grammar. Test your calculator on various expressions. 

**Question:** Explain the meaning of the symbol `->` in your Lark grammar (if there is one). Hint: The `->` in Lark has a different meaning than the `->` in standard CFG notation.

**Activity (10 min):** Use e.g. Copilot or Cursor to create yourself a tutorial that answers all the questions you may have about grammars, Lark, etc.

**Activity (10 min):** Which expressions does your calculator get right and which does it get wrong? What is the easiest way to repair the errors?

**Activity (10 min):** Refactor your code so that the grammar is in a separate file called `grammar.lark`. Your calculator should now use a parser generated through Lark.

**Activity (5 min):** Refactor the code so that the transformer computes the AST and a separate eval function does the evaluation. Make sure that the AST does not contain parentheses.

**Activity (5 min):** Add a function that pretty-prints the AST.

---

If you want to use a venv consider

```bash
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install lark-parser
```

Save this file as `setup.sh` and then run `source setup.sh` (this works with Linux and MacOS and WSL).
