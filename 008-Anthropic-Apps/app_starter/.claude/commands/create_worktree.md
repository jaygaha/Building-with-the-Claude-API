Your task is to create a new worktree named '$ARGUMENTS' in the .trees/$ARGUMENTS folder

Follow these steps:

1. Check if an existing folder in the .trees folder with the name $ARGUMENTS already exists. If it does, stop here and tell the user the worktree already exists.
2. Create a new git worktree in the .trees folder with the name $ARGUMENTS.
3. Symlink the .venv folder into the worktree directory
4. Launches a new VSCode editor instance in that directory by runnning the 'code' comman