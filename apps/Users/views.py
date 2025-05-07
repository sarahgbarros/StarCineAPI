from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Type

class SaveUser(APIView):

    def get_user(self, request, username, password):
        if request.method == 'GET':
            user = User.objects.filter(username=username, password=password).get()
            return user
        else:
            return {"Not found"}
        
    def create_user(self, request, username, password, type, email, name, photo, created_at):
        if request.method == 'GET':
            if not self.get_user(username=username, password=password):
                pass

