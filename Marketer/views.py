from django.shortcuts import render

def index_main(request):
    template_data = {}
    return render(request, 'index_main.html', template_data)
