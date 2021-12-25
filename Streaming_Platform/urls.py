from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# Swagger Docs
from rest_framework_swagger.views import get_swagger_view

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', schema_view, name="docs"),

    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
