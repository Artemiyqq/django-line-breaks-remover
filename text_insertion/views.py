from django.shortcuts import render


def get_the_text(request):
    if request.method == 'POST':
        pass
    return render(request, 'paste_the_text/index.html')
