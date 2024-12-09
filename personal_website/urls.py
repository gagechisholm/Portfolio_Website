# personal_website/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from portfolio.views import SkillViewSet, ProjectViewSet, BlogViewSet

router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
router.register('blogs', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),  # Include the portfolio app's URLs
]