import json 
cookbook = {
    'Sandwich': {
        'ingredients': ['ham','bread','cheese','tomatoes'],
        'meal': 'lunch',
        'prep-time': 10
    },
    'Cake': {
        'ingredients': ['flour','sugar','eggs'],
        'meal': 'dessert',
        'prep-time': 60
    },
    'Salad': {
        'ingredients': ['avocado','aragula','tomatoes','spinach'],
        'meal': 'lunch',
        'prep-time': 15
    }   
}

def all_recipe_names():
    for i in cookbook:
        print(i)

def get_details(name):
    print("Recipe for", name, ":")
    print("Ingredients: ", cookbook[name]['ingredients'])
    print("To be eaten for", cookbook[name]['meal'])
    print("Prep-time: ", cookbook[name]['prep-time'])

def delete_recipe(name):
    del cookbook[name]

def add_recipe():
    x = input("Enter a name: ")
    cookbook[x] = {'ingredients' : [item for item in input("Enter ingredients: ").split()],'meal' : input("Enter a meal type: "),'prep-time': int(input("Enter a preparation time: "))}
 
# pretty = json.dumps(cookbook, indent=4)

# print(pretty)
# add_recipe()
# pretty = json.dumps(cookbook, indent=4)

# print(pretty)
