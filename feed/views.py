from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from feed.models import Post
from feed.forms import PostForm
from django.views.generic import ListView,CreateView,DetailView,TemplateView
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from django.http import HttpResponse

# Create your views here.
class PostListView(ListView):
    context_object_name = 'post_list'
    model = Post
    # - with published_date means descending order
    def get_queryset(self):
        return Post.objects.filter(event_date__gte=timezone.now()).order_by('event_date')

class PostDetailView(DetailView):
        model = Post

class CreatePostView(CreateView):
        redirect_field_name = 'feed/post_detail.html'
        form_class = PostForm
        model = Post

class Notes(TemplateView):
    template_name = 'feed/notes.html'

class MapView(TemplateView):
    template_name = 'feed/map.html'

def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('feed/post_detail',pk=pk)

######### API ###############

class PostList(APIView):

     def get(self,request):
         posts = Post.objects.all()
         serializer = PostSerializer(posts,many=True)
         return Response(serializer.data)
