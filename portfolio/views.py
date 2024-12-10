from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

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

class FreeLanceInquiryView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        return Response({"message": "Freelance Inquiry Received"}, status=status.HTTP_100_OK)

class InfoRequestView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        message = request.data.get('message')

        return Response({"message": "Message Request Received"}, status=status.HTTP_100_OK)