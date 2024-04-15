import customtkinter as ctk
from recipe_manager import RecipeManager
from recipe_saver import save_recipes, load_recipes


def main():
    window = create_window()
    create_widgets(window)

    load("recipes.csv")
    
    window.mainloop()
    
    save("recipes.csv")


def create_window():
    window = ctk.CTk()
    window.title("RecipeManagerApp")
    window.geometry("600x400")
    
    return window


def create_widgets(window):
    # Add Title
    title_label = ctk.CTkLabel(
        window,
        text="RECIPES",
        font=("Arial", 22, "bold"),
        justify="center"
        )
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Add button to create recipes
    add_button = ctk.CTkButton(
        window,
        text="+",
        width=3,
        command=RecipeManager.open_editor
        )
    add_button.place(relx=0.95, rely=0.9)
    

# for the sake of having 3 functions
def load(file):
    load_recipes(file)


# for the sake of having 3 functions
def save(file):
    save_recipes(file)


if __name__ == "__main__":
    main()
