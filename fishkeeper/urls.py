from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path("",fish_card,name="fish_card"),
    path('fish/',fish_list,name='fish_list'),
    path('fish/detail/<int:fish_id>/', fish_detail, name='fish_detail'),
    path('fish/card_detail/<int:fish_id>/', fish_card_detail, name='fish_card_detail'),
    
    path("fish/createfish/",create_fish,name="create_fish"),
    path("fish/addfood/<int:fish_id>",add_food,name="add_food"),
    path("fish/addHabitat/<int:fish_id>",add_habitat,name="add_habitat"),
    path('fish/delete/<int:fish_id>/', delete_fish, name='delete_fish'),
    
    path('fish/edit/<int:fish_id>/', edit_fish, name='edit_fish'),
    path('fish/editfood/<int:food_id>/', edit_food, name='edit_food'),
    path('fish/edithabitat/<int:habitat_id>/', edit_habitat, name='edit_habitat'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
