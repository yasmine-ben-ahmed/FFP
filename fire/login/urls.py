from django.urls import path,include
from . import views

urlpatterns=[
    #path('',views.connect,name='connect'),
    path('',views.connectas,name='connectas'),
    path('client/',views.connectasclient,name='connectasclient'),
    path('supervisor/',views.connectassupervisor,name='connectassupervisor'),

]