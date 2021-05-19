from django.shortcuts import render
from .models import Ingredient
from .services import get_possible_recipes


# Create your views here.
def home(request):
    context = {
        'ingredients': Ingredient.objects.all
    }
    return render(request, 'HOMECHEFAPP/home.html', context)


def possible_recipes_view(request):
    possiblerecipes = get_possible_recipes(request)
    result_dictionary = {
        'recipes': possiblerecipes
    }
    print("Result dictionary: ", result_dictionary)
    return render(request, 'HOMECHEFAPP/possiblerecipes.html', result_dictionary)
