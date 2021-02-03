from django.urls import path
from .views import CourseApiView, EvaluateApiView, CourseApiManage, EvaluateApiManage

urlpatterns = [
    # View All Courses
    path('courses/', CourseApiView.as_view(), name='courses_view_all'),

    # View All Evaluates
    path('evaluate/', EvaluateApiView.as_view(), name='evaluate_view_all'),

    # Change Courses by Primary Key
    path('courses/<int:pk>/', CourseApiManage.as_view(), name='courses_by_pk'),

    # Change Evaluates by Primary Key
    path('evaluate/<int:evaluate_pk>/',
         EvaluateApiManage.as_view(), name='evaluate_pk'),

    # Change Evaluates by Courses Primary Key
    path('courses/<int:course_pk>/evaluate',
         EvaluateApiManage.as_view(), name='evaluates_by_courses_pk'),

    # Change Evaluates by Courses Primary Key and Evaluates Primary Key
    path('courses/<int:course_pk>/evaluate/<int:evaluate_pk>/',
         EvaluateApiManage.as_view(), name='evaluates_by_courses_pk')
]
