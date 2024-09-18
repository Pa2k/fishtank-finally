from django.urls import path,include
from .views import *
urlpatterns = [
    path("",panel,name="panel"),
    path("create/fish/",create_fish,name="create_fish"),
    path("create/food/",create_food,name="create_food"),
    path("create/habitat/", create_habitat, name="create_habitat"),
    path('fish/',fish_list,name='fish_list'),
    path('fish/<int:fish_id>/', fish_detail, name='fish_detail'),
     path('delete/<int:fish_id>/', delete_fish, name='delete_fish'),
]
