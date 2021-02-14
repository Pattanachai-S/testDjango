from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Pattanachai, how are u?. You're at the polls index.")
    
def index2(request):
    return HttpResponse("Hello .")
