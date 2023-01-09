from django.urls import path
from .import views

urlpatterns = [
    path('frontend/',views.this,name='Live Frontend'),
    path('apiview/',views.ApiList.as_view(), name = 'API List'),
    
]