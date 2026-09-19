from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('BSc', 'BSc'),
        ('MSc', 'MSc'),
    ]

    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    admission_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    Descripstion = models.TextField(default="")

    class Meta:
        ordering = ['roll_no']

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

    @property
    def grade(self):
        """Marks ke hisaab se grade return karega"""
        m = float(self.marks)
        if m >= 90: return "A+"
        elif m >= 80: return "A"
        elif m >= 70: return "B"
        elif m >= 60: return "C"
        elif m >= 50: return "D"
        else: return "F"

        