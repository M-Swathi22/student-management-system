from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .models import Admin
from .forms import StudentForm
from django.db.models import Q
from django.contrib import messages

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

def student_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')

        try:
            student = Student.objects.get(name=name, dob=dob)
            return redirect('view_students')  # Redirect after successful login
        except Student.DoesNotExist:
            return render(request, 'student_login.html', {'error': 'Invalid Name or Date of Birth'})
    return render(request, 'student_login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin_user = Admin.objects.get(username=username, password=password)
            request.session['admin_username'] = admin_user.username  # session start
            messages.success(request, 'Login Successful!')
            return redirect('admin_dashboard')  # redirect to admin dashboard page
        except Admin.DoesNotExist:
            messages.error(request, 'Invalid Username or Password')
            return redirect('admin_login')
    return render(request, 'admin_login.html')

def admin_dashboard(request):
    if 'admin_username' not in request.session:
        return redirect('admin_login')
    return render(request, 'admin_dashboard.html')

def admin_logout(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully!')
    return redirect('admin_login')

# Create your views here.
