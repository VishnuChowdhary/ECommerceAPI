from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drfecommerce.product import views

router = DefaultRouter()
router.register(r"category", views.CategoryView)
router.register(r"brand", views.BrandView)
router.register(r"product", views.ProductView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='Schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='Schema')),
]
