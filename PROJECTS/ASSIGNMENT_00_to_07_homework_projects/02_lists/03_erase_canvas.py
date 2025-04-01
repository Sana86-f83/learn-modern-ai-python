# Problem Statement
# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
# We then create an eraser rectangle which, when dragged around the canvas, 
# sets all of the rectangles it is in contact with to white.


""" This program implements an 'eraser' on a canvas.
The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
We then create an eraser rectangle which, when dragged around the canvas, 
sets all of the rectangles it is in contact with to white.
"""
# ===================Start Program=========================================
import tkinter as tk
import time

# Canvas size and other constants
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.eraser = None  # Eraser rectangle
        self.create_grid()
        
        # Bind mouse movement to erase function
        self.canvas.bind("<Motion>", self.erase_objects)
        self.canvas.bind("<Button-1>", self.create_eraser)  # Create eraser on click

    def create_grid(self):
        """Creates a grid of blue squares."""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

    def create_eraser(self, event):
        """Creates an eraser at the mouse click position."""
        if self.eraser is None:  # Only create eraser once
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink"
            )

    def erase_objects(self, event):
        """Erases objects under the eraser by turning them white."""
        if self.eraser:
            self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            overlapping = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            
            for obj in overlapping:
                if obj != self.eraser:
                    self.canvas.itemconfig(obj, fill="yellow") #change color

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Eraser Canvas App")
    app = EraserApp(root)
    root.mainloop()

# ================Program End==============================================