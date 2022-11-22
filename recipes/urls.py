from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path("", views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('', views.home, name="home"),
    path('recipes/<int:id>', views.recipe, name="recipe"),
]
