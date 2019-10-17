from django.shortcuts import render, redirect
from IPython import embed
from .forms import TodoForm

# Create your views here.
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
    return render(request, 'todos/index.html')

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