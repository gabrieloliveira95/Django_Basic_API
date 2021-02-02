from django.urls import path
from .views import CourseApiView, EvaluateApiView


urlpatterns = [
    path('courses/', CourseApiView.as_view(), name='courses'),
    path('evaluate/', EvaluateApiView.as_view(), name='evaluate')
]
