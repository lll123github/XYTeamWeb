from django.shortcuts import HttpResponse, render

# Create your views here.
def test(request):
    return HttpResponse("Hello, world. You're at the HelloWorld Test.")