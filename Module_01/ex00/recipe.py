class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if isinstance(name, str):
            self.name = name
        else:
            print("Error: Name attribute is not a string")
            exit()
        if isinstance(cooking_lvl, int) and cooking_lvl >= 1 and cooking_lvl <= 5:
            self.cooking_lvl = cooking_lvl
        else:
            print("Error: Cooking lvl attribute is not an int or is out of range 1-5")
            exit()
        if isinstance(cooking_time, int) and cooking_time > 0:
            self.cooking_time = cooking_time
        else:
            print("Error: Cooking time attribute is not an int or is a negative number")
            exit()
        if isinstance(ingredients, list) and all(isinstance(n, str) for n in ingredients):
            self.ingredients = ingredients
        else:
            print(
                "Error: Ingredients attribute is not a list or elements are not strings")
            exit()
        if isinstance(description, str) or description == None:
            self.description = description
        else:
            print("Error: Description attribute is not a string. *It can be empty(None)")
            exit()
        if isinstance(recipe_type, str) and recipe_type == 'starter' or recipe_type == 'lunch' or recipe_type == 'dessert':
            self.recipe_type = recipe_type
        else:
            print(
                "Error: Recype type is not a string or type is neither starter/lunch/dessert")
            exit()

    def __str__(self):
        '''Return the string to print with the recipe info'''
        return f" Recipe {self.name} has a cooking lvl of {self.cooking_lvl}. Cooking time is {self.cooking_time} and its ingredients are {self.ingredients}. Description (if any): {self.description}. Type of recipe: {self.recipe_type}"
