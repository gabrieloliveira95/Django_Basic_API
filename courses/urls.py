from django.urls import path
from .views import CourseApiView, EvaluateApiView, CourseApiManage, EvaluateApiManage

urlpatterns = [
    path('courses/', CourseApiView.as_view(), name='courses_view_all'),

    path('evaluate/', EvaluateApiView.as_view(), name='evaluate_view_all'),

    path('courses/<int:pk>/', CourseApiManage.as_view(), name='courses_by_pk'),

    path('evaluate/<int:evaluate_pk>/',
         EvaluateApiManage.as_view(), name='evaluate_pk'),

    path('courses/<int:course_pk>/evaluate',
         EvaluateApiManage.as_view(), name='evaluate_by_courses_pk')
]
