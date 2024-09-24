from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from home.views import *
from vege.views import * 
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # type: ignore
urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact ,name="contact"),
    path('about/', about ,name="about"),
    path('recipes/', recipes, name='recipes'),
    path('delete_recipe/<id>/', delete_recipe, name="delete_recipe"),
    path('update_recipe/<id>/', update_recipe, name="update_recipe"),
    path('login/', login_page , name="login" ),
    path('register/', register , name='register'),
    path('logout/', login_page , name="logout"), 
    
    path('success_page/',success_page,name="success_page"),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
