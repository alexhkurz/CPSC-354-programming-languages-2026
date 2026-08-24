# On the Use of Git

![](https://imgs.xkcd.com/comics/git.png)

https://xkcd.com/1597/

[Git](https://en.wikipedia.org/wiki/Git) is a version control software created by Linus Torvalds (also responsible for giving us Linux). There are different commercial implementations of git. Even though, as some say, the [time has come to give up GitHub](https://sfconservancy.org/blog/2022/jun/30/give-up-github-launch/), the following notes still refer to [Github](https://github.com/). There is also a [lawsuit against Github](https://githubcopilotinvestigation.com/) which is motivated by Github building its success on becoming the repository of open source software development and then, as some claim, abusing the trust that open source developers brought to the platform. We found [Codeberg](https://codeberg.org/) a viable alternative to Github, see also [Resources to Give Up GitHub](https://sfconservancy.org/GiveUpGitHub/).


## New to Git?

Have a look at this [tutorial](https://guides.github.com/activities/hello-world/). Let me know if there are problems or if you have other helpful sources. [^help]

[^help]: From the commandline the basic workflow is (assuming your git repo has a file `myfile`) `git add myfile; git commit -m "describe changes" ; git push`

Watch the video of the MIT Missing Lecture Series on [Version Control (Git)](https://missing.csail.mit.edu/2020/version-control/). (Btw, all of the series is highly recommended.) Specifically, [6m55s](https://www.youtube.com/watch?v=2sjqTHE0zok&t=6m55s) for technical background (tree, blob, snapshot, dag, merge conflict, commit, object, content address store, reference) and [26:40](https://www.youtube.com/watch?v=2sjqTHE0zok&t=26m40s) for an introductory demo (`git init`, `git status`, `git add`, `git commit`, `git log`, `git cat-file -p <hash>`, `git log --all --graph --decorate`, `git checkout`, `git diff`, `git branch`, `git merge`, `git merge --continue`, `git remote`, `git push`, `git clone`, `git branch --set-upstream-to=origin/master`, `git fetch`, `git pull`, `git config`, `git clone --shallow`, `vim ~/.gitconfig`, `git add -p`, `git diff --cached`, `git blame`, `git show`, `git stash`, `git stash pop`, `git bisect`, `.gitignore`, )

If you work with different branches, it is worth using [a command-line prompt that displays the branch you are on](https://gist.github.com/reinvanoyen/05bcfe95ca9cb5041a4eafd29309ff29).

## Git best practices

I collect here some lessons learned from using git for assignments in various courses. 

Proper use of git will be considered for grading. Depending on the nature of the assignment, complete solutions uploaded to the repo just before the deadline and not containing a trail of your work **may not be accepted for grading**.

- Use the repo to create a trail of your work. Commit and push often.  
- Be careful about what you commit:  
   - Do not track/commit/push machine generated files. 
   - Avoid unthinking use of `git add *`. Only add files that should be tracked. 
   - Run `git status`. If you see under `Untracked files` names that you don't recognize, they are likely machine generated files. Do not track those. Rather add these names to a file named `.gitignore` at the root of your repo.
   - Build up your `.gitignore` incrementally using `git status` and add files you do not want to track to `.gitignore` step by step. You can start from my .gitignore file in this repo.
   - Meaningful commit messages will help yourself and collaborators.
- Do not create different versions of files by copying them. [Use branches](http://shafiul.github.io/gitbook/3_basic_branching_and_merging.html) for collaborative projects in which you and your collaborators want to work simultaneously but independently on the same project. Branches can be merged later.
- Delete files only in exceptional circumstances. (Btw, even deleted files will remain accessible via the history.)

## Further reading

- I highly recommend these [Resources](https://missing.csail.mit.edu/2020/version-control/#resources). 
- [The Git Community Book](http://shafiul.github.io/gitbook/index.html)
- [Commit Often, Perfect Later, Publish Once: Git Best Practices](https://sethrobertson.github.io/GitBestPractices/)
- [Examples of gitignore files](https://github.com/github/gitignore)
-  Some pages from 
    - [github.com](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
      - [creating](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository)
      - [cloning](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
    - [git-scm.com](https://git-scm.com/):
      - [Getting a Git Repository (clone)](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
      - [Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
      - [Contributing to a Project (fork)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project) (probably not relevant for us)
- Further information:
  - [How do I update a GitHub forked repository?](https://stackoverflow.com/questions/7244321/how-do-i-update-a-github-forked-repository)

## Some commands

- To delete all local files not under version control (can be dangerous):
  ```
  git clean -fdx
  ```
- If a pull is in conflict with local files and you want to ignore the changes in the local files but still keep a copy:
  ```
  git stash
  ```
- [To throw away all uncommitted local changes:](http://shafiul.github.io/gitbook/4_undoing_in_git_-_reset,_checkout_and_revert.html)
  ``` 
  git fetch origin
  git reset --hard origin
  ```
- [`git rebase`](https://shafiul.github.io/gitbook/4_rebasing.html)  