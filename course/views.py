from django.shortcuts import render
from course.models import Student
from . forms import StudentsRegis

def studentInfo(request):
    stud = Student.objects.all()
    return render(request,'course/course.html', {'stu':stud})

def showformdata(request):
    fm=StudentsRegis()

    return render(request,'course/form.html',{'form':fm})

  





# Create your views here.
# def course(request):
#     return (request, 'course/course.html')

# def combine(request):
#     a = course()
#     b = studentInfo()

#     context = {
#         'f1':a,
#         'f2':b
#     }
#     return render(request, 'course/course.html', context)