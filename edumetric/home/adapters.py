from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        if request.user.role == "student":
            return "/student"
        if request.user.role == "teacher":
            return "/teacher"

    def get_signup_redirect_url(self, request):
        if request.user.role == "student":
            return "/student"
        if request.user.role == "teacher":
            return "/teacher"
