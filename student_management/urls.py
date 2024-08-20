from django.urls import path
from .api import StudentListView #, AttendanceView, DisciplineView, AssessmentView, SkillAssessmentView, TimetableView, EducationalGameView, GameAssignmentView

urlpatterns = [
    path('api/students/', StudentListView.as_view(), name='student-list'),
    # path('api/attendance/', AttendanceView.as_view(), name='attendance-list'),
    # path('api/discipline/', DisciplineView.as_view(), name='discipline-list'),
    # path('api/assessments/', AssessmentView.as_view(), name='assessment-list'),
    # path('api/skills-assessment/', SkillAssessmentView.as_view(), name='skill-assessment-list'),
    # path('api/timetable/', TimetableView.as_view(), name='timetable-list'),
    # path('api/educational-games/', EducationalGameView.as_view(), name='educational-game-list'),
    # path('api/game-assignments/', GameAssignmentView.as_view(), name='game-assignment-list'),
]
