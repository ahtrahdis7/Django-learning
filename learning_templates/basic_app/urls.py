from basic_app import views
from django.urls import path


#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('', views.base, name='base'),
    path('relative/', views.relative, name='relative'),
    path('other', views.other, name= 'other'),
]