from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


admin.site.site_header="Car Hire"
admin.site.site_title="Car Hire"
admin.site.index_title="Car Hire ADMIN"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('carhirehome.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns= urlpatterns+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)