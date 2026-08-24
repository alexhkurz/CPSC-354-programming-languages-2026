# Principles of Programming Languages (PL 2026)

[![Codeberg](https://img.shields.io/badge/Codeberg-2185D0?style=for-the-badge&logo=codeberg&logoColor=white)](https://codeberg.org/alexhkurz/programming-languages-2026/)

The repository for Chapman University's CPSC 354 Programming Languages (Fall 2026).

- Quick links
    - [Lecture by Lecture](lecture-by-lecture.md)
    - [Syllabus](syllabus-long.md)
    - [Feedback for Homework](feedback-hw.md)
    - [Report](report.md)
    - [Attendance](attendance.md)
    - [Git best practices](git-best-practices.md)
    - Canvas: TBD

## Schedule (overview)

| Week | Theme | Day 1 | Day 2 |
|:---:|:---|:---|:---|
| 1 | **NNG** | General introduction | Lean NNG, hw1 (NNG) |
| 2 | **RT1** | Solution hw1, Rewriting Theory | Rewriting Theory, hw2 (RT1) |
| 3 | **RT2** | Solution hw2, quiz 1 (NNG) | Rewriting Theory, hw3 (RT2) |
| 4 | **Parsing** | Solution hw3, quiz 2 (RT1) | CFG, concrete & abstract syntax trees, hw4 |
| 5 | **PA1** | Solution hw4, quiz 3 (RT2) | Lab on PA1 (calculator), hw5 |
| 6 | **Lambda Calculus (LC)** | Solution hw5, quiz 4 (parsing) | Syntax and semantics, hw6 |
| 7 | **Lean Logic Game (LG)** | Solution hw6, quiz 5 (PA1) | Lean LG, hw7; **deadline PA1** |
| 8 | **Church Encodings** | Solution hw7, quiz 6 (LC) | Church encodings, hw8 |
| 9 | **Fixed Point Combinator (Y)** | Solution hw8, quiz 7 (LG) | Fixed Point Combinator, hw9 |
| 10 | **PA2** | Solution hw9, quiz 8 (Church) | Lab on PA2 (lambda calculus), hw10 |
| 11 | **Recursion** | Solution hw10, quiz 9 (Y) | Recursion, hw11 |
| 12 | **Invariants** | Solution hw11, quiz 10 (PA2) | Invariants, hw12; **deadline PA2** |
| 13 | **PA3** | Solution hw12, quiz 11 (Recursion) | Lab PA3 |
| — | Thanksgiving | — | — |
| 14 | **Taking Stock** | Q&A PA3, quiz 12 (Invariants) | Collective puzzle solving, student evals |
| Finals | — | — | **deadline PA3** |

Details (and links to notes as they appear) live in [lecture-by-lecture.md](lecture-by-lecture.md).

## Point scheme

| Component | Points |
|:---|---:|
| Quizzes (12) | 90 |
| Attendance | 23 |
| PA1 | 25 |
| PA2 | 25 |
| PA3 | 37 |
| **Total** | **200** |

## What we will do

This course will be different from any other course you are going to take in computer science. Here are some of the reasons why:

- This course is about the principles underlying all programming languages (and not about a particular programming language). [^lambda]
- You will learn how to make your own programming language.
- We emphasize how to write code that is easy to maintain and provably correct (and not how to write code that is efficient). [^efficiency]
- You will learn how to use recursion instead of iteration. [^recursion]
- We will emphasize functional programming over imperative programming. [^functional]
- We will improve our problem solving skills by showing that some problems are not solvable. [^invariants]
- We will deal with fundamental questions such as: What, in principle, can or cannot be computed? What even is computation? [^computation]
- Instead of concentrating on one level of abstraction (hardware, operating systems, etc) we will emphasize the importance of finding the right levels of abstraction and how to reason simultaneously across different levels of abstraction. [^abstraction]
- We emphasize working with pen & paper as much as with keyboard & screen. [^pen-paper]
- We practice problem solving skills with weekly puzzles. [^puzzles]
- Programming and mathematics are two sides of the same coin. In particular, proofs are programs and programs are proofs. [^Lean]
- Learning the principles of programming languages is a great springboard for lessons about language in general and learning in general. We connect programming language technology with these wider topics. [^philosophy]

[^lambda]: To this end we will study the smallest Turing complete programming language, lambda calculus, and conceptualize all other languages as extensions of lambda calculus. (Footnote: Some languages like C and C++ add enough features to lambda calculus so that they can then disallow higher-order functions.)

[^efficiency]: Of course, efficiency (for example in compiler optimization) is also important in programming languages. But it is, in general, a good strategy to first design for correctness and then understand an efficient program as a refinement of a correct program.

[^recursion]: Formally, recursion and iteration are equivalent. Recursion serves as both a programming technique and a problem solving technique. In fact, iterative programs are often best conceptualized as being derived from a recursive solution. (Footnote: This happens in particular when the recursive solution has the same structure as the problem itself. A famous example is the Towers of Hanoi but every parser, interpreter, and compiler are also examples.)

[^functional]: Most modern languages are "mixed paradigm" and combine features of imperative, object-oriented and functional programming. Since students who take this course are familiar with imperative and object oriented programming, we emphasize functional programming. Another reason to emphasize functional programming is that it relies on principles that are easier to explain and understand. In particular, pure functional programming languages do not have side effects and do not need a memory model to explain their semantics.

[^invariants]: The basic technique to show that a solution does not exist is to find an invariant that all possible solutions must satisfy but the problem does not. But invariants have other uses as well. For example, invariants are at the heart of the design and correctness of algorithms, which we will also touch upon.

[^computation]: We will learn about two mathematical answers to the question of "What is computation?": A function is computable if it can be computed by a Turing machines and a function is computable if it can be implemented in lambda calculus.

[^abstraction]: In our experience, the ability to reason simultaneously across different levels of abstraction is the single most important skill that students of software engineering need to develop.

[^pen-paper]: It is important to use different tools for working on code and for thinking about the problem to be solved.

[^Lean]: This is known as the Curry-Howard correspondence. For a sneak preview see the [Lean Game Server](https://adam.math.hhu.de/).

[^puzzles]: Many of the puzzles we will work on have been created for entertainment. But we will see that the general skills to solve them are the same as the ones that help us, for example, with understanding a tricky algorithm or with debugging code.

[^philosophy]: The most famous example of this is that Chomsky's work on natural language provided the basic theory of [parsing](https://jeffreykegler.github.io/personal/timeline_v3). More generally, much of learning is learning of language and proceeds through the stages of imitation of language, translation between languages, and creation of new languages. (Creation is an example of what Hofstadter calls a strange loop, of recursion without a base case, like a compiler compiling itself.)

## What we will not do

This is a theory course. While we are going to apply theoretical computer science to hands-on coding projects

- we will not present case studies from industry and
- we will not focus on efficiency.

There are other courses that will teach you how to do this and time is limited. Moreover, the methods we will teach are learned best on instructive puzzles and small toy examples. We can promise you that these methods scale to industry sized projects (such as real-world programming languages) but you will have to take our word for it.

## What we require students to do

Learning to implement your own programming language, even a small toy language, requires many stepping stones. We provide the salient ones, but each student learns differently. Therefore, students will have to identify their own individual additional stepping stones. To facilitate this, besides doing the weekly homework, students need to take responsibility for their own learning by asking questions, exploring material and synthesizing knowledge. For example, we encourage everybody to actively participate in class and to make ample use of office hours and of our discussion forum on Discord.

In addition to the theoretical work, there will be programming assignments to give a hands-on experience and applications of the theoretical concepts.

## Organization

The resources for this course are organized as follows:

- Canvas for everything related to grades, deadlines, and submissions.
- Codeberg for everything related to code, lecture notes, and other teaching materials.
- Discord for discussions, troubleshooting, etc.

For details see the Quick Links above.
