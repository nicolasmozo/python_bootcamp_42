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
 
def run(x):
    if int(x) == 1:
        add_recipe()
    elif int(x) == 2:
        delete_recipe(input("Please enter a recipe name to be deleted: "))
    elif int(x) == 3:
        get_details(input("Please enter a recipe name to get its details: "))
    elif int(x) == 4:
        all_recipe_names()
    elif int(x) == 5:
        print("Coookbook closed. Goodbye !")
        exit()
    else:
        options()

def options():
    print("Welcome to the Python Cookbook !")
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    x = input("Please select an option: ")
    try: 
        int(x)
        while(int(x) == 1 or  int(x) == 2 or  int(x) == 3 or  int(x) == 4 or  int(x) ==5):
            run(x)
            x = input("Please select an option: ")
    except ValueError:
        print("Sorry, this option does not exist.")
        options()

options()