from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.db.models import Q

def home_page(request):
    return render(request, 'home.html')

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
    query = request.GET.get('q')
    sort_by = request.GET.get('sort')
    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) | Q(course__icontains=query)
        )

    if sort_by:
        students = students.order_by(sort_by)

    return render(request, 'view_students.html', {'students': students, 'query': query, 'sort_by': sort_by})

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
