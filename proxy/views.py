from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import Http404, HttpResponse

import requests


@csrf_exempt
def reverse_proxy(request, url):
    requestor = getattr(requests, request.method.lower())
    
    proxied_response = requestor(url, data=request.body, files=request.FILES)
    
    response = HttpResponse(proxied_response.content, content_type=proxied_response.headers.get('content-type'))
    for header_key, header_value in proxied_response.headers.items():
        response.headers[header_key] = header_value
    
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Vary"] = "Origin"

    return response