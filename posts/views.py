from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class PostList(ListView) : 
	model = Post
	ordering = '-pk'



class PostDetail(DetailView) :  
    model = Post


<<<<<<< HEAD
class PostCreate(CreateView, LoginRequiredMixin, UserPassesTestMixin) :
	model = Post
	fields = ['title', 'content', 'author']
	
	def form_valid(self, form) : # 장고 제공 함수
		current_user = self.request.user
		if current_user.is_authenticated :
			form.instance.author = current_user
			return super(PostCreate, self).form_valid(form)
		else :
			return redirect('/posts/')


class PostUpdate(UpdateView, LoginRequiredMixin):
	model = Post
	fields = ['title', 'content', 'author']
	template_name = 'posts/post_update_form.html'  # 템플릿 이름 별도로 설정해야

	def dispatch(self, request, *args, **kwargs) : # 로그인했고, 작성자인 경우에만 가능하도록
		if request.user.is_authenticated and request.user == self.get_object().author :
			return super(PostUpdate, self).dispatch(request, *args, **kwargs)
		else :
			raise PermissionDenied # 예외 발생
	
	
=======
>>>>>>> 6dce91ecb4446d8b2594226e8c03fce84d43c8b7
