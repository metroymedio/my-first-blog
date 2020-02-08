from django.shortcuts import render

# Createdef post_list(request):
def post_list(request):
    return render(request, 'blog/post_list.html', {})
