from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import PostModel


# Create your views here.

def blog_list(request):
	all_blog = PostModel.objects.all()
	context = {
		'all_blog': all_blog,
	}
	template = "blog/blog_list.html"
	return render(request, template, context)


def blog_detail(request, id):
	blog = get_object_or_404(PostModel, id = id)
	context = {
		'blog':blog,
	}
	template = "blog/blog_detail.html"
	return render(request, template, context)

	

