## General Information
- Class: CPSC-354 Programming Languages, Fall 2026
- Instructors: 
  - Jonathan Weinberger
    - Mon, Wed 230-345 (S2), Hashinger 303
    - Mon, Wed 400-515 (S1), Hashinger 150
  - Alexander Kurz
    - Tue, Thu, 1130-1245 (S3), Keck 156
- Office hours: 
  - AK: Tue, Thu, 230-330, Keck N205
  - JW: Wed 8-930, Thu 10-1130, locations TBD

## Course Description 

**The aim of the course** is to have a look under the hood of programming languages. How do programming languages work? Could you design your own programming language? Instead of looking at particular examples of programming languages, we will build our own. 

A companion course, CPSC 402 Compiler Construction, might be taught in the future, adapting the material of this semester to industrial-scale programming languages such as C++.

**Prerequisites:** MATH 250 (Discrete Mathematics I), CPSC 350 (Data Structures and Algorithms). It is assumed that you know at least one programming language, ideally a few more. It would also be good to have learned something about computer architecture. One theme of the course is how to bridge the gap between a programming language and the actual machine, so some awareness of how machines work is needed to fully appreciate the material. Finally, while the mathematics that we need to engineer our programming languages is introduced in the course, some ability in manipulating formal mathematical models will be needed---as typically acquired in a discrete mathematics or introductory logic course.[^coursecatalogue] 

[^coursecatalogue]: From the [course catalog](https://catalog.chapman.edu/): Prerequisites, MATH 250, CPSC 350. Students develop an understanding of the organization and design of programming languages through writing interpreters for three different toy languages illustrating a range of programming concepts from pure functional languages to imperative languages with memory management. Moreover, the course will open windows into topics of programming languages research such as parsing, operational and denotational semantics, term rewriting, Hoare logic, verification, and theorem proving. Letter grade with Pass/No Pass option. 

## Course Learning Outcomes

See also the [Fowler School of Engineering Program Learning Outcomes](https://docs.google.com/document/d/1OESCtPUolnWFV_qRFuRzNrzxmUtYr5H-dFaYVmPUKY0/edit?usp=sharing) (requires Chapman login).

After completing this course, students will be able to

- use Lean (Natural Number Game and Logic Game) to write and check mathematical proofs, and relate proofs to programs (Curry–Howard)
- reason about computation with string and term rewriting, including termination and normal forms
- write and analyse context-free grammars and relate concrete and abstract syntax trees; implement a small calculator with a parser
- explain the syntax and operational semantics of the untyped lambda calculus, including substitution, reduction, Church encodings, and the fixed-point combinator
- implement and debug an interpreter for lambda calculus (and extend it toward a small functional language)
- use recursion as a problem-solving and programming technique (including recursion over syntax trees)
- use invariants to argue that a problem has no solution, or that an algorithm or protocol is correct
- connect elementary ideas of logic and type theory (natural deduction, intuitionistic logic, type inference) to programming language practice

Finally, students will appreciate that the mathematical ideas behind programming languages matter for everyday software engineering—not only for building compilers and proof assistants, but for clearer reasoning about correctness, abstraction, and design.

## Program Learning Outcomes

1. Graduates will have mastered the foundational principles of computer science and software engineering, including quantitative reasoning and information literacy related to technology development.

2. Graduates will be able to utilize algorithm, system, and software design and implementation practices in traditional and emerging technology settings.

3. Graduates will be able to present technical information specific to the domain of computer science and software engineering in both oral and written formats.


## Overview 

The course will have a practical and a theoretical component.

- *The theoretical component* will teach some of the mathematics underpinning the design of programming languages such as logic, rewriting, ordered structures, universal algebra, category theory, and type theory. We will cover just enough theory to help the writing of interpreters, and to gain an outlook on some of the questions guiding programming languages research.  

- *The practical component* will be about building interpreters for small programming languages. We will start with a calculator, that is, an interpreter for the language of high-school arithmetic, then go on to the smallest proper programming language known as lambda calculus. Lambda calculus provides variables and functions. Other programming languages can be seen as extensions thereof. Once we have an interpreter for lambda calculus, we will extend it to larger functional and/or imperative programming languages.

## Required Text

The technical content of the course will be distributed via this git repository. 

No required text.

Hofstadter's book *Gödel, Escher, Bach* is a popular science book that we recommend for general background reaing.

## Course Materials 

All course materials will be made available via a git repository.

## Assessment

Assessment will be divided into a total of 200 points. The homework are assigned to you for self-study only, and to prepare for the upcoming quiz. There will be a review session of the respective homework before every quiz. The quiz is taken in-class and on pen and paper. There are 12 quizzes, out of which the 9 best ones count toward your grade (so the 3 lowest ones will be dropped).

Each attended lecture counts for 1P of attendance. We won't take attendance in the first lecture. There are 23 attendance points in total, so 4 lectures can be missed without effect to the grade. Given the highly connected syllabus we do strongly recommend you to attend every lecture.

| Component | Points |
|:---|---:|
| Quizzes | 90 |
| Attendance | 23 |
| Programming Assignment 1 | 25 |
| Programming Assignment 2 | 25 |
| Programming Assignment 3 | 37 |
| **Total** | **200** |

Weekly homework prepares for the quizzes and programming assignments; see [lecture-by-lecture.md](lecture-by-lecture.md).

## Course Grade Breakdown

Grading scale used for the course:

| Percentage | Letter |
|---|---|
| 90 | A |
| 80-89 | B |
| 70-79	| C |
| 60-69	| D |
| < 60 |	F |

You must score a 70 or above to receive a P when taking the course P/NP.

## Late Policy

If you need more time for an assignment 
- convince the instructor that you already have done substantial work (for example by showing me the code in your GitHub repository);
- explain the special circumstances that would allow the instructor to justify giving you more time.

(The two items above need to be acted upon before the deadline.)

## Attendance

It is expected that students attend every lecture. Let us know if you have a religious or medical issue. See [attendance.md](attendance.md).

## Policies required to be listed via University guidelines

#### Chapman University’s Academic Integrity Policy

Chapman University is a community of scholars that emphasizes the mutual responsibility of all members to seek knowledge honestly and in good faith.  Students are responsible for doing their own work and academic dishonesty of any kind will be subject to sanction by the instructor/administrator and referral to the university Academic Integrity Committee, which may impose additional sanctions including expulsion.  Please see the full description of Chapman University's policy on Academic Integrity.

#### Chapman University’s Students with Disabilities Policy

In compliance with ADA guidelines, students who have any condition, either permanent or temporary, that might affect their ability to perform in this class are encouraged to contact the Office of Disability Services.  If you will need to utilize your approved accommodations in this class, please follow the proper notification procedure for informing your professor(s).  This notification process must occur more than a week before any accommodation can be utilized.  Please contact Disability Services at (714) 516–4520 if you have questions regarding this procedure or for information or to make an appointment to discuss and/or request potential accommodations based on documentation of your disability.  Once formal approval of your need for an accommodation has been granted, you are encouraged to talk with your professor(s) about your accommodation options.  The granting of any accommodation will not be retroactive and cannot jeopardize the academic standards or integrity of the course.

#### Chapman University’s Equity and Diversity Policy

Chapman University is committed to ensuring equality and valuing diversity.  Students and professors are reminded to show respect at all times as outlined in Chapman’s Harassment and Discrimination Policy.  Please review the full description of Harassment and Discrimination Policy. Any violations of this policy should be discussed with the professor, the Dean of Students and/or otherwise reported in accordance with this policy.”

#### Student Support at Chapman University

Over the course of the semester, you may experience a range of challenges that interfere with your learning, such as problems with friend, family, and or significant other relationships; substance use; concerns about personal adequacy; feeling overwhelmed; or feeling sad or anxious without knowing why.  These mental health concerns or stressful events may diminish your academic performance and/or reduce your ability to participate in daily activities.  You can learn more about the resources available through Chapman University’s Student Psychological Counseling Services.

Fostering a community of care that supports the success of students is essential to the values of Chapman University.  Occasionally, you may come across a student whose personal behavior concerns or worries you, either for the student’s well-being or yours.  In these instances, you are encouraged to contact the Chapman University Student Concern Intervention Team who can respond to these concerns and offer assistance. While it is preferred that you include your contact information so this team can follow up with you, you can submit a report anonymously.  24-hour emergency help is also available through Public Safety at 714-997-6763.

#### Religious Accommodation

Religious Accommodation at Chapman University Consistent with our commitment of creating an academic community that is respectful of and welcoming to persons of differing backgrounds, we believe that every reasonable effort should be made to allow members of the university community to fulfill their obligations to the university without jeopardizing the fulfillment of their sincerely held religious obligations. Please review the syllabus early in the semester and consult with your faculty member promptly regarding any possible conflicts with major religious holidays, being as specific as possible regarding when those holidays are scheduled in advance and where those holidays constitute the fulfillment of your sincerely held religious beliefs.

#### Changes
This syllabus is subject to change. Updates will be posted on the course website.
