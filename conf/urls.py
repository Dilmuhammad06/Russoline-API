from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

schema_view = get_schema_view(title='Russoline API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('russoline.urls')),
    path('auth/',include('users.urls')),
    path('',include('webrussoline.urls')),
    path('api_schema/', get_schema_view(title='Russoline API',description='Social media'), name='api_schema'),
    path('docs/', TemplateView.as_view(template_name='swagger.html',extra_context={'schema_url':'api_schema'}), name='swagger-ui'),
    
    
]  + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
