#!/usr/bin/env python 
import sys
from rich.console import Console
from rich.markdown import Markdown
import readchar

def read_markdown(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    slides = content.split('\n---\n')
    return slides

def render_slide(slide_content, console):
    console.clear()
    markdown = Markdown(slide_content)
    console.print(markdown)

def navigate_slides(slides):
    console = Console()
    current = 0
    total = len(slides)
    
    while True:
        render_slide(slides[current], console)
        console.print("\n")
        console.print(f"[bold yellow]Slide {current + 1}/{total}[/bold yellow]")
        # console.print("Press 'n' for next, 'p' for previous, 'q' to quit.", end="\n\n")
        
        key = readchar.readkey()
        if key.lower() == 'n':
            if current < total - 1:
                current += 1
        elif key.lower() == 'p':
            if current > 0:
                current -= 1
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