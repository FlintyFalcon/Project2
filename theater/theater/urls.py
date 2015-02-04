from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from theater import views

urlpatterns = patterns('',
    url(r'^$', 'theater.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/', views.movies),
    url(r'^showtimes/', views.showtimes),
    url(r'^about/', views.about),
    url(r'^store/', views.store)

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
