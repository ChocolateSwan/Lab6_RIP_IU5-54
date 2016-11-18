from django.shortcuts import render
from django.views import View
from lab6_dj.models import *

# Create your views here.

class user_view(View):
    def get (self,request):
        users = user_model.objects.all ()
        return render (request,"users.html", {"users":users})

