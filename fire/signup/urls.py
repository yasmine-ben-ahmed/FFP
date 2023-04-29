from django.urls import path,include
from . import views

urlpatterns=[
    path('_<str:pk>',views.compte,name='compte'),
    path('',views.compte,name='compte'),
   # path('<str:variable>/map/<str:pseudo>',views.stocker_polygone,name='map')

  # path('<str:variable>/map/<str:pseudo>', include('map.urls')),
  # path('<str:pk>/map', include('map.urls')),
]


