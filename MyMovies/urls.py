from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from movies.api.viewsets import *

"""API routers."""
router = routers.DefaultRouter()

router.register(r'movie',MovieViewSet,base_name='movie')
router.register(r'actor',ActorViewSet,base_name='actor')
router.register(r'country',CountryViewSet,base_name='country')
router.register(r'language',LanguageViewSet,base_name='language')
router.register(r'genres',GenresViewSet,base_name='genres')
router.register(r'certification',CertificationViewSet,base_name='genres')

urlpatterns = [
    # Examples:
    # url(r'^$', 'MyMovies.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
]
