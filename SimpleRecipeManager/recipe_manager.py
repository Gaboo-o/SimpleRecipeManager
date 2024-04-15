from recipe import Recipe


class RecipeManager:
    """Manages recipes, including adding, removing, and opening editors."""
    
    recipes = []
    recipes_ui = []
        

    @classmethod
    def add(cls, recipe_list, recipe):
        """Add a recipe to the list."""
        
        recipe_list.append(recipe)


    @classmethod
    def remove(cls, recipe):
        """Remove a recipe from the list."""
        
        cls.recipes_ui = [r for r in cls.recipes_ui if r.recipe.my_id != recipe.my_id]
        cls.recipes = [r for r in cls.recipes if r != recipe]


    @classmethod
    def open_editor(cls, recipe=None, my_type="add"):
        """Open the editor with provided title, ingredients, and steps."""
        
        from recipe_editor_ui import RecipeEditorUI # here to avoid circular import
        
        if not recipe:
            recipe = Recipe()
        RecipeEditorUI(recipe, my_type)


    @classmethod
    def close_editor(cls, recipe=None, my_type="add", **kwargs):
        """Close the editor and add edited recipe to the list."""
        
        from recipe_ui import RecipeUI # here to avoid circular import     
        
        if recipe is None: # When app is first opened (loading recipes)            
            recipe = Recipe(
                kwargs.get("title", ""), 
                kwargs.get("ingredients", ""), 
                kwargs.get("steps", "")
                )            
            
        if my_type == "edit": # Update current RecipeUI
            for recipe_ui in cls.recipes_ui:                
                if recipe_ui.recipe.my_id == recipe.my_id:                    
                    recipe_ui.update_recipe(recipe)                       
                    break             
        else: # Create new RecipeUI            
            cls.add(cls.recipes, recipe)         
            cls.add(cls.recipes_ui, RecipeUI(recipe=recipe))            
