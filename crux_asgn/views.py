from django.http import HttpResponse
from django.template import loader
from .forms import UploadExcel
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import FileResponse
from django.http import Http404
from .helper import process_media

@csrf_exempt
def landing_page(request):
  template = loader.get_template('landing_page.html')
  return HttpResponse(template.render())

@csrf_exempt
def process_excel(request):
    if request.method == 'POST':
        form = UploadExcel(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            file_path = handle_uploaded_file(uploaded_file)
            print("file_uploaded_successfully at ", file_path)
            process_excel_file(default_storage.path(file_path))
            return render(request, 'success_page.html', {'file_path': file_path , 'uploaded_file_name' : uploaded_file.name})
    else:
        form = UploadExcel()
    return render(request, 'your_template.html', {'form': form})

def handle_uploaded_file(file):
    with default_storage.open(file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file.name

def download_sementic_file(request , file_path, uploaded_file_name):
    file_absolute_path = default_storage.path(file_path)
    try:
        response = FileResponse(open(file_absolute_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file_name}"'
        return response
    except FileNotFoundError:
        raise Http404("File not found")

 
def process_excel_file(name):
    process_media.process_file(name)