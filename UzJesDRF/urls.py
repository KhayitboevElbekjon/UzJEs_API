from asosiy.views import *
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="UzJes API",
      default_version='v1',
      description="UzJes API",
      contact=openapi.Contact("Xayitboeyev Elbekjon <backenddevolpment@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('bolim',BolimSerializerAPI)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('',schema_view.with_ui('swagger',cache_timeout=0)),
   path('bolim/',BolimSerializerAPI.as_view()),
   path('bolimlar/<int:pk>',BolimgaTegishliSozlar.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
