
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'FIRE--Forest admin'
admin.site.site_title = 'FIRE_Forest admin'
admin.site.site_url = 'http://fireforest.com/'
admin.site.index_title = 'FIRE--Forest administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('',include("home.urls")),
    path('Inscrire', include('signup.urls')),    
    path('connect/', include('login.urls')),
    path('project/',include("map.urls")),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

