from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Artist, Work
from .serializers import WorkSerializer

class WorkList(APIView):
    def get(self, request, format=None):
        works = Work.objects.all()
        artist_name = request.query_params.get('artist', None)
        work_type = request.query_params.get('work_type', None)
        if artist_name:
            artist = get_object_or_404(Artist, name=artist_name)
            works = works.filter(artist=artist)
        if work_type:
            works = works.filter(work_type=work_type)
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

class RegisterUser(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        client = Client.objects.get(user_instance=user)
        return Response({'client_id': client.id})
