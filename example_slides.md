# Slidec example: Introduction to **Git**

Use **Slidec** to navigate and present these slides directly from your terminal.

> **Navigation**

- Next slide: `n` or `j`
- Previous slide: `p` or `k`
- Select slide: `g` navigate with fuzzy search 
- quit: `q`

---
# Contents

1. What is Git?
2. Setting Up a Repository
3. Staging & Committing Changes
4. Branching & Merging

---
# What is Git?

**Git** is a distributed version control system that helps you track changes in your project files over time.  
It allows multiple collaborators to work on a project simultaneously without overwriting each other’s work, ensuring a complete history of changes and easy rollback if needed.

---
# Setting Up a Repository

To start using Git on a project:

1. Configure your username and email if you haven't already.
2. Initialize a new repository.
3. Check the status of your repository.


#### Example:

```bash
# Set your username and email (only required once per machine)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Initialize a Git repository
git init

# Check repository status
git status
```

---
# Staging & Committing Changes

After making changes, you need to stage them before committing.

```bash
# Add all changed files to the staging area
git add .

# Commit the changes with a descriptive message
git commit -m "Implement feature X"
```

**Tip:** Commits should be small and focused, with meaningful messages that explain why the changes were made.

---
# Branching & Merging

**Branches** allow you to work on different features or bug fixes independently.

```bash
# list branches
git branch

# Create a new branch called feature-branch and switch to it
git switch -c feature-branch
```

After completing your work, merge it back into the main branch:

```bash
# Switch back to main branch
git switch main

# Merge changes from 'feature-branch' into 'main'
git merge feature-branch
```
