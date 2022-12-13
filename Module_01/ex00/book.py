import datetime as dt
import recipe as rp


class Book:
    def __init__(self, name, recipes_list):
        if isinstance(name, str):
            self.name = name
            self.last_update = dt.datetime.now()
        else:
            print("Error: Name attribute is not a string")
            exit()
        self.creation_date = dt.datetime.now()
        if isinstance(recipes_list, dict):
            #self.recipes_list = dict({"lunch" : [],  "starter" : [],"dessert" : [] })
            for i in recipes_list.keys():
                if i == 'starter' or i == 'lunch' or i == 'dessert':
                    self.recipes_list = recipes_list
                    self.last_update = dt.datetime.now()
        else:
            print(
                "Error: Name attribute is not a dict or key are neither starter/lunch/dessert")
            exit()

    def __str__(self):
        return f'This book is called {self.name}. Creation date was {self.creation_date}. Last update was {self.last_update} and list of recipes is {self.recipes_list}'

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for i in self.recipes_list:
            for j in self.recipes_list[i]:
                if j == name:
                    return str(name)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for i in self.recipes_list:
            for j in self.recipes_list[i]:
                if j == recipe_type:
                    types = []
                    types.append(i.name)
        for i in self.types:
            for j in self.recipes_list:
                if j == i:
                    print(str(j))

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, dict):
            recipe = rp.Recipe(name=recipe.name, cooking_lvl=recipe.cooking_lvl, cooking_time=recipe.cooking_time,
                               ingredients=recipe.ingredients, description=recipe.descriptio, recipe_type=recipe.recipe_type)
            self.last_update = dt.datetime.now()
        else:
            print("Error: Recipe attribute is not a dictionary")
            exit()
