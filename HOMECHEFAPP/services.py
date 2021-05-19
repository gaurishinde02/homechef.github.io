from .models import Ingredient
from .models import Recipe


# This method will create a dictionary(key-value pairs) of RecipeName and Ingredients from Recipes table
def create_master_recipe_dictionary():
    recipeall = Recipe.objects.all()
    masterrecipedict = {}
    for item in recipeall.iterator():
        masterrecipedict[item.recipename] = set(item.ingredients.split(","))
    return masterrecipedict


# This method will get all the possible recipe that could be made, based on the ingredients selected by user
def get_possible_recipes(request):
    possiblerecipes = set()
    ingredientsselected = set()
    ingredients = Ingredient.objects.all()
    if request.method == 'POST':
        for item in ingredients.iterator():
            if request.POST.get(item.ingredientname):
                ingredientsselected.add(item.ingredientname)
    print("Ingredients selected: ", ingredientsselected)

    masterrecipedict = create_master_recipe_dictionary()
    print("Master recipe dictionary: ", masterrecipedict)

    for recipe, ingredients in masterrecipedict.items():
        for item in ingredientsselected:
            if item in ingredients:
                possiblerecipes.add(recipe)
    print("Possible recipe: ", possiblerecipes)
    return possiblerecipes
