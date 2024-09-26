from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Welcome</h1>')

def about(request):
    return HttpResponse('<h1>Hello</h1>')
