from django.urls import path
from .views import CourseApiView, EvaluateApiView, CourseManageApiView, EvaluateManageApiView


urlpatterns = [
    path('courses/', CourseApiView.as_view(), name='courses'),
    path('evaluate/', EvaluateApiView.as_view(), name='evaluate'),
    path('courses/<int:pk>/', CourseManageApiView.as_view(), name='courses'),
    path('evaluate/<int:pk>/', EvaluateManageApiView.as_view(), name='evaluate')
]
