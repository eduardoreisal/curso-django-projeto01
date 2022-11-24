from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'page': 'Home | Recipes',
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'page': 'Category | Recipes',
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={
        'page': 'Recipe | Recipes',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
