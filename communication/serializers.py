from rest_framework import serializers
from .models import SchoolNews, Homework, HomeworkSubmission, Resource, GalleryImage, GalleryVideo, Menu, MealOrder, LostItem, FoundItem, ContactMessage, Notification

class SchoolNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolNews
        fields = '__all__'

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class GalleryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideo
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MealOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealOrder
        fields = '__all__'

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = '__all__'

class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
