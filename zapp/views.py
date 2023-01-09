from django.shortcuts import render
from .models import Api
from rest_framework import generics
from .serializers import ApiSerializer

# Create your views here.
def this(request):
    details = Api.objects.all()[:20]
    return render (request,'home.html',{'details':details})

class ApiList(generics.ListAPIView):
    queryset = Api.objects.order_by('-created_at').all()
    serializer_class = ApiSerializer