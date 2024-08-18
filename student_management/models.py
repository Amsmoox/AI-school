from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)  # Matricule or ID
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    nationality = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    grade_level = models.CharField(max_length=20)
    class_assigned = models.CharField(max_length=100)
    guardian_name = models.CharField(max_length=100)  # Parent or Guardian
    guardian_phone = models.CharField(max_length=15)
    guardian_email = models.EmailField()
    guardian_relation = models.CharField(max_length=50)  # Relationship to student
    disability = models.BooleanField(default=False)
    disability_details = models.TextField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    emergency_contact_relation = models.CharField(max_length=50)
    medical_conditions = models.TextField(blank=True, null=True)
    previous_school = models.CharField(max_length=100, blank=True, null=True)
    transportation_needs = models.BooleanField(default=False)
    transportation_details = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')])
    reason_for_absence = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
    
class Discipline(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    incident_date = models.DateField()
    incident_type = models.CharField(max_length=100)
    description = models.TextField()
    action_taken = models.CharField(max_length=255)
    reported_by = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.incident_date} - {self.incident_type}"
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assessment_type = models.CharField(max_length=100)
    date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.assessment_type} - {self.score}"


