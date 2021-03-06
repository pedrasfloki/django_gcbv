from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('summary/', include('summary.urls', namespace='summary')),
    path('summary2/', include('summary2.urls', namespace='summary2')),
    path('blog/', include('blog.urls', namespace='blog')),
]

# serving media files only during developement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
