# Anthropic apps

Two powerful applications built by Anthropic

1. Claude Code
2. Computer Use

## Claude Code in action

Claude Code isn't just a tool for writing code - it's designed to work alongside you throughout every phase of a software project. Think of it as another engineer on your team who can handle everything from initial setup to deployment and support.

> Take on example `008-Anthropic-Apps/app_starter`

### The /init Command

When you start working with Claude Code on a project, the first thing you'll want to do is run the `/init` command. This tells Claude to scan your entire codebase and understand your project's structure, dependencies, coding style, and architecture.

Claude summarizes everything it learns in a special file called `CLAUDE.md`. This file automatically gets included as context in all future conversations, so Claude remembers important details about your project.

You can have multiple `CLAUDE.md` files for different scopes:

- **Project** - Shared between all engineers working on the project
- **Local** - Your personal notes that aren't checked into git
- **User** - Used across all your projects

When running `/init`, you can add special directions for areas you want Claude to focus on. The generated file will include build commands, coding guidelines, and project-specific patterns that Claude should follow.

You can also quickly add notes to your CLAUDE.md file using the `#` command. For example, typing `# Always use descriptive variable names` will prompt you to add this guideline to your project, local, or user memory.

### The /clear Command

Clear or reset the conversation history