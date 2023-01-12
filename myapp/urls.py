from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('gettime/',views.current_date_time,name="current_date_time"),
    path("getcourse/<str:course_name>",views.get_course,name="course_name")
]
