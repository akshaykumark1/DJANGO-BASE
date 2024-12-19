# gallery/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_gallery, name='user_gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete/<pk>', views.delete, name='delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
