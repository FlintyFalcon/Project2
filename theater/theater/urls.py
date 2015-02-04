from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'theater.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^showtimes/', include(views.showtimes)),
    url(r'^store/', include(views.store)),

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
