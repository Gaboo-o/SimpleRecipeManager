import tkinter as tk
import customtkinter as ctk

class SlideFrame(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos, rel_speed=0.02, **kwargs):
        super().__init__(master=parent, **kwargs)
        
        self.start_pos = min(start_pos, end_pos)  # Determine the minimum position
        self.end_pos = max(start_pos, end_pos)  # Determine the maximum position
        self.width = abs(start_pos - end_pos)  # Calculate the width of the panel
        self.pos = start_pos  # Set the initial position
        self.increasing = start_pos < end_pos  # Determine the direction of movement
        self.rel_speed = rel_speed  # Set the rel_speed of the animation
        self.place(relx=start_pos, relwidth=self.width, relheight=1)  # Place the panel in the initial position

    def animate(self):
        if self.increasing:
            self._animate_right()  # Animate to the right if the position is increasing
        else:
            self._animate_left()  # Animate to the left if the position is decreasing

    def _animate_right(self):
        if self.pos < self.end_pos:
            self.pos += self.rel_speed  # Increment the position
            self.place(relx=self.pos, relwidth=self.width, relheight=1)  # Update the panel position
            self.after(15, self._animate_right)  # Continue the animation after 5 ms
        else:
            self.increasing = False  # Reverse direction when the end position is reached

    def _animate_left(self):
        if self.pos > self.start_pos:
            self.pos -= self.rel_speed  # Decrement the position
            self.place(relx=self.pos, relwidth=self.width, relheight=1)  # Update the panel position
            self.after(15, self._animate_left)  # Continue the animation after 5 ms
        else:
            self.increasing = True


class ResizableFrame(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos, rel_speed=0.02, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.pos = start_pos
        self.increasing = start_pos < end_pos
        self.rel_speed = rel_speed
        self.place(relx=start_pos, relwidth=1.0, relheight=1.0)
        
    def set_position(self, pos):
        self.pos = pos
        self._update_place()
        self.increasing = self.pos < self.end_pos

    def animate(self):
        if self.increasing:
            self._animate_expand()
        else:
            self._animate_shrink()

    def _animate_expand(self):
        if self.pos < self.end_pos:
            self.pos += self.rel_speed
            self._update_place()
            self.after(15, self._animate_expand)
        else:
            self.increasing = False

    def _animate_shrink(self):
        if self.pos > self.start_pos:
            self.pos -= self.rel_speed
            self._update_place()
            self.after(15, self._animate_shrink)
        else:
            self.increasing = True
                    
    def _update_place(self):
        self.place(relx=self.pos, relwidth=1.0 - self.pos, relheight=1.0)
        self.update_idletasks()  # Force update of the frame and its children
        for child in self.winfo_children():
            child.update_idletasks()