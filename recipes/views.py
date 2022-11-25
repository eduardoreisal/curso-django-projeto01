from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'title': 'Home | Recipes',
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')
    # If object is not found return None
    category_name = getattr(recipes.first(), 'category', None)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{category_name} | Recipes',
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={
        'title': 'Recipe | Recipes',
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
