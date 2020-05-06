from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post import views
from post.views import index, blog, post, search



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name= 'post-list'),
    path('post/<id>', post, name= 'post-detail'),
    path('search/', search, name='search'),
    #path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
