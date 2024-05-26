from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpRequest, HttpResponseRedirect, Http404


# Create your views here.
challenges = {
    "jan": "I am january challenge",
    "feb": "I am february challenge",
    "mar": "I am march challenge",
    "apr": "I am april challenge",
    "may": "I am may challenge",
    "jun": "I am june challenge",
    "jul": "I am july challenge",
    "aug": "I am august challenge",
    "sep": "I am september challenge",
    "oct": "I am october challenge",
    "nov": "I am november challenge",
    "dec": "I am december challenge",
}


def monthly_challenge_by_string(request: HttpRequest, month):

    try:
        return HttpResponse(challenges.get(month))
    except:
        return HttpResponseNotFound("Not found")


def monthly_challenge_by_index(request: HttpRequest, index: int):
    forward_month = list(challenges.keys())
    try:
        return HttpResponseRedirect(forward_month[index - 1])
    except IndexError:
        return HttpResponseNotFound("Could not find challenge")
