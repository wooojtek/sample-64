from vanilla import ListView, DetailView

from .models import Post


class ListPost(ListView):
    model = Post
    template_name = 'blog/post_list.jade'


class DetailPost(DetailView):
    model = Post
    lookup_field = 'slug'
    template_name = 'blog/post_detail.jade'