'''
Created on 2019.11.17

@author: xcKev
'''
from django.shortcuts import render,render_to_response
from alvin_tool import services
from alvin_tool import restful

def index(request):
    result = services.get_home_index()
    return render_to_response('index.html',result)

def linux(request,api_key):
    if api_key in restful.get_linux_restful():
        return render(request, 'linux/%s.html' %(api_key))
    return render(request, '404.html')

def bash(request,api_key):
    if api_key in restful.get_bash_restful():
        return render(request, 'bash/%s.html' %(api_key))
    return render(request, '404.html')

