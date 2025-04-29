from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee,Department
from.serializers import EmployeeSerializer,DepartmentSerializer
from django.contrib.auth.models import User

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.employee.role == 'admin'

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'], 
    permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        employee = request.user.employee
        serializer = self.get_serializer(employee)
        return Response(serializer.data)
    
