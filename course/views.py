from django.shortcuts import render
from course.models import Student
# Create your views here.
# def course(request):
#     return (request, 'course/course.html')

def studentInfo(request):
    stud = Student.objects.all()
    for s in stud:
        print(s)
    print('myoutput',stud)
    return render(request,'course/course.html', {'stu':stud})

# def combine(request):
#     a = course()
#     b = studentInfo()

#     context = {
#         'f1':a,
#         'f2':b
#     }
#     return render(request, 'course/course.html', context)