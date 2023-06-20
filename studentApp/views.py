from django.views.generic import ListView
from .models import Student, Course

# Create your views here.
class StudentListView(ListView):
    model = Student

class CourseListView(ListView):
    model = Course