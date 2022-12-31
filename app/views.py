from django.shortcuts import render
from .models import ProjectModel

def update_like_dislike(request):

    likes = ProjectModel.objects.get().like
    dislikes = ProjectModel.objects.get().dislike

    print(likes)
    print(dislikes)


    context = {'like':likes , 'dislike' : dislikes}

    return render(request , 'templates/home.html' , context)
