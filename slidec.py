#!/usr/bin/env python 
import sys
from rich.console import Console
from rich.markdown import Markdown
import readchar
import subprocess


def read_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    slides = content.split('\n---\n')
    return slides


def render_slide(slide_content, console):
    console.clear()
    markdown = Markdown(slide_content)
    console.print(markdown)


def create_slide_list_for_fzf(slides):
    """Create a one-liner representation for each slide.
    Example Format:
    (slide 1): # My Title Here ...
    """
    slide_lines = []
    for i, slide in enumerate(slides, start=1):
        # Replace newlines with spaces
        single_line = " ".join(slide.splitlines())
        line = f"(slide {i}): {single_line}"
        slide_lines.append(line)
    return slide_lines


def go_to_slide(slides, current):
    """Launch fzf with a list of slides and return the selected slide index."""
    slide_lines = create_slide_list_for_fzf(slides)
    # Join all slides into a single string input for fzf
    fzf_input = "\n".join(slide_lines) + "\n"
    
    # Run fzf
    try:
        result = subprocess.run(
            ["fzf", "--prompt=Slide>", "--reverse", "--height=30%"],
            input=fzf_input,
            text=True,
            capture_output=True
        )
    except FileNotFoundError:
        Console.print("[red]Error:[/red] fzf not found. Install fzf to use this.")
        return current

    if result.returncode != 0 or not result.stdout.strip():
        return current

    selected_line = result.stdout.strip()
    prefix = "(slide "
    if selected_line.startswith(prefix):
        remainder = selected_line[len(prefix):]
        parts = remainder.split('):', 1)
        slide_number_str = parts[0].strip()
        try:
            slide_number = int(slide_number_str)
            return slide_number - 1
        except ValueError:
            return current
    else:
        return current


def navigate_slides(slides):
    console = Console()
    current = 0
    total = len(slides)
    
    while True:
        render_slide(slides[current], console)
        console.print("\n")
        console.print(f"[bold yellow]{current + 1}/{total}[/bold yellow]")
        # console.print("Press 'n' for next, 'p' for previous, 'q' to quit.")
        
        key = readchar.readkey()
        if key.lower() in ['n', 'j']:
            if current < total - 1:
                current += 1
        elif key.lower() in ['p', 'k']:
            if current > 0:
                current -= 1
        elif key.lower() == 'g':
            # Go to a selected slide via fzf
            current = go_to_slide(slides, current)
        elif key.lower() == 'q':
            console.print("Exiting presentation.", style="bold red")
            break


def main():
    if len(sys.argv) != 2:
        print("Usage: python slide_presenter.py path/to/slides.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    slides = read_markdown(file_path)
    navigate_slides(slides)


if __name__ == "__main__":
    main()