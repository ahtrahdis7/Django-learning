from django.urls import path,include
from appTwo import views
urlpatterns = [
    path('', views.helpp, name='helpp'),
]