from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import Group, User

from rest_framework import viewsets, permissions

from journalApp.forms import JournalEntryForm
from journalApp.models import Entry
from journalApp.serializers import EntrySerializer, UserSerializer, GroupSerializer

# Create your views here.

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-created_date')
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

def entry_list(request):
    entries = Entry.objects.all().order_by('-created_date')
    return render(request, 'entries/list.html', {'entries': entries})

def entry_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            return redirect('entry_detail', entry.id)
    else:
        form = JournalEntryForm()
    return render(request, 'entries/form.html', {'form': form})

def entry_detail(request, pk):
    """View details of a specific entry"""
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entries/detail.html', {'entry': entry})

def entry_update(request, pk):
    """Update an existing entry"""
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=entry.id)
    else:
        form = JournalEntryForm(instance=entry)
    return render(request, 'entries/form.html', {'form': form, 'entry': entry})

def entry_delete(request, pk):
    """Delete an entry"""
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'entries/confirm_delete.html', {'entry': entry})
    

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