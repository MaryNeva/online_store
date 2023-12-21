
from django.urls import path
from products import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
