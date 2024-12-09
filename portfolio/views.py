from django.shortcuts import render

# Create your views here.
# portfolio/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Skill, Project, Blog
from .serializers import SkillSerializer, ProjectSerializer, BlogSerializer

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
