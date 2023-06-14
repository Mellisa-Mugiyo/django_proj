

from django.shortcuts import render

def home(request):
    """Constructor method, This method will be used to ask request 
   for the  html page

   :param request: request objects are used  to pass state through the system
   since the html page has been requested, Django creates an HttpRequest object that
    contains metadata about the request

    :returns: It renders the html page(home.html)
    :rtype: html pages

"""
    return render(request,'home.html')


def information(request):
    """Constructor method, This method will be used to ask request 
   for the  html page

   :param request: request objects are used  to pass state through the system
   since the html page has been requested, Django creates an HttpRequest object that
    contains metadata about the request

    :returns: It renders the html page(information.html)
    :rtype: html pages

"""
    return render(request,'information.html',{})

def contact(request):
    """Constructor method, This method will be used to ask request 
   for the  html pages

   :param request: request objects are used  to pass state through the system
   since the html page has been requested, Django creates an HttpRequest object that
    contains metadata about the request

    :returns: It renders the html page(contact.html)
    :rtype: html pages

"""
    return render(request,'contact.html',{})



