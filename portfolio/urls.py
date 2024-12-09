# portfolio/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, ProjectViewSet, BlogViewSet

router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
router.register('blogs', BlogViewSet)

urlpatterns = router.urls
