import tkinter as tk
import customtkinter as ctk
from recipe_manager import RecipeManager


class RecipeEditorUI(ctk.CTkFrame):
    """Displays the recipe editor"""
    
    def __init__(self, parent, recipe, my_type="add"):
        """Takes a recipe"""
        
        super().__init__(master=None)
        self.place(relheight=1, relwidth=1)
                 
        self.parent = parent
        self.recipe = recipe
        self.my_type = my_type
        
        self.string_vars()
        self.create_widgets()
        

    def string_vars(self):
        """Sets up tk.StringVars"""
        
        self.title_var = tk.StringVar(value=self.recipe.title)                            
        self.ingredients_var = tk.StringVar(value=self.recipe.ingredients)       
        self.steps_var = tk.StringVar(value=self.recipe.steps)
        

    def create_widgets(self):
        """Creates the widgets"""

        self.create_title_frame()
        self.create_ingredients_frame()
        self.create_steps_frame()
        self.create_save_button()
        

    def create_title_frame(self):
        """Creates the title frame and adds a label and entry"""

        # Title frame
        title_frame = ctk.CTkFrame(self)
        title_frame.place(relwidth=1, relheight=0.4, relx=0.5, rely=0, anchor="n")

        # Title label
        title_label = ctk.CTkLabel(
            title_frame, 
            text="Title:",
            )
        title_label.pack(anchor="center", expand=True)

        # Title entry
        title_entry = ctk.CTkEntry(
            title_frame, 
            textvariable=self.title_var,
            )
        title_entry.pack(anchor="center", expand=True)
        

    def create_ingredients_frame(self):
        """Creates the ingredients frame and adds a label and textbox"""
        
        # Ingredients frame
        ingredients_frame = ctk.CTkFrame(self)
        ingredients_frame.place(relwidth=0.3, relheight=0.6, relx=0.3, rely=0.4, anchor="ne")

        # Ingredients label
        ingredients_label = ctk.CTkLabel(
            ingredients_frame, 
            text="Ingredients:",
            )
        ingredients_label.pack()

        # Ingredients textbox
        ingredients_textbox = ctk.CTkTextbox(
            ingredients_frame,
            )
        ingredients_textbox.pack(padx=10, pady=25, fill="both", expand=True)

        # Binds ingredients_var (tk.StringVar) to the label (label auto updates as ingredients_var changes)
        self.bind_text_to_stringvar(ingredients_textbox, self.ingredients_var)
     
        
    def create_steps_frame(self):
        """Creates the steps frame and adds a label and textbox"""
        
        # Steps frame
        steps_frame = ctk.CTkFrame(self)
        steps_frame.place(relwidth=0.7, relheight=0.6, relx=0.3, rely=0.4, anchor="nw")

        # Steps label
        steps_label = ctk.CTkLabel(
            steps_frame, 
            text="Steps:",
            )
        steps_label.pack()

        # Steps textbox
        steps_textbox = ctk.CTkTextbox(
            steps_frame,
            )
        steps_textbox.pack(padx=10, pady=25, fill="both", expand=True)

        # Binds steps_var (tk.StringVar) to the label (label auto updates as steps_var changes)
        self.bind_text_to_stringvar(steps_textbox, self.steps_var)


    def create_save_button(self):
        """Creates save button at the bottom of the screen (outside any frames)"""

        # Save button
        save_button = ctk.CTkButton(
            self, 
            text="Save", 
            command=self.save_recipe,
            )
        save_button.place(relx=0.5, rely=0.9, anchor="center")
        

    def bind_text_to_stringvar(self, textbox, stringvar):
        """Updates the textboxes' text when ingredients_var/steps_var (tk.StringVar) changes"""

        textbox.insert("1.0", stringvar.get())
        textbox.bind(
            "<KeyRelease>",
            lambda event: stringvar.set(textbox.get("1.0", "end-1c")),
        )
        

    def save_recipe(self):
        """Update its Recipe obj, have Reciper Manager add the recipe to the list, and close the window"""
        
        self.recipe.title = self.title_var.get()
        self.recipe.ingredients = self.ingredients_var.get()
        self.recipe.steps = self.steps_var.get()
       
        RecipeManager.close_editor(
            parent=self.parent,
            recipe=self.recipe,
            my_type=self.my_type,
            )
        self.destroy()