# Report

The report will be written in $\LaTeX$ (https://www.latex-project.org/). A template for your $\LaTeX$ source file is [`report.tex`](report/report.tex); see also the guidelines in [`report-guidelines.tex`](report/report-guidelines.tex) and examples in [`latex-example.tex`](report/latex-example.tex).

Weekly homework is documented in the report. Graded assessment is via quizzes and programming assignments (see the [syllabus](syllabus-long.md)); the report is the place where you organise solutions, explorations, and notes for yourself and for feedback.

## Teaching Rationale

"*Learning is the process of creating knowledge.*" (Kolb & Kolb)

"*Creativity is just connecting things. When you ask creative people how they did something, they feel a little guilty, because they didn’t really do it, they just saw something. It seemed obvious to them after a while. That’s because they were able to connect experiences they’ve had and synthesize new things.*" (Pentland)

The purpose of the report is to help students grow from learners of a specified curriculum to independent explorers of a subject area. Accordingly, the report should contain solutions to homework (skill drill) and may also document your own explorations around the theme of the course.

## Installing Latex

Our own $\LaTeX$ setup is as follows (all available for Linux, macOS, and Windows):
- [texlive](https://www.tug.org/texlive/) as the $\LaTeX$ distribution
- [VS Code](https://code.visualstudio.com/) / [Cursor](https://cursor.com/) as IDE
- [LaTeX-Workshop](https://github.com/James-Yu/LaTeX-Workshop/blob/master/README.md) as VS Code extension, see [Installation guide](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install)
- macOS-specific guide for MacTeX and LaTeX workshop: https://sudorealm.com/blog/how-to-write-latex-documents-with-visual-studio-code-on-mac

For technical troubleshooting, please see the respective Discord channel and/or the office hours.

If you have problems integrating Latex and Github into your editor, you can run Latex and push to Github via the commandline using `pdflatex report.tex` and `git push`, respectively.

Instead of installing $\LaTeX$ you can also work on [Overleaf](https://www.overleaf.com) if you find this easier.

To **test your setup** make sure of the following:

- You have a local folder, say `cpsc354` (name doesn't matter too much but notice that you will use the same repo throughout the course, so dont call it something like `homework1`).
- It has a subfolder `Report` (name matters and capitalization matters).
- You copy [`report.tex`](report/report.tex) to your subfolder `Report`.
- You can compile `report.tex` locally and generate `report.pdf`, either via the green play button in VSCode or by typing `pdflatex report.tex` in a terminal.
- You can change `report.tex` (eg put your name), commit and push to Github. If pushing via the VSCode interface fails, try `git push` on the commandline.
- Check that `report.pdf` changed on Github.

## Organization

- You will keep both `report.tex` and `report.pdf` in a personal private GitHub repository. 
- Unless specified otherwise, in the beginning, your repo should only contain the following files
    ```
    .gitignore
    Report/report.pdf
    Report/report.tex
    README.md
    ```
    The README should contain name and email.
- For example, if a homework requires programming, make a subdirectory `src` where you store the relevant program files; if you want to include images in your report, make a subdirectory `img`; etc.
- Always use the same repository for all submissions of the course (get in touch if you think an exception is appropriate).
- Do not name different versions of your report, instead rely on the version control of git.
- Give the instructor access to your private GitHub repo by inviting your instructor (details announced in class).
- Submission info will be on Canvas.

## Writing of the Report

For organization of the github repo see [Git Best Practices](git-best-practices.md). In particular,
- respect the naming conventions given by the instructor,
- do not put machine-generated files in the repo,
- do not keep different versions of the report.

For organization of the report, layout and typesetting, take your favourite textbooks or scientific articles as examples. In CS, they are more often than not produced with $\LaTeX$. Learning $\LaTeX$ is one of the aims of the course.

The report should be on the content of the class as well as on your own investigations that you pursue on the topic of the class. Do not put research on Latex into the report, Latex is just a tool for typesetting.

## Homework

**Deadlines:** announced weekly on Canvas. Homework is typically due before the day on which solutions are discussed (see [lecture-by-lecture.md](lecture-by-lecture.md)).
