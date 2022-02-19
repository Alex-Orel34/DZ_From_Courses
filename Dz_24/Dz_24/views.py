from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from NatureImage.froms import NatureImageForm


def index(req):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, req))


def show(req):
    template = loader.get_template('show.html')
    width = req.POST.get('width')
    height = req.POST.get('height')
    context = {'width': width, 'height': height}
    return HttpResponse(template.render(context, req))


def save(req):
    if req.method == 'POST':
        form = NatureImageForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('send')
        else:
            error = 'NON VALID'


def send(req):
    template = loader.get_template('send.html')
    user_email = req.POST.get('email')
    context = {'email': user_email}
    return HttpResponse(template.render(context, req))
