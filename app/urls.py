from django.urls import path
from . import views
app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("adopt/",views.adopt,name="adopt"),
    path("<int:animal_id>/", views.animalDetails, name="animalDetails"),
    path("<int:animal_id>/request/new/", views.new_request, name="new_request"),
    path('addAnimal/', views.addAnimal, name="addAnimal"),
    path('addBreed/',views.addBreed,name='addBreed'),
    path("request",views.requests,name="requests"),
    path('archive',views.archive,name="archive"),
    path("<int:req_id>/request/decision/",views.request_decision,name="request_decision"),
    path("searchAnimals/",views.searchBreeds,name="searchAnimals"),
    path("<int:user_id>/profile/",views.profile,name="profile")
]