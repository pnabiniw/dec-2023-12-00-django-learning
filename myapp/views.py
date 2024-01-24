from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def root_page(request):
    return render(request, template_name="myapp/root_page.html")


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


def portfolio(request):
    return render(request, template_name="myapp/index.html")
