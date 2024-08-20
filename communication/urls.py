from django.urls import path
from .api import SchoolNewsView #, HomeworkView, HomeworkSubmissionView, ResourceView, GalleryImageView, GalleryVideoView, MenuView, MealOrderView, LostItemView, FoundItemView, ContactMessageView, NotificationView

urlpatterns = [
    path('api/school-news/', SchoolNewsView.as_view(), name='school-news'),
    # path('api/homework/', HomeworkView.as_view(), name='homework'),
    # path('api/homework-submissions/', HomeworkSubmissionView.as_view(), name='homework-submission'),
    # path('api/resources/', ResourceView.as_view(), name='resources'),
    # path('api/gallery-images/', GalleryImageView.as_view(), name='gallery-images'),
    # path('api/gallery-videos/', GalleryVideoView.as_view(), name='gallery-videos'),
    # path('api/menu/', MenuView.as_view(), name='menu'),
    # path('api/meal-orders/', MealOrderView.as_view(), name='meal-orders'),
    # path('api/lost-items/', LostItemView.as_view(), name='lost-items'),
    # path('api/found-items/', FoundItemView.as_view(), name='found-items'),
    # path('api/contact-messages/', ContactMessageView.as_view(), name='contact-messages'),
    # path('api/notifications/', NotificationView.as_view(), name='notifications'),
]
