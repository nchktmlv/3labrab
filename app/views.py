from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def mycookie(request):
    playlist = request.POST.get('track_name','')
    cookie_playlist = request.COOKIES.get('playlist')
    print(cookie_playlist)
    if playlist != '':
        response = render(request, 'index.html')
        response.set_cookie('playlist', playlist, 24*7*60*60)
        return response

    return render (request, 'index.html', {'playlist':cookie_playlist})

