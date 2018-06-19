from django.shortcuts import render, redirect
from author.models import Author, Subscribe
from author.forms import SubscribeForm
from blog.models import PostModel, PostCategory


def home(request):
	author = Author.objects.all()
	all_blog = PostModel.objects.all()
	post = PostModel.objects.all()[:4]
	r_post = PostModel.objects.all()[:3]
	category = PostCategory.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')

	context = {
		'author': author,
		'all_blog': all_blog,
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = 'home.html'
	return render(request, template, context)

def about(request):
	post = PostModel.objects.all()[:4]
	r_post = PostModel.objects.all()[:3]
	category = PostCategory.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')

	context = {
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = 'about.html'
	return render(request, template, context)
