from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Dashboard
from .serializers import DashboardSerializer

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dashboard = Dashboard.objects.get(user=request.user)
        serializer = DashboardSerializer(dashboard)
        return Response(serializer.data)

    def post(self, request):
        dashboard, created = Dashboard.objects.get_or_create(user=request.user)
        serializer = DashboardSerializer(dashboard, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
