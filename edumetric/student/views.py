from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponse

# Create your views here.


def role_check(user):
    return user.role == 'student'


@login_required()
@user_passes_test(role_check, login_url="/")
def student_home(request):
    return HttpResponse(f"<p>{request.user.first_name}</p>")
