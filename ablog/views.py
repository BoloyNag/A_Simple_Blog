from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . models import Post,Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy 
#from django.contrib import messages

#def home(request):
#	return render(request,'home.html',{})
class home_view(ListView):
	model=Post
	template_name='home.html'
	ordering=['-post_date']
	#ordering=['-id']

class post_detail_view(DetailView):
	model=Post
	template_name='post.html'

class add_post_view(CreateView):
	model=Post
	form_class=PostForm
	template_name='add_post.html'
	#fields='__all__'

class add_category_view(CreateView):
	model=Category
	#form_class=PostForm
	template_name='add_category.html'
	fields='__all__'

class update_post_view(UpdateView):
	model=Post
	form_class=EditForm
	template_name='update_posts.html'
	#fields=['title','title_tag','body']

class delete_post_view(DeleteView):
	model=Post
	template_name='delete_posts.html'
	success_url=reverse_lazy('home')

	

