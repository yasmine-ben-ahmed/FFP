from django.urls import path,include
from . import views

urlpatterns=[
    path('_<str:pk>',views.compte,name='compte'),
    path('',views.compte,name='compte'),

]


