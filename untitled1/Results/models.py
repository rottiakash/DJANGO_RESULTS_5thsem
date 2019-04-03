from django.db import models

# Create your models here.
class Student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.usn+"-"+self.name

class Marks(models.Model):
    usn = models.ForeignKey(Student, related_name='marks', on_delete=models.CASCADE)
    sub_code = models.CharField(max_length=10)
    internal = models.IntegerField()
    external = models.IntegerField()
    total = models.IntegerField()
    result = models.CharField(max_length=1)