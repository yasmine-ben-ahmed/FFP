
from django.urls import path,include
from . import views
from django.contrib.auth import views as mdp
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.connectas,name='connectas'),
    path('client/',views.connectasclient,name='connectasclient'),
    path('supervisor/',views.connectassupervisor,name='connectassupervisor'),

    path('reset_password/', mdp.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('reset_password_done/', mdp.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', mdp.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', mdp.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]