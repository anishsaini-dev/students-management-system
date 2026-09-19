from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg, Count, Max
from .models import Student
from .forms import StudentForm


def student_list(request):
    """Saare students ki list + search + filter"""
    query = request.GET.get('q', '')
    course = request.GET.get('course', '')

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(email__icontains=query)
        )
    if course:
        students = students.filter(course=course)

    # Statistics
    stats = {
        'total': Student.objects.count(),
        'active': Student.objects.filter(is_active=True).count(),
        'avg_marks': Student.objects.aggregate(Avg('marks'))['marks__avg'] or 0,
        'top_marks': Student.objects.aggregate(Max('marks'))['marks__max'] or 0,
    }

    courses = Student.COURSE_CHOICES

    context = {
        'students': students,
        'query': query,
        'selected_course': course,
        'courses': courses,
        'stats': stats,
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    """Ek student ki poori detail"""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def student_create(request):
    """Naya student add karo"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f"✅ Student '{student.name}' successfully add ho gaya!")
            return redirect('student_list')
        else:
            messages.error(request, "❌ Please form ke errors theek karo.")
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add New Student',
        'button_text': 'Add Student'
    })


def student_update(request, pk):
    """Student ki details update karo"""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"✅ '{student.name}' ki details update ho gayi!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': f'Update Student - {student.name}',
        'button_text': 'Update Student'
    })


def student_delete(request, pk):
    """Student delete karo"""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.success(request, f"🗑️ '{name}' successfully delete ho gaya!")
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})