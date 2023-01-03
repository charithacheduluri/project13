from django.shortcuts import render

# Create your views here.
def operation(request):
    d={'a':23,'b':53}
    return render(request,'operation.html',d)
