from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
from django.shortcuts import redirect
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
import os
import threading


def some_script(_file_path):
    _another_file_path = _file_path
    return _another_file_path


def files_list(request):
    documents = Document.objects.all()
    return render(request, 'transformer/files_list.html', {'documents': documents})


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
    # path = "/".join(settings.MEDIA_ROOT.split("/")[:-1])
    # documents = Document.objects.all()
    document = Document.objects.get(pk=pk)

    file_name = document.document.url.split("/")[-1]
    file_name_without_ext = "".join(str(file_name).split(".")[:-1])

    storage = settings.MEDIA_ROOT + "/videos/"

    config_file_destination = "/".join(str(storage).split("/")[:-2]) + "/configs/"
    flag = 'a'
    if os.path.exists(config_file_destination + file_name_without_ext):
        flag = 'w'
    with open(config_file_destination + file_name_without_ext, flag) as f:
        f.truncate()
        f.write("start=" + str(document.config_start) + "\n")
        f.write("stop=" + str(document.config_end) + "\n")
        f.write("num_machines=" + str(document.num_machines))

    destination = "/".join(str(storage).split("/")[:-2]) + "/output"
    destination_name = destination + "/" + file_name_without_ext + "_mask.csv"
    try:
        threading.Thread(target=run_script, args=(document, destination_name, file_name)).start()
    except:
        pass
    return redirect('files_list')
    # return render(request, 'transformer/files_list.html', {'documents': documents, 'path': path})


def download_file(request, pk):
    document = Document.objects.get(pk=pk)
    file_path = document.result_url
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def run_script(document: Document, destination_name: str, file_name: str) -> None:
    video_file_extensions = ["avi", "mkv", "flv", "m4v", "mpeg"]
    if file_name.split(".")[-1] not in video_file_extensions:
        print("Wrong file format")
        return
    if os.path.exists(destination_name):
        print("Already processed")
        return
    os.putenv("DATA", settings.MEDIA_ROOT)
    os.system("bash ~/tracker_docker/predict Mask_RCNN " + file_name)
    if os.path.exists(destination_name):
        document.processed = True
        document.result_url = destination_name
    document.save()
