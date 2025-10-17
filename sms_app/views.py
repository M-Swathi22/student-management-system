from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('view_students')
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    return render(request, 'delete_student.html', {'student': student})


# Create your views here.
