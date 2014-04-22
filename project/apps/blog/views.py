from vanilla import ListView, DetailView

from .models import Post, Category


class ListPost(ListView):
    model = Post
    template_name = 'blog/post_list.jade'


class DetailPost(DetailView):
    model = Post
    lookup_field = 'slug'
    template_name = 'blog/post_detail.jade'


class ListCategory(ListView):
    model = Category
    template_name = 'blog/category.jade'
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()
