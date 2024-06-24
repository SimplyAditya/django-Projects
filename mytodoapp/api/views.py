from django.shortcuts import render
from django.http import HttpResponse
from api.models import TodoLabel
# from models import TodoLabel
# Create your views here.

def home(request):
    if request.method=="POST":
        title=request.POST.get("newnoteheading")
        description=request.POST.get("newnotedescription")
        print(title,description)
        data=TodoLabel(subject=title,description=description)
        data.save()
    notes=TodoLabel.objects.all()
    data=[]
    for note in notes:
        data.append({
            "heading": note.subject,
            "description":note.description
        })
    context={
        "data": data
    }
    return render(request,"home.html",context)