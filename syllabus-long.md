## General Information
- Class: CPSC-354 Programming Languages, Fall 2026
- Instructors: TBD
- Lectures: TBD
- Office hours: TBD

## Course Description 

**The aim of the course** is to have a look under the hood of programming languages. How do programming languages work? Could you design your own programming language? Instead of looking at particular examples of programming languages, we will build our own. 

A companion course, CPSC 402 Compiler Construction, might be taught in the future, adapting the material of this semester to industrial-scale programming languages such as C++.

**Prerequisites:** MATH 250 (Discrete Mathematics I), CPSC 350 (Data Structures and Algorithms). It is assumed that you know at least one programming language, ideally a few more. It would also be good to have learned something about computer architecture. One theme of the course is how to bridge the gap between a programming language and the actual machine, so some awareness of how machines work is needed to fully appreciate the material. Finally, while the mathematics that we need to engineer our programming languages is introduced in the course, some ability in manipulating formal mathematical models will be needed---as typically acquired in a discrete mathematics or introductory logic course.[^coursecatalogue] 

[^coursecatalogue]: From the [course catalog](https://catalog.chapman.edu/): Prerequisites, MATH 250, CPSC 350. Students develop an understanding of the organization and design of programming languages through writing interpreters for three different toy languages illustrating a range of programming concepts from pure functional languages to imperative languages with memory management. Moreover, the course will open windows into topics of programming languages research such as parsing, operational and denotational semantics, term rewriting, Hoare logic, verification, and theorem proving. Letter grade with Pass/No Pass option. 

## Course Learning Outcomes

See also the [Fowler School of Engineering Program Learning Outcomes](https://docs.google.com/document/d/1OESCtPUolnWFV_qRFuRzNrzxmUtYr5H-dFaYVmPUKY0/edit?usp=sharing) (requires Chapman login).

After completing this course, students will be able to

- use an interactive theorem prover (Lean) to program proofs in discrete mathematics
- explain how interpreters for functional and imperative programming languages work
- use a context-free grammar and a parser generator 
- explain syntax and semantics of various calculi and programming languages
- understand lambda-calculus as a foundation of programming languages and the concepts of operational and denotational semantics
- explain various features of programming languages based on the computational model of term-rewriting
- understand the significance of abstract and algebraic data types
- depending on the available time various theoretical topics will be introduced (program verification, term-rewriting systems, use of well-founded orders in termination proofs, use of invariants in partial correctness proofs)

Moreover, students will be able to acquire the basic ideas of advanced topics such as theorem proving, dependent types and mathematics as a specification and programming language.

Finally, students will learn to appreciate that mathematics is not only important for developers who create the tools used in everyday engineering practice, but also that the knowledge of the mathematical concepts and results underpinning these engineering tools impact everyday engineering practice (and increase your chances to pass a coding interview).

## Program Learning Outcomes

1. Graduates will have mastered the foundational principles of computer science and software engineering, including quantitative reasoning and information literacy related to technology development.

2. Graduates will be able to utilize algorithm, system, and software design and implementation practices in traditional and emerging technology settings.

3. Graduates will be able to present technical information specific to the domain of computer science and software engineering in both oral and written formats.


## Overview 

The course will have a practical and a theoretical component.

- *The theoretical component* will teach some of the mathematics underpinning the design of programming languages such as logic, rewriting, ordered structures, universal algebra, category theory, and type theory. We will cover just enough theory to help the writing of interpreters, and to gain an outlook on some of the questions guiding programming languages research.  

- *The practical component* will be about building interpreters for small programming languages. We will start with a calculator, that is, an interpreter for the language of high-school arithmetic, then go on to the smallest proper programming language known as lambda calculus. Lambda calculus provides variables and functions. Other programming languages can be seen as extensions thereof. Once we have an interpreter for lambda calculus, we will extend it to larger functional and/or imperative programming languages.

## Required Text

The technical content of the course will be distributed via a git repository. Hofstadter's book *Gödel, Escher, Bach* is assigned as supplementary reading to provide general background. Students are expected to read the book to deepen their understanding of the course themes.

## Course Materials 

All course materials will be made available via a git repository.

## Assessment

Assessment will be divided into a total of 200 points.

| Component | Points |
|:---|---:|
| Quizzes | 90 |
| Attendance | 23 |
| Programming Assignment 1 | 25 |
| Programming Assignment 2 | 25 |
| Programming Assignment 3 | 37 |
| **Total** | **200** |

Weekly homework prepares for the quizzes and programming assignments; see [lecture-by-lecture.md](lecture-by-lecture.md) and [report.md](report.md).

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

## Course Assessment 
At some point during the semester, you will be asked to complete a course assessment. This assessment is very important in evaluating how effective the course is meeting its learning outcomes. The assessment will not harm your grade and may be included as a small portion of your attendance grade. 

## Chapman University’s Academic Integrity Policy

Chapman University is a community of scholars that emphasizes the mutual responsibility of all members to seek knowledge honestly and in good faith. Students are responsible for doing their own work and academic dishonesty of any kind will be subject to sanction by the instructor/administrator and referral to the university Academic Integrity Committee, which may impose additional sanctions including expulsion. Please review the full description of Chapman University's policy on [Academic Integrity](https://www.chapman.edu/academics/academic-integrity/index.aspx).
 
 
## Chapman University’s Students with Disabilities Policy

Students who seek an accommodation of a disability or medication condition to participate in the class must contact the [Office of Disability Services](https://www.chapman.edu/students/health-and-safety/disability-services/index.aspx) and follow the proper notification procedure for informing your professor(s) of any granted accommodations. This notification process must occur more than a week before any accommodation can be utilized. Please contact Disability Services at (714) 516-4520 or [DS@chapman.edu](mailto:DS@chapman.edu) if you have questions regarding this process, or for information and to make an appointment to discuss and/or request potential accommodations based on documentation of your disability. The granting of any accommodation will not be retroactive. https://www.chapman.edu/students/health-and-safety/disability-services/policy.aspx

## Chapman University’s Anti-Discrimination Policy

Chapman University is committed to ensuring equality and valuing diversity, including of backgrounds, experiences and viewpoints. Students and professors are reminded to show respect at all times as outlined in Chapman’s Harassment and Discrimination Policy. Please review the full description of the [Harassment and Discrimination ](https://www.chapman.edu/faculty-staff/human-resources/_files/policies/policy-prohibiting-discrimination-and-harassment.pdf)Policy. Any violations of this policy should be discussed with the professor, the Dean of Students and/or otherwise reported in accordance with this policy."
 
## Student Support at Chapman University

Over the course of the semester, you may experience a range of challenges that interfere with your learning, such as problems with friend, family, and or significant other relationships; substance use; concerns about personal adequacy; feeling overwhelmed; or feeling sad or anxious without knowing why.  These mental health concerns or stressful events may diminish your academic performance and/or reduce your ability to participate in daily activities.  You can learn more about the resources available through Chapman University’s [Student Psychological Counseling Services](https://www.chapman.edu/students/health-and-safety/psychological-counseling/). 

Fostering a community of care that supports the success of students is essential to the values of Chapman University.  Occasionally, you may come across a student whose personal behavior concerns or worries you, either for the student’s well-being or yours.  In these instances, you are encouraged to contact the Chapman University Student Concern Intervention Team who can respond to these concerns and offer assistance. While it is preferred that you include your contact information so this team can follow up with you, you can submit a report anonymously.  24-hour emergency help is also available through Public Safety at 714-997-6763. 
 
## Religious Accommodation

Religious Accommodation at Chapman University Consistent with our commitment of creating an academic community that is respectful of and welcoming to persons of differing backgrounds, we believe that every reasonable effort should be made to allow members of the university community to fulfill their obligations to the university without jeopardizing the fulfillment of their sincerely held religious obligations. Please review the syllabus early in the semester and consult with your faculty member promptly regarding any possible conflicts with major religious holidays, being as specific as possible regarding when those holidays are scheduled in advance and where those holidays constitute the fulfillment of your sincerely held religious beliefs.


## Statement on Diversity and Inclusion 
At Chapman University, we strive to make meaningful and lasting connections – with one another and with our broader community and world. We aim to cultivate a welcoming environment, helping every person feel valued and empowered to engage and contribute. Our community members are part of the Chapman Family, where relationships matter – and so do ideas. We strive for a vibrant intellectual community where different perspectives are sought and encouraged freely – to enable new thinking to emerge and interdisciplinary dots to be connected. Through these connections, we advance as individuals, as a campus, and as a society.
