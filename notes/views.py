from django.shortcuts import render, redirect
from .models import Note, Tag

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

# username: ila
# email: ilachafin
# password: nesquece

def index(request):  
    all_tags = Tag.objects.all() 
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        if tag == '':
            Note.objects.create(title=title, content=content)
        else:
            Note.objects.create(title=title, content=content, tag=tag)
            all_tags = Tag.objects.all()
            test_tag = Tag(title=tag)
            title_list = []
            for tagg in all_tags:
                title_list.append(tagg.title)
            if test_tag.title not in title_list:
                Tag.objects.create(title=tag)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})    
    
def delete(request, id):
    nota = Note.objects.get(id=id)
    tag = Tag.objects.get(title=nota.tag)
    nota.delete()
    notas = Note.objects.filter(tag=tag.title)
    qntd_notas = len(notas)
    if qntd_notas == 0:
        tag.delete()
    return redirect('index')

def edit(request, id):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        Note.objects.filter(id=id).update(title=title, content=content)
        return redirect('index')
    else:
        nota = Note.objects.filter(id=id).values()[0]
        return render(request, 'notes/edit.html', {'title': nota['title'], 'content': nota['content']})
    
def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})    

def tag(request, title):
    tag = Tag.objects.get(title=title)
    notas = Note.objects.filter(tag=tag.title)
    return render(request, 'notes/tag_especifica.html', {'tag':tag, 'notas': notas})

def delete_pag_tag(request, id):
    nota = Note.objects.get(id=id)
    nome_tag = nota.tag
    tag = Tag.objects.get(title=nome_tag)
    nota.delete()
    notas = Note.objects.filter(tag=tag.title)
    qntd_notas = len(notas)
    if qntd_notas == 0:
        tag.delete()
    return redirect('index')
    # else:
    #     return render(request, 'notes/tag_especifica.html', {'tag': tag, 'notas': notas})
    
def edit_pag_tag(request, id):
    nota = Note.objects.get(id=id)
    tag = Tag.objects.get(title=nota.tag)
    notas = Note.objects.filter(tag=nota.tag)
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        Note.objects.filter(id=id).update(title=title, content=content)
        # return render(request, 'notes/tag_especifica.html', {'tag':tag, 'notas': notas})
        return redirect('index')
    else:
        nota = Note.objects.filter(id=id).values()[0]
        return render(request, 'notes/edit.html', {'title': nota['title'], 'content': nota['content']})

def delete_tag(request, title):
    tag = Tag.objects.get(title=title)
    notas = Note.objects.filter(tag=tag.title)
    for nota in notas:
        nota.delete()
    tag.delete()
    tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': tags})

# post do update
@api_view(['GET', 'POST', 'DELETE'])
def api_update_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        raise Http404()
    
    if request.method == 'POST':
        new_note_data = request.data
        note.title = new_note_data['title']
        note.content = new_note_data['content']
        note.save()

    if request.method == 'DELETE':
        note.delete(note_id)
        return Response(204)

    serialized_note = NoteSerializer(note)
    return Response(serialized_note.data)

# post de criar nova nota
@api_view(['GET', 'POST'])
def api_create_note(request):
    
    if request.method == 'POST':
        new_note_data = request.data
        title = new_note_data['title']
        content = new_note_data['content']
        Note.objects.create(title=title, content=content)

    notas = Note.objects.all()
    serialized_notes = NoteSerializer(notas, many=True)
    return Response(serialized_notes.data)