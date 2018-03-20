from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from simplemooc.core import views
from simplemooc.courses import views

urlpatterns = [
    path('', include('simplemooc.core.urls')),
    path('cursos/', include('simplemooc.courses.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)