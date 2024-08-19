from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Student, Attendance, Discipline, Assessment, SkillAssessment, Timetable, EducationalGame, GameAssignment
from .serializers import StudentSerializer, AttendanceSerializer, DisciplineSerializer, AssessmentSerializer, SkillAssessmentSerializer, TimetableSerializer, EducationalGameSerializer, GameAssignmentSerializer

class StudentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Similar patterns can be repeated for other models like Attendance, Discipline, etc.
#I ll add it when I ll need it 
# Mharrech Ayoub
