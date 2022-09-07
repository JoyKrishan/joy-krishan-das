from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

user_info = {
    'name': 'Joy Krishan Das'
}

def index(request):
    return render(request, 'myblog/index.html', user_info)