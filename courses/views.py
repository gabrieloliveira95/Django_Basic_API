from rest_framework import generics
from rest_framework.generics import get_object_or_404
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

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.queryset.get('course_id'))
        return self.queryset.all()


# RetrieveUpdateDestroyAPIView - Get/Put/Patch/Delete
# Update and Delete needs ID


class CourseApiManage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluateApiManage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluate.objects.all()
    serializer_class = EvaluateSerializer

    def get_object(self):
        print(self.kwargs)
        if self.kwargs.get('course_pk'):
            return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('course_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('evaluate_pk'))
