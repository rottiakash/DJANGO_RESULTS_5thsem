from rest_framework import serializers
from .models import Student,Marks

class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ('sub_code', 'internal', 'external', 'total', 'result')

class StudentSerializer(serializers.ModelSerializer):
    marks = MarksSerializer(many=True)
    class Meta:
        model = Student
        fields = ('usn', 'name', 'marks')