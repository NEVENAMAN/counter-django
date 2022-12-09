from django.shortcuts import render,redirect

def counter(request):
    count = 0
    request.session['addvisit']= count
    request.session['reset']= count
 
    return render(request,'counter.html',{})
def addvisit(request):
    if request.method == "POST":
     request.session['addvisit'] = request.session['addvisit'] + 2
    return redirect("/show")

def show(request):
    if request.method == "POST":
      request.session['addvisit'] = request.session['addvisit'] + 2
    return render(request,'counter.html')

def reset(request):
    request.session['addvisit'] = 0
    request.session['reset'] = 1
    return redirect('/result')

def reresult(request):
    return render(request,'counter.html')
