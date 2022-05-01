from django.shortcuts import redirect, render

# Create your views here.
def index(req):


    if req.method == "POST":
        city = req.POST['city']
        print(city)
        return redirect('index')

        
    return render(req, 'weather/index.html', {})