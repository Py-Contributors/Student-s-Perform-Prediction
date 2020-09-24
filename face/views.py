import sys
import warnings
import numpy as np
import joblib
if not sys.warnoptions:
    warnings.simplefilter("ignore")

from django.shortcuts import render
#loading model
with open("model/model.pkl", "rb") as file:
    model = joblib.load(file)
# Create your views here.
def indexView(request):
    return render(request, "face/index.html")

def predictionView(request):
    if request.method == "POST":
        gender = request.POST["gender"]
        age = request.POST["age"]
        location = request.POST["location"]
        famsize = request.POST["famsize"]
        traveltime = request.POST["traveltime"]
        studytime = request.POST["studytime"]
        failures = request.POST["failures"]
        paid = request.POST["paid"]
        activities = request.POST["activities"]
        nursery = request.POST["nursery"]
        higher = request.POST["higher"]
        internet = request.POST["internet"]
        freetime = request.POST["freetime"]
        health = request.POST["health"]

        
        data = np.array([ gender, age, location, famsize, traveltime, studytime, failures, 
                            paid, activities, nursery, higher, internet,freetime, health]).reshape(-1,14)
        result = model.predict(data)[0]
        print(result) #debug
        context = {"result" : result}
        return render(request, "face/result.html", context)
    return render(request, "face/prediction.html")
