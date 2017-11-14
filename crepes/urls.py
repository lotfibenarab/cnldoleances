#from django.conf.urls import url, include
#from django.contrib import admin
#from blog import views
#from django.conf import settings

#urlpatterns = [
#    url(r'^blog/', include('blog.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#]
from django.conf.urls import include, url

from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # D'autres éventuelles directives.

    # Celles de notre application blog notamment

    # ...
    url(r'^doleances/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
