from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from myblog.models import blogPost
from django.urls import reverse_lazy
from .forms import QuillFieldForm

def form_view(request):
    return render(request, 'form_view.html', {'form': QuillFieldForm()})

class HomeView(ListView):
    model = blogPost
    template_name = 'home.html'
    ordering = ['-id']

class ArtDetView(DetailView):
    model = blogPost
    template_name = 'art_det.html'

class PushView(CreateView):
    model = blogPost
    template_name = 'host.html'
    fields = '__all__'

class UpPostView(UpdateView):
    model = blogPost
    template_name = 'editpost.html'
    fields = ['title','titletag','content']

class DelView(DeleteView):
    model = blogPost
    template_name = "delete.html"
    success_url = reverse_lazy('home')