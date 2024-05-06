from django.contrib import admin

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pages.views import PageViewSet


router = DefaultRouter()
router.register(r'pages', PageViewSet, basename='page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
