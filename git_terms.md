# Git Terms/Concepts
## SDDA - 7 March 2024
### By: Quinlan Caiger
### Git Merge vs Squash vs Rebase 
All three of these merges are techniques that Git offers for integrating changes from one branch to another. Each of these techniques has their own advantages and is suitable for specific situations. 
#### Git Merge
"Merge" intergrates all commits (complete history) of one branch to another, creating a new commit on the target branch called a "merge commit". "Merge" is the simplest and most commonly used strategy for merging branches but integrating the entire history of one branch into another can cause a lot of clutter and debugging these merge commits when things go wrong can be quite difficult. 
#### Git Squash


### Forks in Github
Forks are copies of Github repositories that allow others to access and modify a copy of the repository's code. 
This means that the main repository is not changed. Others can however, send a pull request to the owner of the main repository 
and with their permission inflict changes to the main repository. 
- Forks are most commonly used to suggest changes to someone else's code or use someone else's code as a starting point/helpful resource for your own project.

### `git rebase -i`
The `git rebase -i` command . Merge is always a forward moving change record. Alternatively, rebase has powerful history rewriting features.

#### References 
1. https://stackoverflow.com/questions/24939843/what-does-it-mean-to-fork-on-github
2. https://medium.com/@shikha.ritu17/git-rebase-vs-merge-vs-squash-choosing-the-right-strategy-for-version-control-a9c9bb97040e#:~:text=%E2%80%94%20Use%20Rebase%20when%20updating%20a,clean%20and%20easier%20to%20manage.&text=%E2%80%94%20Use%20Squash%20when%20merging%20feature,making%20it%20easier%20to%20track.
3. https://www.simplilearn.com/what-is-git-rebase-command-article
