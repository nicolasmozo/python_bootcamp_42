from book import Book
from recipe import Recipe

recipe2 = Recipe('Recipe2', 4, 10, [
                 'arroz', 'carne', 'lechuga'], 'normal lunch', 'lunch')
recipe3 = Recipe('Recipe3', 1, 10, [
                 'azucar', 'chocolate', 'cafe'], 'muffin de chocolate y cafe', 'dessert')
recipe1 = Recipe('Recipe1', 3, 5, [
                 'papas', 'salsa', 'aceite'], 'papas bravas', 'starter')
print(recipe1)
recipes = {
    'starter': {
        # Book.add_recipe(recipe1)
    },
    'lunch': {
        # Book.add_recipe(recipe2)
    },
    'dessert': {
        # Book.add_recipe(recipe3)
    }
}
