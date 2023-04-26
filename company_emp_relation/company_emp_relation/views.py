from django.http import HttpResponse
def homepage(request):
    print("home page  requested")
    return HttpResponse("this is home page")