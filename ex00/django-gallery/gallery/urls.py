from django.urls import path
from .views import GalleryView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', GalleryView.as_view(), name="gallery"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
