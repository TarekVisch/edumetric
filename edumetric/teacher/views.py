from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse


# Create your views here.

@login_required
def tacher_home(request):
    return HttpResponse(f"<p>Hello Teacher: {request.user.first_name}</p>")
