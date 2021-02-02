from rest_framework import generics
from .models import Course, Evaluate
from .serializers import CourseSerializer, EvaluateSerializer

# ListApiView - Get
# ListCreateApiView - Get / Post


class CourseApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluateApiView(generics.ListCreateAPIView):
    queryset = Evaluate.objects.all()
    serializer_class = EvaluateSerializer

# RetrieveUpdateDestroyAPIView - Get / Post/ Put / Delete
# Update and Delete needs ID


class CourseManageApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluateManageApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluate.objects.all()
    serializer_class = EvaluateSerializer
