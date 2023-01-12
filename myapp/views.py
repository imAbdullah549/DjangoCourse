from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    return HttpResponse("welcome to home page")
def current_date_time(request):
    now = datetime.datetime.now()
    html = "<h2>current time is %s</h2>" % now
    return HttpResponse(html)

def get_course(request,course_name):
    course={
        "frontend":"reatc",
        "backend":"django",
        "fullStack":"mern",
    }
    request_course=course[course_name]
    html= "<h3>your desire course is %s </h3>" % request_course
    return HttpResponse(html)