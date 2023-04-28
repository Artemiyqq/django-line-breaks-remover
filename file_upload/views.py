from django.shortcuts import render

from .file_processing import get_text_from_file


def process_file(request):
    if request.method == 'POST':
        text = get_text_from_file(request.FILES['file'],
                                  request.FILES['file'].name)
        print(text)
    return render(request, 'upload_the_file/index.html')
