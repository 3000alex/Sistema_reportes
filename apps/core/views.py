from django.shortcuts import render
 
# Create your views here.
def error(request, *args, **argv):
    return render(request, 'core/error.html', status=404)