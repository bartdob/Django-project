from django.shortcuts import render
from .models import todoItem
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import DetailView, CreateView, ListView

def todo(request):
    all_todo_items = todoItem.objects.all()

    print(todoItem.objects.all())

    return render(request, 'todo/todo.html',{'all_items': all_todo_items,})

# class TodoListView(ListView):
#     model = todoItem
#     template_name = 'todo.html'
#     context_object_name = 'todo'
#     ordering = ['-date']
#     paginate_by = 4


# class TodoCreateView(LoginRequiredMixin ,CreateView):
#     model = todoItem
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

@login_required
def addTodo(request):
    new = todoItem(content = request.POST['content'])
    new.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_del = todoItem.objects.get(id=todo_id)
    print(item_to_del)
    item_to_del.delete()
    return HttpResponseRedirect('/todo/')

# class TodoDetailView(DetailView):
#     model = todoItem



