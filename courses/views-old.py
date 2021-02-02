from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Evaluate
from .serializers import CourseSerializer, EvaluateSerializer


class CourseApiView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EvaluateApiView(APIView):
    def get(self, request):
        evaluates = Evaluate.objects.all()
        serializer = EvaluateSerializer(evaluates, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EvaluateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
