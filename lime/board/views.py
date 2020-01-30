from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import (DetailView, ListView,
                                  CreateView, DeleteView,
                                  UpdateView)
#  Methods allowed
#  forms

#  Models
from .models import Board, Task
# Create your views here.

class BoardDetailView(DetailView):
    model = Board
    template_name = 'board_detail.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = Task.objects.filter(status='TD', board=self.object)
        context['in_progress_list'] = Task.objects.filter(status='PR', board=self.object)
        context['done_list'] = Task.objects.filter(status='DN', board=self.object)
        return context


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'text']
    http_method_names = ['post', 'get']
    template_name = 'task_edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('board:board_detail', kwargs={'pk': self.object.board.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('board:board_detail', kwargs={'pk': self.object.board.id})


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'text']
    template_name = 'task_create.html'

    def form_valid(self, form):
        form.instance.board = Board.objects.get(pk=self.kwargs['board_pk'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('board:board_detail', kwargs={'pk': self.object.board.id})


class TaskMoveView(UpdateView):
    model = Task
    fields = ['status']
    http_method_names = ['post', 'get']
    template_name = 'task_edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('board:board_detail', kwargs={'pk': self.object.board.id})
