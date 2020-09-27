from django.contrib import admin
from django.urls import path, include
from resources import views as resources_views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'philosophers', resources_views.PhilosopherViewSet)
router.register(r'books', resources_views.BookViewSet)
router.register(r'ideas', resources_views.IdeaViewSet)
router.register(r'schools', resources_views.SchoolViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]