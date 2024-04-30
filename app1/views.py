from django.shortcuts import render

# Create your views here.
def app1_test(request):
    return render(request,'app1_test.html')
def app1_test2(request):
    return render(request,'app1_test2.html')
