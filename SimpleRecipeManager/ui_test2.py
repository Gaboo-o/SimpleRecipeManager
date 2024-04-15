import tkinter as tk
from turtle import width
import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos, **kwargs):
        super().__init__(master=parent, **kwargs)
        self.start_pos = min(start_pos, end_pos)
        self.end_pos = max(start_pos, end_pos)
        self.width = abs(start_pos - end_pos)
        self.pos = start_pos
        self.increasing = start_pos < end_pos
        self.place(relx=start_pos, relwidth=self.width, relheight=1)

    def animate(self):
        if self.increasing:
            self.animate_right()
        else:
            self.animate_left()

    def animate_right(self):
        if self.pos < self.end_pos:
            self.pos += 0.008
            self.place(relx=self.pos, relwidth=self.width, relheight=1)
            self.after(10, self.animate_right)
        else:
            self.increasing = False

    def animate_left(self):
        if self.pos > self.start_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, relwidth=self.width, relheight=1)
            self.after(10, self.animate_left)
        else:
            self.increasing = True


def show_tab(tab_frame):
    for tab in tabs:
        tab.pack_forget()
    tab_frame.pack(fill='both', expand=True)

window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

new_tab1 = ctk.CTkScrollableFrame(window, bg_color="red")
ctk.CTkLabel(new_tab1, text="This is Tab 1", bg_color="red").pack(padx=20, pady=20)
new_tab2 = ctk.CTkScrollableFrame(window, bg_color="blue")
ctk.CTkLabel(new_tab2, text="This is Tab 2", bg_color="blue").pack(padx=20, pady=20)
new_tab3 = ctk.CTkScrollableFrame(window, bg_color="yellow")
ctk.CTkLabel(new_tab3, text="This is Tab 3", bg_color="yellow").pack(padx=20, pady=20)

tabs = [new_tab1, new_tab2, new_tab3]

show_tab(new_tab1)

animated_button = SlidePanel(window, 0.0, 0.3, fg_color="transparent")
animated_panel = SlidePanel(window, -0.3, 0.0)

def animate():
    animated_panel.animate()
    animated_button.animate()

button = ctk.CTkButton(animated_button, text='>', fg_color="transparent", command=animate)
button.place(relx=animated_panel.pos+animated_panel.width, rely=0.15, relwidth=animated_panel.width, relheight=0.1)

title_frame = ctk.CTkFrame(animated_panel, width=animated_panel.width, bg_color="transparent")
title_frame.pack(fill="x")
ctk.CTkLabel(title_frame, text="Folders").pack(side="left", anchor="center")

ctk.CTkButton(animated_panel, text="All", corner_radius=0, command=lambda: show_tab(new_tab1)).pack(anchor="n", fill="x")
ctk.CTkButton(animated_panel, text="Favorites", corner_radius=0, command=lambda: show_tab(new_tab2)).pack(anchor="n", fill="x")
ctk.CTkButton(animated_panel, text="Trash", corner_radius=0, command=lambda: show_tab(new_tab3)).pack(anchor="n", fill="x")

button = ctk.CTkButton(window, text="+", corner_radius=0, command=animated_panel.animate)
button.place(relx=0.5, rely=0.9, anchor="center")

window.mainloop()
