from django.shortcuts import render
from django.http import HttpResponse
import requests
def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    return render(request,'index.html',{'users':users})

