Your task is to merge in the $ARGUMENTS worktree in the .tree/$ARGUMENTS folder.

Follow these steps:

1. Change into the .trees/$ARGUMENTS directory
2. Examine the changes that were made in the lastest commit
3. Change back to the root dir
4. Merge in the worktree
5. There might be merge conflicts. Use "git status", "git diff --name-only --diff-filter=U" or "git ls-files -u" to list files that have merge conflicts.
6. Manually resolve conflicts based upon your knowledge of the changes. 