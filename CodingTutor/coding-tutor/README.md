# Coding Tutor

Personalized AI tutoring that creates tutorials from your actual codebase, tracks progress with spaced repetition, and builds a persistent learning trail.

## Features

- **Personalized Learning**: Onboarding interview creates learner profile for tailored teaching
- **Real Code Examples**: Uses YOUR codebase as teaching material, not abstract examples
- **Spaced Repetition**: Quiz system with Fibonacci intervals for optimal retention
- **Living Documents**: Tutorials evolve with Q&A sections and updates
- **Progress Tracking**: Understanding scores (1-10) track mastery over time

## Usage

### Commands

```
/teach-me [topic]     # Learn a specific concept
/quiz-me [topic]      # Test knowledge retention
/quiz-me              # Open quiz based on spaced repetition priority
```

### First Time Setup

1. Create tutorials directory: `mkdir -p ~/coding-tutor-tutorials`
2. Complete onboarding interview (automatic on first use)
3. Start learning!

### Tutorial Storage

All tutorials are stored in `~/coding-tutor-tutorials/`:
- `learner_profile.md` - Your background and goals
- `*.md` - Individual tutorials with metadata

## How It Works

1. **Learner Profiling**: Interview captures background, goals, and context
2. **Gap Analysis**: Reviews existing knowledge to find optimal next topic
3. **Real Examples**: Finds demonstrations in your actual codebase
4. **Tutorial Creation**: Writes personalized, narrative-driven tutorials
5. **Spaced Review**: Quiz system surfaces topics at optimal intervals

## Tutorial Quality

Tutorials follow the Julia Evans / Dan Abramov style:
- Start with the "why" - the problem being solved
- Use actual code from your projects
- Build mental models with diagrams and analogies
- Predict and address confusion points
- End with a practical challenge

## Attribution

Adapted from [claude-code-essentials](https://github.com/nityeshaga/claude-code-essentials) under MIT license.
