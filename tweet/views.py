from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.utils import timezone
from django.views.generic import (ListView,
                                  TemplateView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )


class Home(TemplateView):
    template_name = "tweet/home.html"


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "tweet/post_list.html"
    context_object_name = "posts"
    ordering = ['-posted_at']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "tweet/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.posted_at = timezone.now()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.update_at = timezone.now()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'tweet/post_delete.html'
    success_url = '/post-list/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False
