from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import landing.views

urlpatterns = [
    path('', landing.views.index, name='index'),
    path('news', landing.views.news, name='news'),
    path('news/<int:pk>', landing.views.NewsDetailView.as_view(), name='news-detail'),
    path('events', landing.views.events, name='events'),
    path('events/<int:pk>', landing.views.EventDetailView.as_view(), name='event-detail'),
    path('products/', landing.views.our_products, name='our_products')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)