from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from .models import Todo


# Create your views here.
@login_required
def index(request):
    # session에 id랑 저장되어있음(딕셔너리 정보)
    # visit_num이 없으면 0이 출력
    # 데이터를 가져오는 것
    # visit_num = request.session.get('visit_num', 0)
    
    # # 1씩 늘려서 보여줌
    # request.session['visit_num'] = visit_num + 1
    
    # request.session.modified = True

    # context = {
    #     'visit_num': visit_num,
    # }

    #지금 로그인한 사람이 작성한 todo만 보여야함
    todos = request.user.todo_set.all().order_by('-due_date')
    context = {
        'todos':todos,
    }

    
    return render(request, 'todos/index.html', context)


@login_required
def create(request):
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            # todo에 비어있는 정보가 user
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context ={
        'form': form,
    }
    return render(request, 'todos/form.html', context)


@login_required
def delete(request, id):
    todo = get_object_or_404.get(Todo, id=id)
    if todo.user == request.user:
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:index')