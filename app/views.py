from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from rest_framework.decorators import api_view

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'app/note_list.html', {'notes':notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id = note_id)
    return render(request, 'app/note_detail.html', {'note':note})

# def note_create(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         text = request.POST.get('text')
#
#         if title and text:
#             Note.objects.create(title = title, text = text)
#             return redirect('note-list')
#         else:
#             return HttpResponse("Все поля обязательны", status=400)
#     return render(request, 'app/note_create.html')


def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')

        # Проверяем, что оба поля заполнены
        if not title or not text:
            return render(request, 'app/note_create.html', {'error_message': 'Оба поля (Заголовок и Текст) обязательны!'})

        # Создаём заметку
        Note.objects.create(title=title, text = text)
        return redirect('note-list')  # Перенаправляем на список заметок

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