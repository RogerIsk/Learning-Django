from django.shortcuts import render

def posts_lists(request):
    return render(request, 'posts/posts_list.html')
