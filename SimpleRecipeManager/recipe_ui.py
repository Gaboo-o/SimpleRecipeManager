import tkinter as tk
import customtkinter as ctk
from recipe_manager import RecipeManager


class RecipeUI(ctk.CTkFrame):
    """Displays a recipe"""
    
    def __init__(self, parent=None, recipe=None):
        """Takes a Recipe obj and uses it to set itself up"""

        super().__init__(master=parent, width=200, height=200)
        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.parent = parent
        self.recipe = recipe
        
        self.string_vars()
        self.create_widgets()
    

    def string_vars(self):
        """Creates or updates tk.StringVars"""
        
        try:
            self.title_var.set(self.recipe.title)
        except:
            self.title_var = tk.StringVar(value=self.recipe.title)
            
        try:
            self.ingredients_var.set(self.recipe.ingredients)
        except:
            self.ingredients_var = tk.StringVar(value=self.recipe.ingredients)
            
        try:
            self.steps_var.set(self.recipe.steps)
        except:
            self.steps_var = tk.StringVar(value=self.recipe.steps)


    def create_widgets(self):
        """Creates widgets"""
        
        self.create_label()
        self.create_menu()


    def create_label(self):
        """Creates the label that consists of the recipe's title"""
        
        # Label for the title
        label_title = ctk.CTkLabel(
            self, 
            text=self.title_var.get(), 
            font=("Arial", 12, "bold"),
            )
        label_title.pack(padx=10, pady=5, side="left", anchor="sw")
        
        # Binds title_var (tk.StringVar) to the label (label auto updates as title_var changes)
        self.bind_text_to_stringvar(label_title, self.title_var)


    def create_menu(self):
        """Creates the menu and its toggle button"""
        
        # Shows/Hides menu
        def toggle_menu():
            if self.menu_sign.get() == "+":
                self.menu_sign.set("-")
                menu_frame.place(relx=0.7, rely=0.7)
            else:
                self.menu_sign.set("+")
                menu_frame.place_forget()

        #Button to toggle menu
        self.menu_sign = tk.StringVar(value="+")
        button_edit = ctk.CTkButton(
            self, 
            textvariable=self.menu_sign, 
            width=3, 
            command=toggle_menu,
            )
        button_edit.pack(padx=5, pady=5, side="left", anchor="se")
        
        # Menu frame (initially hidden)
        menu_frame = ctk.CTkFrame(self, width=50, height=100, bg_color="red")
        
        # Menu Edit button
        menu_button_edit = ctk.CTkButton(
            menu_frame, 
            text="EDIT", 
            width=3, 
            command=self.open_editor,
            )
        menu_button_edit.pack(side="top", fill="x")
        
        # Menu Delete button
        menu_button_delete = ctk.CTkButton(
            menu_frame, 
            text="DELETE", 
            width=3, 
            command=self.remove,
            )
        menu_button_delete.pack(side="top", fill="x")
          

    def bind_text_to_stringvar(self, label, stringvar):
        """Updates the label text when title_var (tk.StringVar) changes"""
        
        # Initial label text
        label.configure(text=stringvar.get())
        
        # Update the label text when the StringVar changes
        stringvar.trace_add("write", lambda *args: label.configure(text=stringvar.get()))  

        
    def update_recipe(self, new_recipe):
        """Updates the RecipeUI with a new recipe"""
        
        self.recipe = new_recipe        
        self.string_vars()
        

    def remove(self):
        """Removes itself from the list of recipes and destroy itself"""
        
        RecipeManager.remove(self.recipe)
        self.destroy()


    def open_editor(self):
        """Opens the editor"""
        
        RecipeManager.open_editor(
            parent=self.parent,
            recipe=self.recipe,
            my_type="edit",
            )
        