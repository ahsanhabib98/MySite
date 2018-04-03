from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Service


# Create your views here.

def service_list(request):
	all_service = Service.objects.all()
	context = {
		'all_service': all_service,
	}
	template = "service/service_list.html"
	return render(request, template, context)


def service_detail(request, id):
	service = get_object_or_404(Service, id = id)
	context = {
		'service':service,
	}
	template = "service/service_detail.html"
	return render(request, template, context)

	

