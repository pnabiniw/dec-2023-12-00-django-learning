from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    html = """
    <html>
    <head>
        <title>Home</title>
    </head>
    
    <body>
    <h1>Django is Awesome</h1>
    
    </body>
    
    </html>
    
    """
    # return HttpResponse("<h1>Hello I'm learning Django</h1>")
    return HttpResponse(html)


def template_home(request):
    return render(request, template_name="myapp/home.html")
