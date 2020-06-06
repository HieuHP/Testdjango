from django.shortcuts import render, get_object_or_404
from blog1.models import Post, Comment
from blog1.forms import CommentForm
from django.http import HttpResponseRedirect
#from .models import Post
#from django.views.generic import ListView, DetailView
# Create your views here.
def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'blog/post.html', {"post":post, "form":form})
#def list(request):
#    Data = {'Posts': Post.objects.all().order_by("-date")}
#    return render(request, 'blog/blog.html', Data)
# //
#class PostListView(ListView): chuyển trực tiếp qua urls
#    queryset = Post.objects.all().order_by("-date")
#    template_name = 'blog/blog.html'
#    context_object_name = 'Posts'
#    paginate_by = 1 #mỗi trang không quá 1 bài viết(tiếp theo(blog.html))

#def post(request, id):
#    post = Post.objects.get(id=id)
#    return render(request, 'blog/post.html', {'post': post})
# //
#class PostDetailView(DetailView): chuyển trực tiếp qua urls
#    model = Post
#    template_name = 'blog/post.html'
