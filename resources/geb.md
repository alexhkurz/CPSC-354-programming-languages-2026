# Background reading: Hofstadter's *Gödel, Escher, Bach*

Douglas Hofstadter's *Gödel, Escher, Bach: an Eternal Golden Braid* (GEB) is the recommended general reading for this course. Large parts of it are — sometimes in disguise — about the same material we study: formal systems as string-rewriting, meaning as isomorphism, recursion, toy programming languages, self-reference, and the Church–Turing thesis.

The table below maps the blocks of our course to chapters of GEB (page numbers refer to the standard pagination). GEB alternates dialogues and chapters; the dialogues listed are the ones that carry technical content.

Topics marked *no direct counterpart* are not covered in the book; the pointers given are the nearest related material.

| Our topic | Topic in GEB |
|---|---|
| Week 1 — Natural Number Game: arithmetic on successors, induction, formal proofs | Ch. II *Meaning and Form in Mathematics* (pp. 46–60): the pq-system is addition on successor strings — NNG on paper; Ch. VIII *Typographical Number Theory* (pp. 204–230): formalized Peano arithmetic, including the rule of induction |
| Weeks 2–3 — Rewriting theory: axioms, rules of inference, derivations, theorems | Ch. I *The MU-puzzle* (pp. 33–41): the MIU-system, our paradigmatic string-rewriting system — axioms, production rules, derivations, decision procedures, working inside vs outside the system; Ch. III *Figure and Ground* (pp. 64–74): theorems vs nontheorems, recursive vs recursively enumerable sets |
| Weeks 4–5 — Parsing, context-free grammars, ASTs; PA1 (calculator) | Ch. V *Recursive Structures and Processes* (pp. 127–152): Recursive Transition Networks (ORNATE NOUN, FANCY NOUN) — grammar rules that call each other, with push/pop stack discipline; Ch. VI *The Location of Meaning* (pp. 158–176): coded message vs decoder — syntax vs semantics |
| Week 6 — Lambda calculus | *No direct counterpart* — GEB does not treat the λ calculus. Nearest: Ch. XIII *BlooP and FlooP and GlooP* (pp. 406–430) on designing toy languages, and Ch. V on recursion |
| Week 7 — Lean Logic Game: propositional logic, natural deduction | Ch. VII *The Propositional Calculus* (pp. 181–198): formal rules for *and/or/not/implies*, including the "fantasy rule" — reasoning inside an assumption, i.e. →-introduction; Ch. IV *Consistency, Completeness, and Geometry* (pp. 82–102) on soundness of formal systems |
| Week 8 — Church encodings: data as functions/programs | *No direct counterpart* — but the same idea, data encoded in another medium: Ch. IX *Mumon and Gödel* (pp. 246–272) on Gödel-numbering (strings and proofs encoded as numbers); dialogue *A Mu Offering* (pp. 231–245) |
| Week 9 — Fixed-point combinator Y: recursion without self-reference | Dialogue *Air on G's String* (pp. 431–437): "quining" — producing self-reference without directly naming yourself, the prose version of a fixed point; Ch. XVI *Self-Ref and Self-Rep* (pp. 495–548): quines and self-reproducing programs |
| Week 10 — PA2: writing an interpreter | Ch. X *Levels of Description, and Computer Systems* (pp. 285–310): machine language, assembly, compiler languages — levels stacked by interpretation; Ch. XIII (pp. 406–430): writing actual programs in a toy language |
| Week 11 — Recursion | Ch. V *Recursive Structures and Processes* (pp. 127–152); Ch. XIII (pp. 406–430): BlooP's bounded loops vs FlooP's unbounded loops = primitive recursive vs general recursive functions — the for/while distinction |
| Week 12 — Invariants: proving something cannot be reached | Ch. I *The MU-puzzle* (pp. 33–41): the count-of-I's invariant that shows `MU` is underivable — exactly our use of invariants to prove impossibility; Ch. III (pp. 64–74) |
| The big picture — formal systems, meaning, computability | *Introduction: A Musico-Logical Offering* (pp. 3–28); Ch. XIV *On Formally Undecidable Propositions of TNT* (pp. 438–460) and Ch. XV *Jumping out of the System* (pp. 465–479): Gödel's incompleteness proof; Ch. XVII *Church, Turing, Tarski, and Others* (pp. 559–593): Church–Turing thesis, the halting problem |

Reading advice (from previous years' notes): if you read Chapters I–V ahead of time you will keep discovering connections with the lectures. The whole of Part I is essentially our Weeks 1–7 in disguise.
