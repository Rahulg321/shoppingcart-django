from django.shortcuts import render
from .models import Post


# context -> pass additional info in our template
def home(request):
    context = {}

    # looks for subdir within our templates
    return render(request, 'blog/home.html', context)


def review(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/review.html', context)
