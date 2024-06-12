from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from app.models import Animal,AnimalType,AdoptingRequest
from django.urls import reverse
from app.forms import AnimalForm,AnimalTypeForm

def base(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "app/base.html", context)

def	index (request):
    user=request.user
    context={
        "user":user
    }
    return render(request, "app/index.html", context)
def adopt (request):
    user=request.user
    cats = Animal.objects.filter(type__type=AnimalType.CAT)
    dogs= Animal.objects.filter(type__type=AnimalType.DOG)
    context={
        "user":user,
        "dogs": dogs,
        "cats":cats
    }
    return render(request, "app/adopt.html", context)

def animalDetails(request,animal_id):
    animal=party = get_object_or_404(Animal, pk=animal_id)
    user=request.user
    if user.is_authenticated:
        animal_request = AdoptingRequest.objects.filter(
            user_id=user, animal_id=animal_id
        ).first()
    else:
        animal_request=None
    context ={
        "animal":animal,
        "request":animal_request
    }
    return render(request, "app/animalDetails.html", context)

def new_request(request,animal_id):
    animal=get_object_or_404(Animal,pk =animal_id)
    if request.method == "POST" and request.user.is_authenticated:
        text = request.POST.get("text")
        adoptingReq = AdoptingRequest(
            animal_id=animal,
            user_id=request.user,
            status=AdoptingRequest.PENDING,
            description=text,
        )
        adoptingReq.save()
    return HttpResponseRedirect(reverse("app:animalDetails", args=(animal_id,)))

def requests(request):
    pending_requests=AdoptingRequest.objects.filter(status=AdoptingRequest.PENDING)
    context={
        "pending":pending_requests,

    }
    return render(request, "app/requests.html", context)
def archive(request):
    approved_requests=AdoptingRequest.objects.filter(status=AdoptingRequest.APPROVED)
    declined_requests=AdoptingRequest.objects.filter(status=AdoptingRequest.DECLINED)
    context={
        "approved":approved_requests,
        "declined":declined_requests,
    }
    return render(request, "app/archive.html", context)

def request_decision(request,req_id):
    req = get_object_or_404(AdoptingRequest, pk=req_id)
    animal_id = req.animal_id
    if request.method == "POST" and request.user.is_authenticated:
        inputvalue = request.POST.get("decision", None)
        if inputvalue == "APPROVE":
            req.status = AdoptingRequest.APPROVED
            animal_id.is_adopted=True
            animal_id.save()
        else:
            req.status = AdoptingRequest.DECLINED
        req.save()
    return HttpResponseRedirect(reverse("app:requests", args=()))


def addAnimal(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = AnimalForm(request.POST)
        if form.is_valid():
            saved_animal = form.save(commit=False)
            saved_animal.is_adopted=False
            saved_animal.save()
            return HttpResponseRedirect(reverse("app:index"))
    else:
        form = AnimalForm()
    context = {
        "form": form,
    }
    return render(request, "app/add.html", context)

def addBreed(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = AnimalTypeForm(request.POST)
        if form.is_valid():
            saved_animal = form.save(commit=False)
            saved_animal.is_adopted=False
            saved_animal.save()
            return HttpResponseRedirect(reverse("app:index"))
    else:
        form = AnimalTypeForm()
    context = {
        "form": form,
    }
    return render(request, "app/add.html", context)