from django.shortcuts import render
from django.contrib.auth.models import Group, User

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from journalApp.models import Entry
from journalApp.serializers import EntrySerializer, UserSerializer, GroupSerializer

# Create your views here.

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-created_date')
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def create_entry(request):
    entry = EntrySerializer(data=request.data)
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]