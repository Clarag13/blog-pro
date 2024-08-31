from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profissoes/', views.profissoes, name='profissoes'),
    path('passatempos/', views.passatempos, name='passatempos'),
    path('sobre/', views.sobre, name='sobre'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)