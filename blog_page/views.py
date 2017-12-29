from django.shortcuts import render

def post_list(request):
    return render(request,
                  'blog_page/post_list.html')

