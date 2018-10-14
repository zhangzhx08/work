# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token


def csrf(request):
    # csrf_token = get_token(request)
    # context = {'csrf_token': csrf_token}
    get_token(request)
    context = {'csrf_token': 'haha'}
    return JsonResponse(context)
