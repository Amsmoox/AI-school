from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import SchoolNews #, Homework, HomeworkSubmission, Resource, GalleryImage, GalleryVideo, Menu, MealOrder, LostItem, FoundItem, ContactMessage, Notification
from .serializers import SchoolNewsSerializer #, HomeworkSerializer, HomeworkSubmissionSerializer, ResourceSerializer, GalleryImageSerializer, GalleryVideoSerializer, MenuSerializer, MealOrderSerializer, LostItemSerializer, FoundItemSerializer, ContactMessageSerializer, NotificationSerializer

class SchoolNewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        news = SchoolNews.objects.all()
        serializer = SchoolNewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolNewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Repeat similar patterns for Homework, HomeworkSubmission, Resource, GalleryImage, GalleryVideo, Menu, MealOrder, LostItem, FoundItem, ContactMessage, Notification
