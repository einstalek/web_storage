from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Document
from .forms import DocumentForm
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
import os

def some_script(_file_path):
	_another_file_path = _file_path
	return _another_file_path

def files_list(request):
	documents = Document.objects.all()
	return render(request, 'transformer/files_list.html', {'documents':documents})

def upload_new_file(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('files_list')
	else:
		form = DocumentForm()
	return render(request, 'transformer/upload_new_file.html', {'form': form})
	
def run_on_file(request, pk):
	path = "/".join(settings.MEDIA_ROOT.split("/")[:-1])
	documents = Document.objects.all()
	document = Document.objects.get(pk=pk)
	
	_another_file_path = some_script(document.document.url)
	
	document.processed = True
	document.result_url = path + _another_file_path
	document.save()
	return render(request, 'transformer/files_list.html', {'documents':documents, 'path': path})
	
def download_file(request, pk):
    root = "/".join(settings.MEDIA_ROOT.split("/")[:-1])
    file_path = root + Document.objects.get(pk=pk).document.url
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
	

