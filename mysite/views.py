from django.shortcuts import render, redirect
from author.models import Author, Subscribe
from author.forms import SubscribeForm
from blog.models import PostModel, PostCategory


def home(request):
	author = Author.objects.all()
	post = PostModel.objects.all()
	category = PostCategory.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')

	context = {
		'author': author,
		'post': post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = 'home.html'
	return render(request, template, context)

def about(request):
	author = Author.objects.all()
	post = PostModel.objects.all()
	category = PostCategory.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')
	
	context = {
		'author': author,
		'post': post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = 'about.html'
	return render(request, template, context)
