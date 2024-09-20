from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",panel,name="panel"),
    
    path('fish/',fish_list,name='fish_list'),
    path('fish/<int:fish_id>/', fish_detail, name='fish_detail'),
    path("fish/create/",create_fish,name="create_fish"),
    path('fish/delete/<int:fish_id>/', delete_fish, name='delete_fish'),
    path('fish/edit/<int:fish_id>/', edit_fish, name='edit_fish'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
