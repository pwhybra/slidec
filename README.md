# slidec

A simple python script to present markdown in your terminal as slides.

Useful if you are wanting to do demos from the command line and refer to notes.

Works well with e.g. tmux and having split planes, one for live demo, one for the 
slides/notes.


<img src="assets/demo.gif">

## Format

Slides are written in a single markdown file separated by `---`.

E.g.

```markdown
# Example slide 1

-  Content 

--- 

# Example slide 2

- More content

```

## Run 
```terminal
python slidec.py example_slides.md
```

## Setup dependencies

In your chosen python environment, install the requirements
```terminal
pip install requirements/requirements.txt
```

## Navigation
Once in presentation mode

- Next slide: `n` or `j`
- Previous slide: `p` or `k`
- Select slide: `g` navigate with fuzzy search 
- quit: `q`

## Inspiration

There are other much more robust tools for this task

e.g. lookatme, slides

However, I found I could get all the functionality I wanted in a single small python
script with very little overhead.