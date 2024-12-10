# portfolio/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    SkillViewSet,
    ProjectViewSet,
    BlogViewSet,
    FreeLanceInquiryView,
    InfoRequestView,
)

# Router for existing viewsets
router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)
router.register('blogs', BlogViewSet)

# Explicit paths for the new views
urlpatterns = [
    path('freelance-inquiry/', FreeLanceInquiryView.as_view(), name='freelance-inquiry'),
    path('info-request/', InfoRequestView.as_view(), name='info-request'),
]

# Combine router URLs with custom paths
urlpatterns += router.urls
