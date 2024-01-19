from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    roll_no = models.IntegerField()
    profile_picture = models.FileField(null=True, blank=True,
                                       upload_to='profile_pictures')
