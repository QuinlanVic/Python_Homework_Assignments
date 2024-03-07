# Git Terms/Concepts
## SDDA - 7 March 2024
### By: Quinlan Caiger
### Git Merge vs Rebase vs Squash
All three of these merges are techniques that Git offers for integrating changes from one branch to another. Each of these techniques has their own advantages and is suitable for specific situations. 
#### Git Merge
"Merge" intergrates all commits (complete history) of one branch (feature branch) to another, creating a new commit on the target branch called a "merge commit". "Merge" is always a forward moving change record (integrates changes of a branch with another to update the target branch and move forwards with development). "Merge" is the simplest and most commonly used strategy for merging branches but integrating the entire history of one branch into another can cause a lot of clutter and debugging these merge commits when things go wrong can be quite difficult. 

![image](https://github.com/QuinlanVic/Python_Homework_Assignments/assets/109174553/2d323d0f-1ea8-4e44-a7ee-dc7a1c5b7474)

#### Git Rebase
"Rebase" moves a set of commits so that it is situated on top of the base/master branch's latest commit. This results in all of the feature branch's commits (entire history) following the latest commit on the base/master branch, rewriting history. 

![image](https://github.com/QuinlanVic/Python_Homework_Assignments/assets/109174553/a8549868-d102-4758-83fa-6b0ea128a495)

Another example of using Git Rebase

*Before using Git Rebase*

![image](https://github.com/QuinlanVic/Python_Homework_Assignments/assets/109174553/8f8caa15-583a-42cf-a41f-30c7fbdc205f)

*After using Git Rebase*

![image](https://github.com/QuinlanVic/Python_Homework_Assignments/assets/109174553/99b0df56-8191-43e1-9952-cc970330274b)

#### Git Squash
"Squash" joins all of the feature branch's commits from its entire history into one commit with a commit message. Therefore, it does not integrate the feature branch's entire history and removes this excess information which can cause cluttering. This makes it easier to find specific changes when things go wrong.

![commit-squashing-diagram](https://github.com/QuinlanVic/Python_Homework_Assignments/assets/109174553/e8ca2f93-a90e-4284-a5f5-5f070e748663)

### Forks in Github
Forks are copies of Github repositories that allow others to access and modify a copy of the repository's code. 
This means that the main repository is not changed. Others can however, send a pull request to the owner of the main repository 
and with their permission inflict changes to the main repository. 
- Forks are most commonly used to suggest changes to someone else's code or use someone else's code as a starting point/helpful resource for your own project.

### `git rebase -i`
The `git rebase -i` command .  Alternatively, rebase has powerful history rewriting features.

#### References 
1. https://stackoverflow.com/questions/24939843/what-does-it-mean-to-fork-on-github
2. https://medium.com/@shikha.ritu17/git-rebase-vs-merge-vs-squash-choosing-the-right-strategy-for-version-control-a9c9bb97040e#:~:text=%E2%80%94%20Use%20Rebase%20when%20updating%20a,clean%20and%20easier%20to%20manage.&text=%E2%80%94%20Use%20Squash%20when%20merging%20feature,making%20it%20easier%20to%20track.
3. https://www.simplilearn.com/what-is-git-rebase-command-article
4. https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges
5. https://git-scm.com/docs/git-rebase
