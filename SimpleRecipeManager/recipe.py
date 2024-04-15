class Recipe:
    """Represents a recipe with title, ingredients, and steps"""
    
    my_id = 0

    # Takes Strings
    def __init__(self, title="", ingredients="", steps=""):
        self.my_id = Recipe.my_id
        Recipe.my_id += 1

        self._title = title
        self._ingredients = ingredients
        self._steps = steps    

    # To compare two recipes
    def __eq__(self, other):
        if isinstance(other, Recipe):
            return self.my_id == other.my_id
        return False
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        
    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):      
        self._steps = value

