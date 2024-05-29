import tkinter as tk
import customtkinter as ctk
from recipe_manager import RecipeManager
from widgets import SlideFrame, ResizableFrame


def setup_animated_panel(window):
    animated_panel = SlideFrame(window, -0.3, 0.0)
    
    return animated_panel


def setup_sidebar(animated_panel):
    title_frame = ctk.CTkFrame(
        animated_panel, 
        width=animated_panel.width, 
        bg_color="transparent",
        )
    title_frame.pack(fill="x")
    ctk.CTkLabel(
        title_frame, 
        text="Folders",
        ).pack(side="top", anchor="center")

    for name in tabs.keys():
        tab_button = ctk.CTkButton(
            animated_panel, 
            text=name, 
            border_width=0, 
            corner_radius=0, 
            command=lambda name=name: show_tab(name),
            )
        tab_button.pack(anchor="n", fill="x")   

    
current_active_tab = None
def show_tab(tab_name):
    global current_active_tab
    
    if current_active_tab:
        current_place_info = current_active_tab.place_info()
        new_pos = float(current_place_info["relx"])
        current_active_tab.place_forget()
    else:
        new_pos = 0
        for _, tab in tabs.items():
            tab.place_forget()
        
    current_active_tab = tabs[tab_name]
    current_active_tab.set_position(new_pos)
    current_active_tab.place(relx=new_pos, relwidth=1.0 - new_pos, relheight=1.0)


def create_tabs(parent):
    tabs = {
        "All": ResizableFrame(parent, 0, 0.3, fg_color="red"),
        "Favorites": ResizableFrame(parent, 0, 0.3, fg_color="blue"),
        "Trash": ResizableFrame(parent, 0, 0.3, fg_color="yellow")
    }
    # for name, frame in tabs.items():
    #     ctk.CTkLabel(frame, text=f"This is {name} Tab", fg_color=frame.cget("fg_color")).pack(padx=20, pady=20)
    return tabs


def setup_main_window():
    window = ctk.CTk()
    window.title('Animated Widgets')
    window.geometry('600x400')
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    
    return window

max_columns = 3
def calculate_max_columns():
    global max_columns
    widget_width = 200  # Assumed width of each widget
    window_width = window.winfo_width()
    max_columns = max(1, window_width // widget_width)

def on_resize(event):
    calculate_max_columns()
    rearrange_recipes()

def rearrange_recipes():
    for frame in tabs.values():
        for widget in frame.winfo_children():
            widget.grid_forget()
    
    for frame in tabs.values():
        row = col = 0
        for widget in frame.winfo_children():
            widget.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            col += 1
            if col >= max_columns:
                col = 0
                row += 1

def add_recipe_to_active_tab():
    RecipeManager.open_editor(current_active_tab, None, "add")
    rearrange_recipes()


if __name__ == "__main__":
    window = setup_main_window()
    global tabs
    tabs = create_tabs(window)
    show_tab("All")

    animated_panel = setup_animated_panel(window)

    def animate():
        animated_panel.animate()
        current_active_tab.animate()

    setup_sidebar(animated_panel)
    
    button = ctk.CTkButton(
        window,
        text="-", 
        width=25,
        height=25,
        corner_radius=0, 
        command=animate,
        )
    button.place(relx=0.03, rely=0.03, anchor="center")
    
    add_button = ctk.CTkButton(
        window,
        text="+",
        width=25,
        height=25,
        corner_radius=0,
        command=add_recipe_to_active_tab
    )
    add_button.place(relx=0.9, rely=0.9, anchor="center")

    window.bind("<Configure>", on_resize)
    window.mainloop()
