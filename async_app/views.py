from django.shortcuts import render
from django.http import JsonResponse
from time import sleep

def index(request):
    json_payload = {
        "message": "Hello world!"
    }
    #sleep(10)
    async_task("async_app.services.sleep_and_print", 10)
    return JsonResponse(json_payload)
