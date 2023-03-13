from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from my_site import settings
from projects.views import main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
