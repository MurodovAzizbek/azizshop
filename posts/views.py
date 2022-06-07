from django.views.generic import ListView, DetailView

from posts.models import PostModel


class PostsListView(ListView):
    queryset = PostModel.objects.order_by('-pk')
    template_name = 'blog.html'
    paginate_by = 3

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')

        if tag:
            qs = qs.filter(tags__title=tag)

        return qs


class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel
