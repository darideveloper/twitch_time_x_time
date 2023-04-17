import django
from . import models
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from app.twitch import TwitchApi

def get_json_model (model:django.db.models) -> str:
    """ Serializes a model to json

    Args:
        model (django.db.models): model to serialize

    Returns:
        str: json data
    """
    
    # Get all objects from table
    objects = model.objects.all()
    
    # Format objects to json
    objects_json = serializers.serialize('json', objects)
    
    return objects_json

def get_settings (request):
    """ Returns all settings in json format """        
    return HttpResponse(get_json_model(models.Setting), content_type='application/json')

def get_proxies (request):
    """ Returns all proxies in json format """    

    return HttpResponse(get_json_model(models.Proxy), content_type='application/json')

def get_users (request):
    
    """ Returns all users in json format """
        
    return HttpResponse(get_json_model(models.User), content_type='application/json')

def get_locations (request):
    
    """ Returns all locations in json format """
    
    return HttpResponse(get_json_model(models.Location), content_type='application/json')
    
def get_streams (request):
    """ Returns names of the current streamers in comunidad mc, as json format """
    
    # get current streams
    twitch = TwitchApi()
    streams = twitch.get_current_streams ()
    
    # Get streamers
    streamers = list(map(lambda stream: stream.user.user_name, streams))
    data_json = {"streams": streamers}
        
    return JsonResponse (data_json)