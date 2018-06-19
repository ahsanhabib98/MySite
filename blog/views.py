from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import PostModel, PostCategory
from .forms import PostModelForm
from author.models import Author, Subscribe
from author.forms import SubscribeForm


# Create your views here.

def blog_list(request):
	author = Author.objects.all()
	post = PostModel.objects.all()[:4]
	r_post = PostModel.objects.all()[:3]
	category = PostCategory.objects.all()
	all_blog = PostModel.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')

	context = {
		'all_blog': all_blog,
		'author': author,
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = "blog/blog_list.html"
	return render(request, template, context)


def blog_create(request):
	forms = PostModelForm(request.POST or None)
	author = Author.objects.all()
	post = PostModel.objects.all()[:4]
	r_post = PostModel.objects.all()[:3]
	category = PostCategory.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')

	if forms.is_valid():
		obj = forms.save(commit=False)
		obj.save()
		return HttpResponse('Success')

	context = {
		'author': author,
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
		'forms': forms,
	}
	template = 'blog/blog_create.html'
	return render(request, template, context)


def blog_detail(request, id):
	author = Author.objects.all()
	post = PostModel.objects.all()[:4]
	r_post = PostModel.objects.all()[:3]
	category = PostCategory.objects.all()
	blog = get_object_or_404(PostModel, id = id)

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')


	context = {
		'blog': blog,
		'author': author,
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = "blog/blog_detail.html"
	return render(request, template, context)

def category(request):
	author = Author.objects.all()
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
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = 'blog/category.html'
	return render(request, template, context)

def categorywise_blog(request, id):
	all_blog = PostModel.objects.filter(category__id = id)
	author = Author.objects.all()
	post = PostModel.objects.all()[:4]
	r_post = PostModel.objects.all()[:3]
	category = PostCategory.objects.all()

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			obj = form.save()
			return redirect('home')

	context = {
		'all_blog': all_blog,
		'author': author,
		'post': post,
		'r_post': r_post,
		'category': category,
		'form': SubscribeForm(),
	}
	template = "blog/categorywise_blog.html"
	return render(request, template, context)
