from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect

# UPLOAD
def index(request):
    # Handle file upload
    if request.method == 'POST':
        # print('request', request.FILES)
        newdoc = Document(
            docfile=request.FILES['docfile'],
        )
        # save() handles storing of the file to the filesystem automatically
        newdoc.save()
        # Redirect to the documents after POST
        return HttpResponseRedirect('/')
    context = {
        'documents': Document.objects.all()
    }
    return render(request, 'index.html', context)
