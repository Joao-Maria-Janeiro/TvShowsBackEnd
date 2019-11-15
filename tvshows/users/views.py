from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from .models import TvShow, Suggestion
from django.contrib.auth.models import User

# Create your views here.
def get_user(request):
    try:
        token = str(request.META['HTTP_AUTHORIZATION']).split(' ')[1]
        user = User.objects.get(auth_token=token)
        return user
    except:
        return -1


def add_show(request):
    user = get_user(request)
    if(user == -1):
        return HttpResponse("No logged in user")

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    show = TvShow(
        tv_id=body['id'],
        name=body['original_name'],
        backdrop_path=body['backdrop_path'],
        poster_path=body['poster_path'],
        vote_average=body['vote_average']
    )
    show.save()
    user.userprofile.saved_shows.add(show)
    return HttpResponse("Success")

def get_user_list(request):
    user = get_user(request)
    if(user == -1):
        return HttpResponse("No logged in user")
    shows = []
    for show in user.userprofile.saved_shows.all():
        shows.append(
            {
                "id": show.tv_id,
                "original_name": show.name,
                "backdrop_path": show.backdrop_path,
                "poster_path": show.poster_path,
                "vote_average": show.vote_average
            }
        )
    json_data = json.dumps(shows)
    return HttpResponse(json_data, content_type='application/json')

def make_suggestion(request):
    print("\n\n\n\n\n HERE")
    user = get_user(request)
    if(user == -1):
        return HttpResponse("No logged in user")
    print("\n\n\n\n\n HERE 2")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        show = TvShow(
                tv_id=body['id'],
                original_name=body['original_name'],
                backdrop_path=body['backdrop_path'],
                poster_path=body['poster_path'],
                vote_average=body['vote_average']
            )
        show.save()
        suggestion = Suggestion(
            show = show,
            suggested_by = User.objects.get(username=body['username'])
        )
        suggestion.save()
        user.userprofile.suggested_shows.add(suggestion)
        return HttpResponse("Success")
    except Exception as e:
        return HttpResponse("No user with username " + body['username'] + " " + str(e))

def get_suggestions(request):
    user = get_user(request)
    if(user == -1):
        return HttpResponse("No logged in user")
    shows = []
    for show in user.userprofile.suggested_shows.all():
        shows.append(
            {
                "id": show.tv_id,
                "original_name": show.show.name,
                "backdrop_path": show.show.backdrop_path,
                "poster_path": show.show.poster_path,
                "vote_average": show.show.vote_average,
                "suggested_by": show.suggested_by.username
            }
        )
    json_data = json.dumps(shows)
    return HttpResponse(json_data, content_type='application/json')

def integrate_suggestion(request):
    user = get_user(request)
    if(user == -1):
        return HttpResponse("No logged in user")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    suggestion = user.userprofile.suggested_shows.get(show__name = body['name'])
    user.userprofile.saved_shows.add(suggestion.show)
    user.userprofile.suggested_shows.remove(suggestion)
    suggestion.delete()
    return HttpResponse("Success")

def get_user_list_name(request, username):
    try:
        user = User.objects.get(username=username)
        shows = []
        for show in user.userprofile.saved_shows.all():
            shows.append(
                {
                    "id": show.tv_id,
                    "original_name": show.name,
                    "backdrop_path": show.backdrop_path,
                    "poster_path": show.poster_path,
                    "vote_average": show.vote_average
                }
            )
        json_data = json.dumps(shows)
        return HttpResponse(json_data, content_type='application/json')
    except expression:
        return "No user with this username"
    
