from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import *

def index(request):
    return render(request, 'index.html')

def list_com1(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list_com1.html', boards)

def list_com2(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list_com2.html', boards)

def list_com3(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list_com3.html', boards)

def post_com1(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('list_com1'))
    else:
        return render(request, 'post_com1.html')

def post_com2(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('list_com2'))
    else:
        return render(request, 'post_com2.html')

def post_com3(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('list_com3'))
    else:
        return render(request, 'post_com3.html')

def detail1(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail1.html', {'board': board})

def detail2(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail2.html', {'board': board})

def detail3(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail3.html', {'board': board})


#@login_required
def comment_write(request):
    errors = []
    if request.method == 'POST':
        board_id = request.POST.get('board_id', '').strip()
        content = request.POST.get('content', '').strip()

        #if not content:
        #    errors.append("댓글을 입력하세요.")
        if not errors:
            sub_board = sub_Board.objects.create(board_id=board_id, content=content)
            return redirect(reverse('post_com1', kwargs={'board_id': sub_board.board_id}))

    return render(request, 'detail1.html', {'errors': errors})


def post_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    is_liked = False

    sub_boards = sub_Board.objects.filter(board=board.id)

    if board.likes.filter(id=request.board_id.id).exists(): # board_id -> user_id로 추후 변경
        is_liked = True

    return render(request, 'detail1.html', context={'board': board, 'sub_boards': sub_boards,
                                                        'is_liked': is_liked, 'total_likes': board.total_likes()})