from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Custom admin text  
admin.site.site_header = 'Contacts'
admin.site.index_title = 'Welcome To Project'
admin.site.site_title = 'Control Panel'