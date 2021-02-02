from rest_framework import serializers
from . models import Course, Evaluate


class EvaluateSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwagrs = {
            'email': {'write_only': True},
        }
        model = Evaluate
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comments',
            'evaluate',
            'publicated',
            'active'
        )


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'publicated',
            'active'
        )
