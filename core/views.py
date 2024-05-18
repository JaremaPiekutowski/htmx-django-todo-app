from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST

from core.forms import TodoForm
from core.models import Todo


@login_required
def index(request):
    context = {
        'todos': Todo.objects.filter(user=request.user),
        'form': TodoForm()
        }
    return render(
        request=request,
        template_name="index.html",
        context=context
        )


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
    return index(request)
