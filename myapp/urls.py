from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index,name="index"),
    path("fish/home/",home,name="fish-home"),
    path("fish/card/",fish_card_member,name="fish-card-member"),
    path('fish/card_detail/<int:fish_id>/', fish_card_detail_member, name='fish-card-detail-member'),

    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('user/logout/', UserLogoutView.as_view(), name='user-logout'),
    path("user/register/",registration_view,name="register"),

    path("fishkeeper/", staff_home, name="staff-home"),

    path('fishkeeper/fishlist',fish_list,name='fish_list'),
    path('fishkeeper/detail/<int:fish_id>/', fish_detail, name='fish_detail'),
    path("fishkeeper/card/",fish_card,name="fish_card"),  
    path('fishkeeper/card_detail/<int:fish_id>/', fish_card_detail, name='fish_card_detail'),

    path("fishkeeper/createfish/",create_fish,name="create_fish"),
    path("fishkeeper/addfood/<int:fish_id>",add_food,name="add_food"),
    path("fishkeeper/addHabitat/<int:fish_id>",add_habitat,name="add_habitat"),
    path('fishkeeper/delete/<int:fish_id>/', delete_fish, name='delete_fish'),
    
    path('fishkeeper/edit/<int:fish_id>/', edit_fish, name='edit_fish'),
    path('fishkeeper/editfood/<int:food_id>/', edit_food, name='edit_food'),
    path('fishkeeper/edithabitat/<int:habitat_id>/', edit_habitat, name='edit_habitat'),

    path('fishkeeper/dashboard/',dashboard,name="dashboard"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


