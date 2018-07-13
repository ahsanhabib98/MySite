from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EmailForm
from django.conf import settings
from blog.models import PostModel

def emailview(request):
    form = EmailForm(request.POST or None)
    post = PostModel.objects.filter(draft=True)
    context = {
    	'form':form,
        'post': post,
    }
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            # from_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message, from_email, ['ahredoan@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    template = "sendmail/email.html"
    return render(request, template, context)

def successview(request):
    return HttpResponse('Success! Thank you for your message.')
# Create your views here.
