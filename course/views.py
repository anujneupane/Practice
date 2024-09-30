from django.shortcuts import render
from course.models import Student
from . forms import StudentsRegis
from . forms import StudentsRegistration

def studentInfo(request):
    stud = Student.objects.all()
    return render(request,'course/course.html', {'stu':stud})

def showformdata(request):
    fm=StudentsRegis()

    return render(request,'course/form.html',{'form':fm})

def showformloop(request):
    if request.method == 'POST':
        fm = StudentsRegistration(request.POST)
        if fm.is_valid():
            print('Form validated')
            print('name:',fm.cleaned_data ['name'])
            print('email:',fm.cleaned_data ['email'])
            print('mobile:',fm.cleaned_data ['mobile'])
         
        else:
            fm = StudentsRegistration()
        
        return render(request,'course/form2.html',{'form':fm})

  





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