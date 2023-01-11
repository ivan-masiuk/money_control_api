from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'api-auth/', include(
            'rest_framework.urls',
            namespace='rest_framework',
        ),
    ),

    path("api/v1/", include("balance.urls")),
    path("api/v1/", include("user.urls")),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
