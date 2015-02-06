from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import home, movies, synopsis, about, store


urlpatterns = patterns('',
                       # url(r'^$', 'theater.views.home', name='home'),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', home),
                       url(r'^movies/', movies),
                       url(r'^synopsis/', synopsis),
                       url(r'^about/', about),
                       url(r'^store/', store)
)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
