from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def hello(request):
	return HttpResponse("Hello, World!")

def me(request, name, group, role):
	t = get_template('index.html')
	context = Context({'first':name,
				'second' : group,
				'third' : role,})
	html = t.render(context)
	return HttpResponse(html, content_type = 'text/html;charset=UTF-8')
