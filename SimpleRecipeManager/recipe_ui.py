import tkinter as tk
import customtkinter as ctk
from PIL import Image
from recipe_manager import RecipeManager

class RecipeUI(ctk.CTkFrame):
    """Displays a recipe"""
    
    def __init__(self, parent=None, recipe=None):
        """Takes a Recipe obj and uses it to set itself up"""
        
        super().__init__(master=parent, width=300, height=300)
        self.grid(row=0, column=0, sticky="nsew")

        self.parent = parent
        self.recipe = recipe
        
        self.string_vars()
        self.create_widgets()
    

    def string_vars(self):
        """Creates or updates tk.StringVars"""
        
        self.title_var = tk.StringVar(value=self.recipe.title)
        self.ingredients_var = tk.StringVar(value=self.recipe.ingredients)
        self.steps_var = tk.StringVar(value=self.recipe.steps)


    def create_widgets(self):
        """Creates widgets"""
        
        self.create_icon()
        self.create_label()
        self.create_menu()


    def create_icon(self):
        """Creates an icon representing the recipe"""
        
        # Load the icon image
        icon_image = Image.open("images/coxinha.jpg")
        #icon_image = icon_image.resize((200, 200), Image.Resampling.LANCZOS)
        
        # Convert PIL image to CTkImage
        icon_photo = ctk.CTkImage(
            dark_image=icon_image, 
            size=(300, 200),
            )
        image_button = ctk.CTkLabel(master=self, image=icon_photo, text="")
        image_button.pack(side="top", anchor="n")
        

    def create_label(self):
        """Creates the label that consists of the recipe's title"""
        
        # Label for the title
        label_title = ctk.CTkLabel(
            self, 
            text=self.title_var.get(), 
            font=("Arial", 14, "bold"),
            anchor="center"
        )
        label_title.pack(side="top", anchor="n")

        # Binds title_var (tk.StringVar) to the label (label auto updates as title_var changes)
        self.bind_text_to_stringvar(label_title, self.title_var)


    def create_menu(self):
        """Creates the menu and its toggle button"""
        
        def toggle_menu():
            if self.menu_sign.get() == "+":
                self.menu_sign.set("-")
                menu_frame.pack(side="right", fill="y", padx=10, pady=10)
            else:
                self.menu_sign.set("+")
                menu_frame.pack_forget()

        # Button to toggle menu
        self.menu_sign = tk.StringVar(value="+")
        button_edit = ctk.CTkButton(
            self, 
            textvariable=self.menu_sign, 
            width=10, 
            command=toggle_menu,
            corner_radius=8
        )
        button_edit.pack(padx=5, pady=5, side="right", anchor="ne")

        # Menu frame (initially hidden)
        menu_frame = ctk.CTkFrame(self, width=100, height=100, bg_color="white")
        
        # Menu Edit button
        menu_button_edit = ctk.CTkButton(
            menu_frame, 
            text="EDIT", 
            width=10, 
            command=self.open_editor,
            corner_radius=8
        )
        menu_button_edit.pack(side="top", fill="x", pady=5)
        
        # Menu Delete button
        menu_button_delete = ctk.CTkButton(
            menu_frame, 
            text="DELETE", 
            width=10, 
            command=self.remove,
            corner_radius=8
        )
        menu_button_delete.pack(side="top", fill="x", pady=5)


    def bind_text_to_stringvar(self, label, stringvar):
        """Updates the label text when the StringVar changes"""
        
        label.configure(text=stringvar.get())
        stringvar.trace_add("write", lambda *args: label.configure(text=stringvar.get()))  


    def update_recipe(self, new_recipe):
        """Updates the RecipeUI with a new recipe"""
        
        self.recipe = new_recipe        
        self.string_vars()
        self.create_widgets()


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
