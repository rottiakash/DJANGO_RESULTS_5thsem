from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student,Marks
from .serializers import StudentSerializer, MarksSerializer
# Create your views here.


class GetAll(APIView):
    def get(self, request):
        results = Student.objects.all()
        serial = StudentSerializer(results, many=True)
        return Response(serial.data)

    def post(self):
        pass


class GetUsn(APIView):
    def get(self, request):
        usn = self.request.query_params.get('usn')
        results = Student.objects.filter(usn=usn)
        serial = StudentSerializer(results, many=True)
        return Response(serial.data)

    def post(self):
        pass