from django.db import models
from django.contrib.auth.models import User

class SchoolNews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='news_author')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    featured_image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    related_files = models.FileField(upload_to='news_files/', blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Keywords for searchability

    def __str__(self):
        return self.title

class Homework(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='homework_teacher')
    class_assigned = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='homework_files/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Assigned', 'Assigned'), ('Submitted', 'Submitted')], default='Assigned')

    def __str__(self):
        return f"{self.title} - {self.class_assigned} - {self.subject}"

class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homework_student')
    submission_date = models.DateTimeField(auto_now_add=True)
    submission_file = models.FileField(upload_to='homework_submissions/', blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.homework.title}"


class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resource_uploader')
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    subject = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=20, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Keywords for searchability

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gallery_uploader')
    upload_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Keywords for searchability

    def __str__(self):
        return self.title

class GalleryVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='gallery_videos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='gallery_video_uploader')
    upload_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)  # Keywords for searchability

    def __str__(self):
        return self.title


class Menu(models.Model):
    date = models.DateField()
    meal_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    allergens = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='canteen/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date} - {self.meal_name}"

class MealOrder(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_order_student')
    menu_item = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Ordered', 'Ordered'), ('Served', 'Served')], default='Ordered')

    def __str__(self):
        return f"{self.student} - {self.menu_item.meal_name} - {self.status}"


class LostItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    date_lost = models.DateField()
    location_lost = models.CharField(max_length=100)
    found = models.BooleanField(default=False)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lost_item_reporter')
    contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='lost_and_found/', blank=True, null=True)

    def __str__(self):
        return f"{self.item_name} - {self.date_lost} - {'Found' if self.found else 'Not Found'}"

class FoundItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    date_found = models.DateField()
    location_found = models.CharField(max_length=100)
    claimed = models.BooleanField(default=False)
    found_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='found_item_reporter')
    contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='lost_and_found/', blank=True, null=True)

    def __str__(self):
        return f"{self.item_name} - {self.date_found} - {'Claimed' if self.claimed else 'Unclaimed'}"


class ContactMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contact_message_sender')
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contact_message_recipient')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"From {self.sender} to {self.recipient} - {self.subject}"


class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50, choices=[('SMS', 'SMS'), ('Email', 'Email'), ('In-App', 'In-App')], default='In-App')

    def __str__(self):
        return f"Notification to {self.recipient} - {self.title}"
