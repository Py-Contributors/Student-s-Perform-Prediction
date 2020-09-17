from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, "face/index.html")

def predictionView(request):
    return render(request, "face/prediction.html")

def resultView(request):
    return render(request, "face/result.html")