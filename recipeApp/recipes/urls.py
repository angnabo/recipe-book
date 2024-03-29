from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('get/', views.get, name='get'),
    path('activity/', views.activity, name='activity'),
    path('get_recipe_likes_activity/', views.get_recipe_likes_activity, name='get_recipe_likes_activity'),
    path('<int:recipe_id>/edit/', views.edit, name='edit'),
    path('<int:recipe_id>/delete/', views.delete, name='delete'),
    path('<int:recipe_id>/', views.details, name='details'),
    path('<int:recipe_id>/like/', views.like, name='like'),
    path('<int:recipe_id>/add_comment/', views.add_comment, name='add_comment')
]
