from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('classes', views.ClassesViewSet)
router.register('comps', views.CompsViewSet)


urlpatterns = [
    path('', views.main),
    path('rout/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]