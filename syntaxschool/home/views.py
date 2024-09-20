from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def support(request):
    return render(request,'support.html')


def lesson(request):
    return render(request,'lesson.html')