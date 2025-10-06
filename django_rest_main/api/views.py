from students.models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["GET","POST"])
def studentsView(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students,many="true")
        
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        try:
            serializer = StudentSerializer(data = request.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

@api_view(["GET","DELETE"])        
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)