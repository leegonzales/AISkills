# AISkills Commands

Slash commands for Claude Code - reusable prompts triggered by `/command-name`.

## What Are Commands?

Commands are markdown files that expand into prompts when invoked. They provide:
- **Consistency**: Same approach every time
- **Discipline**: Enforce best practices
- **Speed**: Quick access to common workflows

## Usage

In Claude Code, commands are invoked with `/command-name`:

```
/pinpoint Error: undefined is not a function
/review Check the authentication flow changes
```

## Available Commands

| Command | Purpose |
|---------|---------|
| `/pinpoint` | Root-cause analysis before fixing |
| `/review` | Structured code review with severity ratings |

## Command Structure

Each command is a markdown file with:
- Clear instructions for Claude
- `$ARGUMENTS` placeholder for user input
- Specific constraints and expectations

## Creating New Commands

1. Create `command-name.md` in this directory
2. Write clear, specific instructions
3. Use `$ARGUMENTS` where user input should go
4. Test the command in various scenarios

## Best Practices

- **Be specific**: Vague commands produce vague results
- **Set constraints**: Tell Claude what NOT to do
- **Request confirmation**: Require approval before destructive actions
- **Think first**: Ask for analysis before solutions

## Attribution

Commands adapted from [claude-code-essentials](https://github.com/nityeshaga/claude-code-essentials) under MIT license.
