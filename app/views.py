from django.contrib.auth.decorators import login_required
from django.core.signals import request_started
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegisterForm


def note_list(request):
    notes = Note.objects.filter(author = request.user) if request.user.is_authenticated else []
    return render(request, 'app/note_list.html', {'notes':notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id = note_id)
    return render(request, 'app/note_detail.html', {'note':note})


@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        if title and text:
            Note.objects.create(title = title, text = text, author = request.user)
            return redirect('note-list')
    return render(request, 'app/note_create.html')


@api_view(['GET', 'POST'])
def note_list_api(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note-list')
    else:
        form = RegisterForm()
    return render(request, 'app/registration/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('note-list')
        else:
            error_message = 'Неверное имя пользователя или пароль'
            return render(request, 'app/registration/login.html', {'error': error_message})

    return render(request, 'app/registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('note-list')


