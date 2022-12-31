from django.shortcuts import render
from .models import ProjectModel

def update_like_dislike(request):

    data = ProjectModel.objects.first()
    likes = data.like
    dislikes = data.dislike


    if request.POST.get('like_button'):
        likes += 1
    
    if request.POST.get('dislike_button'):
        dislikes += 1

    data.like = likes
    data.dislike= dislikes

    data.save()
    

    print(likes)
    print(dislikes)


    context = {'like':likes , 'dislike' : dislikes}

    return render(request , 'templates/home.html' , context)
