from django.shortcuts import render
from course.models import Student
from . forms import  StudentsRegistration

    
def studentInfo(request):
    stud = Student.objects.all()
    return render(request,'course/course.html', {'stu':stud})

def showformloop(request):
    if request.method == 'POST':
        fm = StudentsRegistration(request.POST)
        if fm.is_valid():
            print('Form validated')
            print('name:',fm.cleaned_data ['name'])
            print('email:',fm.cleaned_data ['email'])
            fm = StudentsRegistration()
    else:
        fm = StudentsRegistration() #form for GET request
        
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