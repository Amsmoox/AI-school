from rest_framework import serializers
from .models import Student, Attendance, Discipline, Assessment, SkillAssessment, Timetable, EducationalGame, GameAssignment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class SkillAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillAssessment
        fields = '__all__'

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'

# class EducationalGameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EducationalGame
#         fields = '__all__'

# class GameAssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GameAssignment
#         fields = '__all__'
