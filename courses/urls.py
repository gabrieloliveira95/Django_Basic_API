from django.urls import path
from .views import CourseApiView, EvaluateApiView, CourseManageApiView, EvaluateManageApiView


urlpatterns = [
    path('courses/', CourseApiView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseManageApiView.as_view(), name='courses'),
    path('courses/<int:course_pk>/evaluate',
         EvaluateManageApiView.as_view(), name='courses_evaluate'),
    path('courses/<int:course_pk>/evaluate/<int:evaluate_pk>',
         EvaluateApiView.as_view(), name='courses_evaluates'),

    path('evaluate/', EvaluateApiView.as_view(), name='evaluate'),
    path('evaluate/<int:evaluate_pk>/',
         EvaluateManageApiView.as_view(), name='evaluates')
]
